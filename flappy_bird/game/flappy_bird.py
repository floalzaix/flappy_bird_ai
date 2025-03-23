from tkinter import Tk

from config.config_manager import get_config_param

from models.world import World
from models.pipe import Pipe

from views.view_world import ViewWorld

from controllers.pipes_rolling import PipesRolling
from controllers.gravity import Gravity
from controllers.keyboard import Keyboard
from controllers.game_loop import GameLoop

class FlappyBird(Tk):
    """ The classical Flappy Bird game ! """
    
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
        
        # Setting up actionners 
        self.__roller = PipesRolling(self.__world)
        self.__gravity = Gravity(self.__world)
        self.__keyboard = Keyboard(self.__gravity, self.__view_world)
        
        # Setting up the thread game
        self.__game_loop = GameLoop(self.__roller, self.__gravity, self.__world)
        self.__game_loop.start()
        
        # Starting the views' loop
        self._initialise_views_loop()
        
    def _initialise_views_loop(self):
        self.mainloop() 
        
FlappyBird()