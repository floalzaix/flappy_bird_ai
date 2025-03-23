from config.config_manager import get_config_param

from models.world import World
from models.pipe import Pipe

class PipesRolling:
    """ Handles rolling of the pipes meaning the -3 movement on the x axis """
    
    def __init__(self, world):
        # Importing pipes rolling config
        self.__rolls_before_new = get_config_param("pipes_rolling", "rolls_before_new")
        self.__initial_speed = get_config_param("pipes_rolling", "initial_speed")
        self.__delta_t = get_config_param("time", "delta_t")
        
        self.__world = world
        
        # Parameters 
        self.reset()
        
    def roll(self):
        """ Meant to roll one time the pipes meaning to make them come -3 
            closer to the bird on the x axis
            
            If the rolls number exceeds the rolls_before_new number then
            creates a new pipe to the game added to the world
            
            @raise ? If when moved the pipes hit the bird
        """
        for pipe in self.__world.get_pipes():
            pipe.move(self.__initial_speed * self.__delta_t, 0)
            
        # Creating new pipe
        if self.__rolls <= 0:
            self.__rolls = self.__rolls_before_new
            self.__world.add_pipe(Pipe(self.__world.get_window_width(), self.__world.get_window_height()))
        else:
            self.__rolls-= 1
            
    def reset(self):
        """ Reset the pipes rolling meaning reset the number of rolls """
        self.__rolls = self.__rolls_before_new