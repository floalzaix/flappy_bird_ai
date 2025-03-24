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
            
            collision = self.__game_api.step(action)
            if collision != None:
                reward = -1000
                n+= 1
                
                # Feedback
                print("Episode num : ", n, " / ", nb_episodes)
            
            reward+= 1 / math.sqrt(data[0]**2 + data[1]**2)