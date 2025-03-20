from tkinter import Canvas

from models.bird import Bird

from views.view_rectangle import ViewRectangle 

class ViewBird(ViewRectangle):
    """ The view of the bird object which displays a rectangle of the
        bird in a red color. Can add the bird, delete it from the canvas
        which is the view of the world. Finally, can update the bird so 
        that when given a move its moven is seen.
    """
    
    def __init__(self, view_world, bird):
        # Creating its rectangle
        super().__init__(view_world, bird.get_rectangle())
        
    
        
        
        