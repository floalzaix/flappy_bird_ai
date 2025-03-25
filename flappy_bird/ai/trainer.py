import math

from game.flappy_bird import FlappyBird

class Trainer:
    """ An AI Trainer """
    
    def __init__(self, q_algo, game_api):
        self.__q_algo = q_algo
        self.__game_api = game_api
        
    def train(self, nb_episodes):
        """ Trains accordingly to the number of episodes """
        reward = 0
        n = 0
        while nb_episodes > n:
            # Getting the game data
            data = self.__game_api.get_data()
            
            # AI's action
            action = self.__q_algo.execute(data, reward)
            
            # Step in the game + reward
            reward = 0
            
            if action == 1:
                reward-= 10
                
            #### REVOIR notamment au niveau des plus de 5 sauts
            
            collision = self.__game_api.step(action)
            if collision != None:
                reward = -1000000
                n+= 1
                
                # Feedback
                print("Episode num : ", n, " / ", nb_episodes)
            
            res = math.sqrt(data[1]**2)
            if res <= 1 and res >= 0:
                reward+= 1000
            elif res <= 30 and res > 1:
                reward+=  30 / res
            else:
                reward-= res // 30