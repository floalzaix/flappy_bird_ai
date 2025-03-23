from config.config_manager import get_config_param

from helpers.update_handler import UpdateListenerCanvas

class ViewScore(UpdateListenerCanvas):
    """ Displays the score """
    
    def __init__(self, view_world, score):
        super().__init__(view_world)
        
        # Importing score config
        self.__x = view_world.get_width() / 100 * get_config_param("score", "width_pourcentage")
        self.__y = get_config_param("score", "top_padding")
        
        self.__view_world = view_world
        self.__score = score
        
        # Adding itself as a update listener to the score
        self.__score.add_update_listener(self)
        
        # Drawing
        self.draw()
        
    def draw(self):
        """ Draws the text on the view """
        self.__score_id = self.__view_world.create_text(self.__x, self.__y, anchor = "n", text = self.__score.get_text(), font = ("Arial", 40, "bold"), fill = "white")
        
    def update_canvas(self, event):
        e_id = event.get_id()
        
        if e_id == "increase_score" or e_id == "decrease_score" or e_id == "reset_score":
            self.__view_world.itemconfig(self.__score_id, text = event.get_new().get_text())