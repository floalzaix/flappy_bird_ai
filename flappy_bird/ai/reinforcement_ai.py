import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from threading import Thread

from config.config_manager import get_config_param

from game.helpers.update_handler import UpdateListener

from game.flappy_bird import FlappyBird
from ai.apis.flappy_bird_api import FlappyBirdAPI
from ai.trainers.flappy_bird_trainer import FlappyBirdTrainer
from q_algo import QAlgo

from saves.saver import Saver

class ReinforcementAI(UpdateListener):
    """ The AI which trains on a game like Flappy Bird based on Q-Learning """
    
    def __init__(self, trainer):
        # Importing configuration
        self.__nb_actions = get_config_param("q_algo", "nb_actions")
        self.__alpha = get_config_param("q_algo", "alpha")
        self.__gamma = get_config_param("q_algo", "gamma")
        self.__start_epsilon = get_config_param("q_algo", "start_epsilon")
        self.__decay_epsilon = get_config_param("q_algo", "decay_epsilon")
        self.__min_epsilon = get_config_param("q_algo", "min_epsilon")
        self.__nb_params = get_config_param("q_algo", "nb_params")
        self.__quatums = get_config_param("q_algo", "quantums")
        
        self.__file_name = get_config_param("saver", "file_name")
        self.__episode_counter_save = get_config_param("saver", "episode_counter_save") # Episodes counter before save
        self.__saver = Saver(self.__file_name, self.__episode_counter_save)
        
        self.__game_api = trainer.get_game_api()
        self.__trainer = trainer
        
        self.__q_algo = QAlgo(self.__nb_actions, self.__alpha, self.__gamma, self.__start_epsilon, self.__decay_epsilon, self.__min_epsilon, self.__nb_params, self.__quatums, self.__saver)
        
        self.__num_episodes = 0
        
        # Adding it self as a game listener
        self.__game_api.add_game_listener(self)
        
    def load_data(self):
        """ Loads data from the saver's file """
        self.__num_episodes = self.__q_algo.load_q_matrix()
        
    def train(self, nb_episodes, in_thread):
        """ Trains the model according to the number of episodes

            @param in_thread Executes the training in a thread so that it can
                             be seen in a tkinter window for instance
        """
        if nb_episodes > self.__num_episodes:
            if in_thread:
                thread = Thread(daemon = True, target = self.__trainer.train, args = (self.__q_algo, self.__num_episodes, nb_episodes, ))
                thread.start()
            else:
                self.__trainer.train(self.__q_algo, self.__num_episodes, nb_episodes)
        self.__num_episodes = nb_episodes
        
    def update(self, event):
        """ Plays the game """
        if event.get_id() == "step_in_loop":
            # Getting the game data
            data = self.__game_api.get_data()
            
            # AI's action
            action = self.__q_algo.play(data)
            
            # Playing with the api
            self.__game_api.play(action)
        
    def show(self):
        """ Shows it self in a window calling the app show method """
        self.__game_api.show()
    
# Game     
game = FlappyBird()
game_api = FlappyBirdAPI(game)
trainer = FlappyBirdTrainer(game_api)

# AI ! 
ai = ReinforcementAI(trainer)

## Training
ai.train(200000, False)

# Simulating a game to see how ai does
game_api.start()
ai.show()
        
        