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
        
    def add_pipe(self, pipe):
        self.__pipe.append(pipe)
        
    def remove_pipe(self, pipe):
        self.__pipes.remove(pipe)
        
    # Getters setters
    def get_bird(self):
        return self.__bird
    def get_pipes(self):
        return self.__pipes
    def get_window_width(self):
        return self.__window_width
    def get_window_height(self):
        return self.__window_height