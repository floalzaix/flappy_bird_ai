from ..config.config import get_config_param

class Bird:
    """ This class is the simulation of a bird bying a
        red rectangle
    """
    
    def __init__(self):
        # Importing window config
        window_width = get_config_param("window", "width")
        window_height = get_config_param("window", "height")
        
        # Importing bird config
        self.width = get_config_param("bird", "width")
        self.height = get_config_param("bird", "height")
        
        # Calculating initial position
        self.x = window_width // 10
        self.y = window_height // 2 - self.height // 2
        