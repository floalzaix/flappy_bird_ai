import numpy as np

from time import sleep
from config.config_manager import get_config_param

class FlappyBirdAPI:
    """ The flappy bird API which allows for a program to access game data
        and also make some actions on the game (jump ...)    
    """
    
    def __init__(self, flappy_bird):
        self.__flappy_bird = flappy_bird
        self.__episode_counter_stats = get_config_param("api", "episodes_before_calc_stats_reset_data")
        
        # Initialize
        self.__flappy_bird.create_game_logic()
        
        # Stores data values for stats
        self.__datas = []                           # The data is updated each time get_data is called
        self.__max_score_all_games = 0              # The max of all games
        self.__max_episode = 0                      # The episode to which the max was reached
        self.__stats = (np.zeros((4, 4)), 0, 0)       # The stats of the game means, maxs, mins, stds + max_score + max_episode (see calculate_stats)
        
        # Counters
        self.__counter_stats = 0
        
    def get_data(self):
        """ Returns the data of the game : vector_next_pipe_center_x, vector_next_pipe_center_y """
        world = self.__flappy_bird.get_world()
        
        bird = world.get_bird()
        bird_center_x = bird.get_x() + bird.get_width() // 2
        bird_center_y = bird.get_y() + bird.get_height() // 2
        
        pipe = world.get_pipes()[0]
        pipe_center_x = pipe.get_x() + pipe.get_width() // 2
        pipe_center_y = pipe.get_y() + pipe.get_delta() // 2
        
        score = world.get_score().get_value()
        
        # Storring data
        self.__datas.append((pipe_center_x - bird_center_x, pipe_center_y - bird_center_y, self.__flappy_bird.get_gravity().get_v_y(), score))
        
        return (pipe_center_x - bird_center_x, pipe_center_y - bird_center_y, self.__flappy_bird.get_gravity().get_v_y())
    
    def calculate_stats(self, num_episodes):
        """ Calculate the statistics of the game's parameters : pipe's dist,
            bird's y, bird's y velocity.
            
            These stats are the last self.__episodes_counter_start ones
        """
        if num_episodes % self.__episode_counter_stats == 0 and self.__counter_stats == 0:
            self.__counter_stats = 1
            
            # Getting the data
            data = np.array(self.__datas)
            
            # Result
            res = []
            
            for i in range(4):
                res.append([])
                res[i].append(np.mean(data[:, i]))
                res[i].append(np.min(data[:, i]))
                res[i].append(np.max(data[:, i]))
                res[i].append(np.std(data[:, i]))
                
            if res[3][2] >= self.__max_score_all_games:
                self.__max_score_all_games = res[3][2]
                self.__max_episode = num_episodes
            
            self.__stats = (res, self.__max_score_all_games, self.__max_episode)
        elif num_episodes % self.__episode_counter_stats != 0:
            self.__counter_stats = 0
            self.__datas = []
        
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
        
    def play(self, action):
        """ Plays to the game according the ai decision being action """
        if action == 1:
            self.bird_jump()
        
    def reset(self):
        """ Resets the pipes rolling, the gravity and the world """
        self.__flappy_bird.reset()
        
    # Getters setters
    def get_stats(self):
        return self.__stats