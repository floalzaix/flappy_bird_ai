# AI Reinforcement training V2 on a Flappy bird

---

> The game 

--- 

The game is a MVC develped app. It includes the basics features : 
the bird, the pipes and the system.

*  **GameLoop** handles the main thread of the game logic by rolling the pipes actionning gravity and checking for collision error raised in the models
*  The **World** contains all the game features
*  **FlappyBird** is the main app
  
It also uses config file : config.json to configure the games parameters. Then, these
configs are imported by the config_handler.py in the targetted files

Finally, it relies on a helper UpdateHandler to make the link between the views and the models mostly. To know more
about the helper got to the file.

---

> The AI

--- 

Curently in develpment of the second version. First one, not available.