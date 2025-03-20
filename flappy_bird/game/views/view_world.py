from tkinter import Canvas

from models.pipe import Pipe

from views.view_pipe import ViewPipe
from views.view_bird import ViewBird

class ViewWorld(Canvas):
    """ Thic class is a view of the world object and is a tkinter 's Canvas """
    
    def __init__(self, window, width,  height, world, bg):
        super().__init__(window, width = width, height = height, bg = bg)
        
        self.__window = window
        
        # Handling bird's view
        self.__view_bird = ViewBird(self, world.get_bird())
        
        # Creating a view_pipe list
        self.__views_pipes = [] 
        
        # Putting everything to place
        self.pack()
        
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
            
    def update(self):
        """ Updates itself so that change like mvt can be seen """
        self.__view_bird.update()
        for view in self.__views_pipes:
            view.update()