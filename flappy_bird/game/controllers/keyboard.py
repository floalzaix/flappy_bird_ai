from game.config.config_manager import get_config_param

class Keyboard:
    """ Manages the keyboard's inputs of a view_world 

        It associates a key to the action of jumping for the bird
    """
    
    def __init__(self, gravity, view_world):
        # Importing the keyboard config
        self.__key = get_config_param("keyboard", "key")
        
        self.__gravity = gravity
        self.__view_world = view_world
        
        # Binding the key
        self.__view_world.focus_set()
        self.__view_world.bind("<KeyPress>", self.__on_key)
        
    def __on_key(self, event):
        """ Handles the key pressed event and chek if the pressed key is
            the one expected and if so then jump
        """
        if event.keysym == self.__key:
            self.__gravity.bird_jump()