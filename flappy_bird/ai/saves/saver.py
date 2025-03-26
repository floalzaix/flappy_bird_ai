from datetime import datetime

class Saver:
    """ Stores data into a file. Specifically designed for q matrices """
    
    def __init__(self, file_name, episode_counter_save):
        self.__file_name = file_name
        
        # Counters for saving
        self.__episode_counter_save = episode_counter_save
        self.__counter_save = 0
        
    def write_q_matrix(self, q, num_epdisodes_done, epsilon):
        """ Storres the q matrix for a certain number of episodes dones"""
        with open(self.__file_name, "w") as file:
            # Writting the date + the nb of done episodes
            file.write("Date : " + str(datetime.now()) + " \n")
            file.write("Number of episodes : " + str(num_epdisodes_done) + " \n")
            file.write("Epsilon : " + str(epsilon) + " \n")
            
            # Storring the q matrice
            for key, value in q.items():
                file.write(str(key) + "\t")
                file.write(str(value) + "\t\n")
                
            print("Matrix saved !!!")
                
    def read_q_matrix(self, default_epsilon):
        """ Reads the q matrix saved and returns it as a dict and 
            also epsilon and num_episodes """
        num_episodes = None
        epsilon = None
        d = {}
        with open(self.__file_name, "r") as file:
            # Skips the first line
            file.readline()
            
            # Loading num_episodes
            line = file.readline().split()
            if len(line) >= 5:
                num_episodes = int(line[4])
            else:
                num_episodes = 0
                
            # Loading epsilon
            line = file.readline().split()
            if len(line) >= 3:
                epsilon = float(line[2])
            else:
                epsilon = default_epsilon
            
            # Loading the matrix
            line = file.readline()
            while line:
                # Getting the matrix data
                items = line.split("\t")
                if items[0] != "" and items[1] != "":
                    d[eval(items[0])] = eval(items[1])
                    
                line = file.readline()
                
        return num_episodes, epsilon, d
    
    def save_data(self, q, num_episodes, epsilon):
        """ Saves periodicaly QAlgo.COUNTER_SAVE """
        if num_episodes % self.__episode_counter_save == 0 and self.__counter_save == 0:
            self.__counter_save = 1
            self.write_q_matrix(q, num_episodes, epsilon)
        elif num_episodes % self.__episode_counter_save == 1:
            self.__counter_save = 0