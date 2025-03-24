class CollisionError(Exception):
    """ An special exception to handle the collisions when there is one
    
        Types :
        
            * COLLISION_SKY             
            * COLLISION_GROUND          
            * COLLISION_ENTERING_PIPE
            * COLLISION_EXITING_PIPE

        @param type The type of the collision
    """
    
    COLLISION_SKY = 0
    COLLISION_GROUND = 1
    COLLISION_ENTERING_PIPE = 2
    COLLISION_EXITING_PIPE = 3
    
    def __init__(self, type):
        super().__init__("Collision")
        
        self.__type = type
        
    # Getters setters
    def get_type(self):
        return self.__type
    
    