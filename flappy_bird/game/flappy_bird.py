from tkinter import Tk

from config.config_manager import get_config_param

from models.world import World
from models.pipe import Pipe

from views.view_world import ViewWorld

from controllers.pipes_rolling import PipesRolling

class FlappyBird(Tk):
    """"""
    
    def __init__(self):
        super().__init__()
        
        # Importing the window config
        self.__window_width = get_config_param("window", "width")
        self.__window_height = get_config_param("window", "height")
        self.__window_bg = get_config_param("window", "bg")
        self.__window_title = get_config_param("window", "title")
        
        # Setting title
        self.title(self.__window_title)
        
        # Creating the world
        self.__world = World(self.__window_width, self.__window_height)
                        
        # Creating the world view
        self.__view_world = ViewWorld(self, self.__window_width, self.__window_height, self.__world, self.__window_bg)
                
        # Starting the views' loop
        self._initialise_views_loop()
        
    def _initialise_views_loop(self):
        self.mainloop() 
        
FlappyBird()