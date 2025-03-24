from tkinter import Tk

from config.config_manager import get_config_param

from models.world import World
from models.pipe import Pipe

from views.view_world import ViewWorld

from controllers.pipes_rolling import PipesRolling
from controllers.gravity import Gravity 
from controllers.keyboard import Keyboard
from controllers.game_loop import GameLoop

class FlappyBird:
    """ The classical Flappy Bird game ! """
    
    def __init__(self):                                                     
        # Importing the window config
        self.__window_width = get_config_param("window", "width")
        self.__window_height = get_config_param("window", "height")
        self.__window_bg = get_config_param("window", "bg")
        self.__window_title = get_config_param("window", "title")
        
    def create_game_logic(self):
        """ Creates the necessary elements of the game logic """
        # Creating the world
        self.__world = World(self.__window_width, self.__window_height)
        
        # Setting up actionners 
        self.__roller = PipesRolling(self.__world)
        self.__gravity = Gravity(self.__world)
        
        # Setting up the thread game
        self.__game_loop = GameLoop(self.__roller, self.__gravity, self.__world)
    
    def create_window(self):
        """ Creates a window to have an interactive and visible game 
        
            Do not call before create_game_logic
        """
        self.__window = Tk(self.__window_title)
        
        # Creating the world view
        self.__view_world = ViewWorld(self.__window, self.__window_width, self.__window_height, self.__world, self.__window_bg)
        
        # Setting up keyboard
        self.__keyboard = Keyboard(self.__gravity, self.__view_world)
        
        # Starting the views' loop
        self.__window.mainloop()
        
    def start_game(self):
        """ Starts the game as a normal game """
        self.__game_loop.start()
        
    def step(self):
        """ Makes a step un the game """
        return self.__game_loop.step()
    
    # Getters setters
    def get_world(self):
        return self.__world
        
game = FlappyBird()
game.create_game_logic()
game.start_game()
game.create_window()