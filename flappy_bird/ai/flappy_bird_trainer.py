from config.config_manager import get_config_param

from game.flappy_bird import FlappyBird

class FlappyBirdTrainer:
    """ An AI Trainer for flappy bird """
    
    def __init__(self, q_algo, reward_sys):
        # Importing configuration
        self.__alpha = get_config_param("q_algo", "alpha")
        self.__gamma = get_config_param("q_algo", "gamma")
        self.__start_epsilon = get_config_param("q_algo", "start_epsilon")
        self.__decay_epsilon = get_config_param("q_algo", "alpha")
        self.__min_epsilon = get_config_param("q_algo", "min_epsilon")
        self.__nb_params = get_config_param("q_algo", "nb_params")
        self.__quatums = get_config_param("q_algo", "quantums")
        
        self.__q_algo = q_algo
        self.__reward_sys = reward_sys
        
        # Creating an instance of the game
        self.__flappy_bird = FlappyBird()
        self.__flappy_bird.create_game_logic()