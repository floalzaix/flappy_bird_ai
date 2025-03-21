from tkinter import Canvas

from helpers.update_handler import UpdateListenerCanvas

from models.pipe import Pipe

from views.view_pipe import ViewPipe
from views.view_bird import ViewBird

class ViewWorld(UpdateListenerCanvas, Canvas):
    """ Thic class is a view of the world object and is a tkinter 's Canvas """
    
    def __init__(self, window, width,  height, world, bg):
        UpdateListenerCanvas.__init__(self, self)
        Canvas.__init__(self, window, width = width, height = height, bg = bg)
        
        self.__window = window
        
        # Handling bird's view
        self.__view_bird = ViewBird(self, world.get_bird())
        
        # Creating a view_pipe list
        self.__views_pipes = [] 
        
        # Putting everything to place
        self.pack()
        
        # Adding listener
        world.add_update_listener(self)
        
    def draw(self):
        """ Draws the world's objects calling their functions """
        self.__view_bird.draw()
        for view in self.__views_pipes:
            view.draw()
    
    def delete(self):
        """ Deletes from this Canvas its elements 
        
            @raises Exception if the element is deleted but not drawn in 
            the first place
        """
        self.__view_bird.delete()
        for view in self.__views_pipes:
            view.delete()
            
    def update_canvas(self, event):
        """ Updates itself so that change like mvt can be seen """
        self.__view_bird.update(event)
        for view in self.__views_pipes:
            view.update(event)
            
        # Adding the new pipe if there is one
        new = event.get_new()
        if type(new) == Pipe:
            new_view = ViewPipe(self, new)
            self.__views_pipes.append(new_view)