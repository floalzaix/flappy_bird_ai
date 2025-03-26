import math

from trainers.trainer import Trainer

class FlappyBirdTrainer(Trainer):
    """ An AI Trainer """
        
    def train(self, q_algo, num_episodes, nb_episodes):
        """ Trains accordingly to the number of episodes """
        reward = 0
        n = num_episodes
        while nb_episodes > n:
            # Getting the game data
            data = self._game_api.get_data()
            
            # AI's action
            action = q_algo.execute(data, reward, n, self._game_api.get_stats)
            
            # Step in the game + reward
            reward = 0
            
            if action == 1:
                reward-= 10
                
            #### REVOIR notamment au niveau des plus de 5 sauts
            
            collision = self._game_api.step(action)
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
                
            # Show stats
            self._game_api.calculate_stats(n)