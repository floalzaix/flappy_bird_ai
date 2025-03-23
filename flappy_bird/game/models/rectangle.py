from helpers.update_handler import UpdateSupport, UpdateEvent

class Rectangle(UpdateSupport):
    """ A class that manages a rectangle's coords and sizes"""
    
    def __init__(self, x, y, width, height, color):
        super().__init__()
        
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color
        
        # Initialisating the 2nd point coordinates
        self.__x1 = self.__x + self.__width
        self.__y1 = self.__y + self.__height
        
    def move(self, x, y):
        """ Allows for us to move the rectangle """
        self.__x+= x
        self.__y+= y
        self.__x1+= x
        self.__y1+= y
        self.action_listeners(UpdateEvent("move_rectangle", None, self))
        
    # Getters setters
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def get_x1(self):
        return self.__x1
    def get_y1(self):
        return self.__y1
    def get_color(self):
        return self.__color
        
    