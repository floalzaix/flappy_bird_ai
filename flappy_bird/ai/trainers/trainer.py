from abc import ABC, abstractmethod

class Trainer(ABC):
    """ This class is the model of the trainer for the reinforcement ai """
    
    def __init__(self, game_api):
        self._game_api = game_api
        
    @abstractmethod
    def train(self, q_algo, num_episodes, nb_episodes):
        """ This function trains the q algorithm 
        
            @param num_episodes The start episode (numero of the episode)
            @param nb_episodes  The number of episodes that 
                                needs to be reached 
        """
        pass
    
    # Getters setters
    def get_game_api(self):
        return self._game_api