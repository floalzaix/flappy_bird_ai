import json
import os

_config_file = None

def get_config_param(header, param):
    """ Gets the parameter of the category selected which is from the
        config file config.json
        
        @param header The category of the param
        @param param  The param itself
        
        @return The value of the param
        
        @raise  FileNotFoundError If the file is not found
                KeyError If the parameter or category don't exist
    """
    global _config_file
    if _config_file == None:
        _config_file = _get_params_from_config_file()
        
    return _config_file[header][param]
    
def _get_params_from_config_file():
    """ Gets the table of the categories x params of the config json file
        
        @return The table of the categories x params
        
        @raise FileNotFoundError If the file is not found
    """
    
    script_dir = os.path.dirname(__file__)

    file_path = os.path.join(script_dir, "config.json")
    
    with open(file_path, "r") as file:
        config_file = json.load(file)
        
    return config_file