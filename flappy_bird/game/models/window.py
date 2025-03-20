from ..config.config import get_config_param

class Window:
    """ Handles the game windows including a bird object and 
        pipes.
    """
    
    def __init__(self):
        # Importing the window config
        self.width = get_config_param("window", "width")
        self.height = get_config_param("window", "height")
        self.bg = get_config_param("window", "background")