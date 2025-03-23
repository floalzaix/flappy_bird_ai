from tkinter import Canvas

from helpers.update_handler import UpdateListenerCanvas

from models.pipe import Pipe

from views.view_pipe import ViewPipe
from views.view_bird import ViewBird
from views.view_score import ViewScore

class ViewWorld(UpdateListenerCanvas, Canvas):
    """ Thic class is a view of the world object and is a tkinter 's Canvas """
    
    def __init__(self, window, width,  height, world, bg):
        UpdateListenerCanvas.__init__(self, self)
        Canvas.__init__(self, window, width = width, height = height, bg = bg)
        
        self.__world = world
        self.__width = width
        self.__height = height
        
        # Handling bird's view
        ViewBird(self, world.get_bird())
        
        # Creating a view_pipe list
        self.__views_pipes = [] 
        for pipe in self.__world.get_pipes():
            self.__views_pipes.append(ViewPipe(self, pipe))
        
        # Putting everything to place
        self.pack()
        
        # Adding listener
        world.add_update_listener(self)
        
        # Show score
        ViewScore(self, self.__world.get_score())
            
    def update_canvas(self, event):
        """ Updates when there is an add or removal of a pipe """
           
        # Adding the new pipe if there is one
        if event.get_id() == "add_pipe":
            new = event.get_new()
            new_view = ViewPipe(self, new)
            self.__views_pipes.append(new_view)
            
        # Removing the pipe if there is one to remove
        if event.get_id() == "remove_pipe":
            old = event.get_new()
            old_view = self.__search_view_pipe(old)
            old_view.delete()
            self.__views_pipes.remove(old_view)
            
    # Processing functions
    def __search_view_pipe(self, pipe):
        """ Searches the view linked to the pipe 
        
            @param pipe The pipe 
            @return The view linked to it
            @raise ValueError If the view is not found in the 
                              class pipes' views
        """
        for view_pipe in self.__views_pipes:
            if view_pipe.get_pipe() == pipe:
                return view_pipe
        raise ValueError
    
    # Getters setters
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height