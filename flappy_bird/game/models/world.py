from config.config_manager import get_config_param

from models.bird import  Bird

class World:
    """ Handles the game windows including a bird object and 
        pipes.
    """
    
    def __init__(self, window_width, window_height):
        self.__window_width = window_width
        self.__window_height= window_height
        
        # Adding the bird to the world
        self.__bird = Bird(self.__window_width, self.__window_height)
        
        # Creating the list of pipes
        self.__pipes = []
        
    # Getters setters
    def get_bird(self):
        return self.__bird