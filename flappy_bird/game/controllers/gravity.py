from config.config_manager import get_config_param

class Gravity:
    """ This class is made to handle the gravity of the bird 
        according to the two parameters : delta_t and g 
        
        It also includes the action of jumping 
    """
    
    def __init__(self, world):
        # Importing the gravity config
        self.__delta_t = get_config_param("time", "delta_t")
        self.__g = get_config_param("gravity", "g")
        self.__jump_a = get_config_param("gravity", "jump_a")
        self.__jump_a_duration = get_config_param("gravity", "jump_a_duration")
        
        self.__world = world
        
        # Setting up the parameters
        self.__v = self.__delta_t
        self.__jump_a_time_left = 0
        
    def action_gravite(self):
        """ Simulate the gravity for the bird. It calculates it speed and
            position thanks to g
        """
        # Carry on the gravity
        self.__world.get_bird().move(0, -int(self.__v * self.__delta_t))
        
        # Update the speed according to the accelerations
        self.__v+= (self.__jump_a * (self.__jump_a_time_left > 0) + self.__g) * self.__delta_t
        
        #Updating the jump acceleration duration
        if self.__jump_a > 0:
            self.__jump_a_time_left-= self.__delta_t
        
    def bird_jump(self):
        """ Simulate the jump of the bird which adds an acceleration """
        
        # Updating the jump duration
        self.__jump_a_time_left = self.__jump_a_duration