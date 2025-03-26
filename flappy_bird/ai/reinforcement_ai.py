import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from threading import Thread

from config.config_manager import get_config_param

from game.helpers.update_handler import UpdateListener

from game.flappy_bird import FlappyBird
from flappy_bird_api import FlappyBirdAPI
from trainer import Trainer
from q_algo import QAlgo

from saves.saver import Saver

class ReinforcementAI(UpdateListener):
    """ The AI which trains on a game like Flappy Bird based on Q-Learning 
    
        @param mem Loads data from a file if True
    """
    
    def __init__(self, game_api, mem):
        # Importing configuration
        self.__alpha = get_config_param("q_algo", "alpha")
        self.__gamma = get_config_param("q_algo", "gamma")
        self.__start_epsilon = get_config_param("q_algo", "start_epsilon")
        self.__decay_epsilon = get_config_param("q_algo", "decay_epsilon")
        self.__min_epsilon = get_config_param("q_algo", "min_epsilon")
        self.__nb_params = get_config_param("q_algo", "nb_params")
        self.__quatums = get_config_param("q_algo", "quantums")
        self.__file_name = get_config_param("q_algo", "file_name")
        
        self.__game_api = game_api
        
        self.__saver = Saver(self.__file_name)
        self.__q_algo = QAlgo(self.__alpha, self.__gamma, self.__start_epsilon, self.__decay_epsilon, self.__min_epsilon, self.__nb_params, self.__quatums, self.__saver)
        self.__trainer = Trainer(self.__q_algo, self.__game_api)
        
        self.__num_episodes = 0
        if mem:
            self.__num_episodes = self.__q_algo.load_q_matrix()
        
        # Adding it self as a game listener
        self.__game_api.add_game_listener(self)
        
    def train(self, nb_episodes, in_thread):
        """ Trains the model according to the number of episodes """
        if nb_episodes > self.__num_episodes:
            if in_thread:
                thread = Thread(daemon = True, target = self.__trainer.train, args = (self.__num_episodes, nb_episodes, ))
                thread.start()
            else:
                self.__trainer.train(self.__num_episodes, nb_episodes)
        
    def update(self, event):
        """ Plays the game """
        if event.get_id() == "step_in_loop":
            # Getting the game data
            data = self.__game_api.get_data()
            
            # AI's action
            action = self.__q_algo.play(data)
            if action == 1:
                self.__game_api.bird_jump()
        
    def show(self):
        """ Shows it self in a window calling the app show method """
        self.__game_api.show()
        
game = FlappyBird()
game_api = FlappyBirdAPI(game)
ai = ReinforcementAI(game_api, False)

ai.train(200000, False)

game_api.start()
ai.show()
        
        