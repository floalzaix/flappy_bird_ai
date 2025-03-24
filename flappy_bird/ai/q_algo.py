from random import uniform, choice
from numpy import argmax

class QAlgo:
    """ The Q-Learning algorithm to be trained on games with two possibles
        actions. Like Flappy Bird. Actions : 0 or 1

        @param alpha    The learning speed (0 - 1)
        @param gamme    How much it values the future rewards (0 - 1)
        @param epsilon  The discovery rate exploration(1) -  exploitation(0) 
    """
    
    def __init__(self, alpha, gamma, epsilon, nb_params, quantums):
        assert len(quantums) == nb_params, "Errors size don't match"
        
        self.__alpha = alpha
        self.__gamma = gamma
        self.__epsilon = epsilon
        self.__nb_params = nb_params
        self.__quantums = quantums
        
        # The matrice (which is a dict)
        self.__q = {}
        
    def quantification_state(self, values):
        """ Quantifies the state given the game parameters. The parameters
            must be integer float or string but not arrays or tab or dict
            because a tuple is const
        
            @param values   The values like speed, position, ...
            @param quantums  The parameters which will divide the values
            
            @return The state to be used by the q-learning algo
            
            @raise AssertionError If the tabs are not the same length
            
            Ex : values = [bird_x, bird_y, dist_pipe, ...]
                 quantums = [10, 10, 5, ...]
                 
                 returns : (bird_x // 10, bird_y // 10, dist_pipe // 5)
                 
        """
        assert len(values) == self.__nb_params, "Error the quantification needs to have two arrays the same sizes"
        return (values[i] // self.__quantums[i] for i in range(self.__nb_params))
        
    def get_g_value(self, state, action):
        """ Gets the q values in the matrix of a given 
            2-uple (state, action)    
        """
        # if state not in self.__q: CHECK
            
        return self.__q[state][action]
    
    def choose_next_action(self, state):
        """ Chooses the next action according to the state and the epsilon
            ratio. It has a 1 - epsilon chances to discover and epsilon 
            chance to take the best actions according to what it already 
            knows
            
            @param state The state in which we want to select the next 
                         best action
                         
            @return The next action discovery or explotation
        """
        if uniform(0, 1) < 1 - self.__epsilon:
            return choice([0, 1]) # CHECK
        
        return argmax(self.__q.get(state, [0, 1]))
    
    def update_q_matrix(self, state, reward, action, next_state):
        """ Update the q matrix that holds the q values of the learning
            algorithm. 
            
            @param state        The current state
            @param action       The action choosed when at the current state
            @param reward       The reward at the current state when action
                                was performed
            @param next_state   The next state when action is performed
            
            It uses the formula :
                q(state, action) = q(state, action) + alpha * (reward + gamme * q(next_state, action_max) + q(state, action))
        """
        qa = self.get_g_value(state, action)
        action_max = argmax(self.__q.get(next_state)) # CHECK
        qna = self.get_g_value(next_state, action_max)
        
        # Updating matrix
        self.__q[state, action] = qa + self.__alpha * (reward + self.__gamma * qna + qa)
        
    def execute(self, game_params, reward):
        """ Executes the algorithm : 
        
            * Quantifies the states
            * Chooses the next action according to espilon and the previous
              ones
            * Updates the matrix accordingly to past decisions
            
            @param game_params The parameters of the game x, y, dist, ...
            
            @returns The choosen action
        """
        
        # Quantifying the states
        state = self.quantification_state(game_params)
        
        # Choosing the next action
        action = self.choose_next_action(state)
        
        # Updating the matrix
        if hasattr(self, "__previous_state") and hasattr(self, "__previous_action"):
            self.update_q_matrix(self.__previous_state, reward, self.__previous_action, state)
            
        # Storing the state and the action 
        self.__previous_state = state
        self.__previous_action = action
        
        return action