class FlappyBirdAPI:
    """ The flappy bird API which allows for a program to access game data
        and also make some actions on the game (jump ...)    
    """
    
    def __init__(self, flappy_bird):
        self.__flappy_bird = flappy_bird
        
        # Initialize
        self.__flappy_bird.create_game_logic()
        
        
    def get_data(self):
        """ Returns the data of the game : vector_next_pipe_center_x, vector_next_pipe_center_y """
        world = self.__flappy_bird.get_world()
        
        bird = world.get_bird()
        bird_center_x = bird.get_x() + bird.get_width() // 2
        bird_center_y = bird.get_y() + bird.get_height() // 2
        
        pipe = world.get_pipes()[0]
        pipe_center_x = pipe.get_x() + pipe.get_width() // 2
        pipe_center_y = pipe.get_y() + pipe.get_delta() // 2
        
        return (pipe_center_x - bird_center_x, pipe_center_y - bird_center_y)
        
    def step(self, action):
        """ Execute a step of the game 

            @return The collision type if there is one
        """
        return self.__flappy_bird.step(action)
    
    def add_game_listener(self, game_listener):
        """ Adds a listener to the game loop so that when a step in the loop
            is taken then it triggers the listener
        """
        self.__flappy_bird.get_game_loop().add_update_listener(game_listener)
        
    def bird_jump(self):
        """ Makes the bird jump """
        self.__flappy_bird.get_gravity().bird_jump()
    
    def show(self):
        """ Shows it self in a window calling the app show method """
        self.__flappy_bird.create_window()
        
    def start(self):
        """ Starts the Flappy Bird game """
        self.__flappy_bird.start_game()
        
    def reset(self):
        """ Resets the pipes rolling, the gravity and the world """
        self.__flappy_bird.reset()