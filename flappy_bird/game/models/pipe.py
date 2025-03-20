import random as rd

from config.config_manager import get_config_param

from models.rectangle import Rectangle

class Pipe:
    """ This class is the illustration of a pipe in the flapy bird
        game. It thought to handle the dimensions and the mouvement
        of the pipe.
        
        A pipe is a two pieces rectangle One above and one bellow.
        
        Its coordinates are (x, y, delta) where the point (x, y) is
        the upper rectangle' s closer to the bird bottom left corner
        and the delta is the distance to the lower rectangle
    """
    
    def __init__(self, window_width, window_height):
        # Importing window config
        self.__window_width = window_width
        self.__window_height = window_height
        
        # Importation of pipe config
        self.__width = get_config_param("pipe", "width")
        self.__delta = get_config_param("pipe", "delta")
        self.__y_quantification = get_config_param("pipe", "y_quantification")
        self.__y_min_max_quantum = get_config_param("pipe", "y_min_max_quantum")
        
        # Verification des imports
        assert self.__y_quantification > self.__y_min_max_quantum + 1, "The pipes quantification must be 2 times higher than the y_min_max"
        
        # Initialising its coords
        self.__x = int(self.__window_width / 100 * get_config_param("pipe", "start_x_pourcentage"))
        self.__y = int((rd.randint(0, self.__y_quantification - 2 - 2 * self.__y_min_max_quantum) + self.__y_min_max_quantum) * self.__window_height / self.__y_quantification)
        
        # Initialising its rectangles
        self.__upper_rect = Rectangle(self.__x, 0, self.__width, self.__y, "green")
        y2 = self.__y + self.__delta
        self.__lower_rect = Rectangle(self.__x, y2, self.__width, self.__window_height - y2, "green")
        
    def __update_rectangles(self, delta_x, delta_y):
        """ Updates the parameters of the upper and lower rectangle of the pipe """
        self.__upper_rect.move(delta_x, delta_y)
        self.__lower_rect.move(delta_x, delta_y)
        
    def move(self, delta_x, delta_y):
        """ Moves the object to the coord x + delta_x and y + delta_y and 
            actualises the rectangles 
        """
        self.__x+= delta_x
        self.__y+= delta_y
        self.__update_rectangles(delta_x, delta_y)
        
    # Getters setters 
    def get_upper_rectangle(self):
        return self.__upper_rect 
    def get_lower_rectangle(self):
        return self.__lower_rect
        