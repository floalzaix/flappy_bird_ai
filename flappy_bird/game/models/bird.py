from ..config.config import get_config_param
from rectangle import Rectangle

class Bird:
    """ This class is the simulation of a bird bying a
        red rectangle
    """
    
    def __init__(self, window_width, window_height):
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
        self.update_rectangle()
        
    def update_rectangle(self):
        self.__rectangle = Rectangle(self.__x, self.__y, self.__width, self.__height)
        