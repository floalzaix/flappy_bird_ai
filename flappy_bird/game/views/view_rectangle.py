from tkinter import Canvas

from helpers.update_handler import UpdateListenerCanvas

from models.rectangle import Rectangle

class ViewRectangle(UpdateListenerCanvas):
    """ This is the view of the rectangle object which
        given a Canvas can display itself on it and also
        delete itself and update the rectangle display
    """
    
    def __init__(self, view_world, rectangle):
        super().__init__(view_world)
        
        self.__view_world = view_world
        self.__rectangle = rectangle
        
        # Adding the ractangle to the view
        self.draw()
        
        # Set listener of the rectangle
        self.__rectangle.add_update_listener(self)
        
    def draw(self):
        """ Draws the rectangle on the canvas which is the view of the world """
        self.__rectangle_id = self.__view_world.create_rectangle(self.__rectangle.get_x(), self.__rectangle.get_y(), self.__rectangle.get_x1(), self.__rectangle.get_y1(), fill=self.__rectangle.get_color())
        
    def delete(self):
        """ Deletes the rectangle from the Canvas which is the world's view 

            @raise Exception When the rectangle is not on the Canvas
        """
        self.__view_world.delete(self.__rectangle_id)
        self.__rectangle.remove_update_listener(self)
        
    def update_canvas(self, event):
        """ Update the view of the rectangle on the Canvas which is the world's view

            It aims at the fact that every time a rectangle is moved, this function is
            called in order to update the view.
        """
        if event.get_id() == "move_rectangle":
            self.__view_world.coords(self.__rectangle_id, self.__rectangle.get_x(), self.__rectangle.get_y(), self.__rectangle.get_x1(), self.__rectangle.get_y1())
