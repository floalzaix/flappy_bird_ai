from tkinter import Canvas

from helpers.update_handler import UpdateEvent

from models.pipe import Pipe

from views.view_rectangle import ViewRectangle 

class ViewPipe:
    """ This is a view of the pipe object. It can be drwn, delete
        or updated.
        
        Still, it is a bit different from the bird view because made
        of multiple rectangles.
        
        Therefore, it does not extends the ViewRectangle
    """
    
    def __init__(self, view_world, pipe):
        self.__view_world = view_world
        self.__pipe = pipe
        
        # Getting pipe's rectangles
        self.__upper_rect = pipe.get_upper_rectangle()
        self.__lower_rect = pipe.get_lower_rectangle()
        
        # Creating rectangles' views
        self.__upper_view = ViewRectangle(self.__view_world, self.__upper_rect)
        self.__lower_view = ViewRectangle(self.__view_world, self.__lower_rect)
        
    def draw(self):
        """ Draws the rectangles. It simply calls their views
            method to do it.
        """
        self.__upper_view.draw()
        self.__lower_view.draw()
        
    def delete(self):
        """ Delete itself from the View meaning deleting its 
            rectangles' view method to delete 
        """
        self.__upper_view.delete()
        self.__lower_view.delete()
        
    def update(self, event):
        """ Updates itself by calling the rectangles' views methods """
        if type(event.get_new()) == Pipe:
            self.__upper_view.update(UpdateEvent(None, event.get_new().get_upper_rectangle()))
            self.__lower_view.update(UpdateEvent(None, event.get_new().get_lower_rectangle()))
        
        