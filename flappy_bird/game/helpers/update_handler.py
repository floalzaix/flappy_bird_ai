""" ALZAIX Florian

    Similarly to Java, these class are intented to solve the 
    matter of event handling. 
    
    There are meant to be used when an action is done and an 
    this action must have multiple consequences elsewhere.
    
    The class which triggers the event is a SUPPORT.
    
    The classes which must react to the event are the LISTENERS.
    
    ***
    HOW TO USE =>
    As a user the class that needs to triggers an event must 
    extend th support class and call its constructor. For the
    class that reacts to the event, it must extend the one of the 
    listeners class and add it self as a listener to the support
    ***
    
    Here, the support calls every update method of the listeners
    it is the function action_listeners.
    
    There are two types of listeners : the simple one which just
    reacts to the trigger overriding the method UPDATE and the 
    canvas one which executes the same things but in the tkinter
    loop and overrides UPDATE_CANVAS instead.
    
    CAREFUL : don't override the update method when extending 
    th UpdateListenerCanvas it won't be called in the tkinter 
    thread no more.
"""

from abc import ABC, abstractmethod

class UpdateListener(ABC):
    """ This class a the making of a listener. It is thought to
        be extended by a class which needs to do something when
        an action is triggered.
        
        Therefore, when extended the user must define the function 
        in the class to be called when the action is performed.
    """
    
    @abstractmethod
    def update(self, event):
        pass
    
class UpdateListenerCanvas(UpdateListener, ABC):
    """ Same thing than the UpdateListener but for the update being 
        called in the canvas thread thanks to after. 
    """
    
    def __init__(self, canvas):
        self.__canvas = canvas
        
    def update(self, event):
        """ Redifinition of the update function so that it calls the 
            update function in the canvas thread thanks to after
        """
        self.__canvas.after(0, self.update_canvas, event)
        
    @abstractmethod
    def update_canvas(self, event):
        """ The update methode same as for the UpdateListener. Triggered
            when the support does so
        """
        pass
    
class UpdateSupport:
    """ This class is intended to allow for another class to have
        listeners. See the class above to understand the concept 
        of listeners. 
        
        The listener must add itself to the support class by using the
        addUpdateListener method.
        
        The user of the class can trigger everyone of its listeners
        by using the method action_listeners
    """
    
    def __init__(self):
        self.update_listeners = []
        
    def action_listeners(self, event):
        """ Actions the listeners registered by calling their update method
        
            @param event The event that is send to the listener 
                         (cf. UpdateEvent)
        """
        for listener in self.update_listeners:
            listener.update(event)
    
    def add_update_listener(self, update_listener):
        """ Allows for the listener to register to the class support which
            extended this class.
            
            @param update_listener The listener to be registered to this 
                                   support
        """
        self.update_listeners.append(update_listener)
        
    def remove_update_listener(self, update_listener):
        """ Allows for the listener to unregister to the class support which
            extended this class.
            
            @param update_listener The listener to be unregistered to this
                                   support
        """
        self.update_listeners.remove(update_listener)
        
class UpdateEvent:
    """ An event class to carry data when the update function of the listener is
        called.
        
        old is the former data
        
        new is the new data
        
    """
    
    def __init__(self, id, old, new):
        self.__id = id
        self.__old = old
        self.__new = new
        
    # Getters setters
    def get_id(self):
        return self.__id
    def get_old(self):
        return self.__old
    def get_new(self):
        return self.__new