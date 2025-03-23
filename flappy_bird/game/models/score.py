from helpers.update_handler import UpdateSupport, UpdateEvent

class Score(UpdateSupport):
    """ Keeps track of the score """
    
    def __init__(self):
        super().__init__()
        
        self.__score = 0
        
    def increase_score(self, amount):
        self.__score+= amount
        
        # Action listeners
        self.action_listeners(UpdateEvent("increase_score", None, self))
        
    def decrease_score(self, amount):
        self.__score-= amount
        
        # Action_listeners
        self.action_listeners(UpdateEvent("decrease_score", None, self))
        
    def reset_score(self):
        self.__score = 0
        
        # Action listeners
        self.action_listeners(UpdateEvent("reset_score", None, self))
        
    # Getters setters
    def get_text(self):
        return self.__score