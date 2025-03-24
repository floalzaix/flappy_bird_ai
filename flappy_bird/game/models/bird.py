from helpers.update_handler import UpdateSupport, UpdateEvent

from game.config.config_manager import get_config_param

from models.rectangle import Rectangle

class Bird(UpdateSupport):
    """ This class is the simulation of a bird being a
        red rectangle
    """
    
    def __init__(self, window_width, window_height):
        super().__init__()
        
        # Importing window config
        self.__window_width = window_width
        self.__window_height = window_height
        
        # Importing bird config
        self.__width = get_config_param("bird", "width")
        self.__height = get_config_param("bird", "height")
        
        # Calculating initial position
        self.__x = int(self.__window_width / 100 * get_config_param("bird", "start_x_pourcentage"))
        self.__y = self.__window_height // 2 - self.__height // 2 
        
        # Initialisation of the rectangle
        self.__rectangle = Rectangle(self.__x, self.__y, self.__width, self.__height, "red")
        
    def initial_position(self):
        """ Reset the birds position according to its initial position """
        y_i = self.__window_height // 2 - self.__height // 2    
        self.__update_rectangle(0, y_i - self.__y)
        self.__y = y_i
    
    def __update_rectangle(self, delta_x, delta_y):
        """ Updates the rectangle coordinates of the bird """
        self.__rectangle.move(delta_x, delta_y)
        
    def move(self, delta_x, delta_y):
        """ Moves the object to the coordinates x + dx and y + dy and 
            actualises the rectangle position + actions the listeners
            (being the world) to test for collision
        """
        self.__x+= delta_x
        self.__y+= delta_y
        self.__update_rectangle(delta_x, delta_y)
        
        # Actionning the listeners
        self.action_listeners(UpdateEvent("move_bird", None, self))
        
    # Getters setters
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def get_rectangle(self):
        return self.__rectangle
        