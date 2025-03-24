from threading import Thread, Event
import time

from config.config_manager import get_config_param

from models.collision_error import CollisionError

class GameLoop(Thread):
    """ The main loop of the game : it actions the gravity rolls th pipes
        and does that every separated of delta_t seconds
    """
    
    def __init__(self, pipes_rolling, gravity, world):
        super().__init__(daemon=True)
        
        self.__roller = pipes_rolling
        self.__gravity = gravity
        self.__world = world
        
        # Loading time config
        self.__delta_t = get_config_param("time", "delta_t")
        
        # Flag for stopping the thread
        self.__stop = Event()
        
    def run(self):
        """ The loop """
        while not self.__stop.is_set():
            self.step()
            time.sleep(self.__delta_t)
                
    def step(self):
        """ Makes a step in the game """
        try:
            self.__roller.roll()
            self.__gravity.action_gravity()
        except CollisionError as ce:
            # Handling the Collisions 
            self.restart()
            return ce.get_type()
              
    def stop(self):
        """ Kills the Thread """
        self.__stop.set()
        
    def restart(self):
        """ Reset every parameters of the game to 0 """
        self.__roller.reset()
        self.__gravity.reset()
        self.__world.reset()