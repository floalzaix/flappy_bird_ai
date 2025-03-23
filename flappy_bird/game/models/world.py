from helpers.update_handler import UpdateSupport, UpdateEvent, UpdateListener

from config.config_manager import get_config_param

from models.collision_error import CollisionError
from models.bird import Bird
from models.pipe import Pipe

class World(UpdateSupport, UpdateListener):
    """ Handles the game windows including a bird object and 
        pipes.
    """
    
    def __init__(self, window_width, window_height):
        super().__init__()
        
        self.__window_width = window_width
        self.__window_height= window_height
        
        # Adding the bird to the world
        self.__bird = Bird(self.__window_width, self.__window_height)
        self.__bird.add_update_listener(self)
        
        # Creating the list of pipes
        pipe = Pipe(self.__window_width, self.__window_height)
        pipe.add_update_listener(self)
        self.__pipes = [pipe]
        
    def add_pipe(self, pipe):
        """ Adds a pipe to the pipes of the world. Actionnate a listener
            for the window and adds itself as a listener so that when they
            move it tests for collision
        """
        # Appends listener
        pipe.add_update_listener(self)
                
        self.__pipes.append(pipe)
        
        # Triggers listeners
        self.action_listeners(UpdateEvent("add_pipe", None, pipe))
        
    def remove_pipe(self, pipe):
        """ Remove a pipe same as adding it triggers listeners so that when 
            moved it tests for collision 
        """
        # Removes listener
        pipe.remove_update_listener(self)
        
        self.__pipes.remove(pipe)
        
        # Triggers listeners
        self.action_listeners(UpdateEvent("remove_pipe", None, pipe))
        
    def reset(self):
        """ Reset of the world : bird to initial position and pipes gone """
        self.__bird.initial_position()
        
        for _ in range(len(self.__pipes)):
            self.remove_pipe(self.__pipes[0])
            
        self.add_pipe(Pipe(self.__window_width, self.__window_height))
        
    # Listener
    def update(self, event):
        # Testing collision
        if event.get_id() == "move_bird" or event.get_id() == "move_pipe":
            self.__test_collision()
            
    # Processing functions
    def __test_collision(self):
        """ Testing collision with the ground, the sky and the first pipe
            because it can't collided with the second when thefirst is still
            there
            
            @raise 
        """
        assert len(self.__pipes) > 0, "Error can't test collision if there are no pipes" 
        
        # Getting the birs params
        b_x = self.__bird.get_x() 
        b_y = self.__bird.get_y() 
        b_x1 = self.__bird.get_x() + self.__bird.get_width()
        b_y1 = self.__bird.get_y() + self.__bird.get_height()
        
        # Getting the pipes params
        #
        ### Upper rectangle
        p_upper = self.__pipes[0].get_upper_rectangle()
        p_x = p_upper.get_x()
        p_x1 = p_upper.get_x1()
        p_upper_y = p_upper.get_y1()
        #
        ### Lower rectangle
        p_lower = self.__pipes[0].get_lower_rectangle()
        p_lower_y = p_lower.get_y()
        
        # Testing sky or ground collision
        if b_y <= 0:
            raise CollisionError(CollisionError.COLLISION_SKY)
        
        if b_y1 >= self.__window_height:
            raise CollisionError(CollisionError.COLLISION_GROUND)
        
        # Testing for pipes collisions
        if b_x1 >= p_x and b_x < p_x and (b_y <= p_upper_y or b_y1 >= p_lower_y):
            raise CollisionError(CollisionError.COLLISION_ENTERING_PIPE)
        
        if b_x1 >= p_x and b_x <= p_x1 and (b_y <= p_upper_y or b_y1 >= p_lower_y):
            raise CollisionError(CollisionError.COLLISION_EXITING_PIPE)
        
        # Testing if crossed a pipe
        self.__test_crossed_pipe(b_x, p_x1)
    
    def __test_crossed_pipe(self, b_x, p_x1):
        """ Testing if the bird crossed a pipe and if so then removes it """
        if b_x > p_x1:
            ######################################################################################## A MODIFIER
            self.remove_pipe(self.__pipes[0])
        
    # Getters setters
    def get_bird(self):
        return self.__bird
    def get_pipes(self):
        return self.__pipes
    def get_window_width(self):
        return self.__window_width
    def get_window_height(self):
        return self.__window_height