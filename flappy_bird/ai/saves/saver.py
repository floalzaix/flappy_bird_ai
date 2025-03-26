from datetime import datetime

class Saver:
    """ Stores data into a file. Specifically designed for q matrices """
    
    def __init__(self, file_name, episode_counter_save):
        self.__file_name = file_name
        
        # Counters for saving
        self.__episode_counter_save = episode_counter_save
        self.__counter_save = 0
        
    def write_q_matrix(self, q, num_epdisodes_done, alpha, epsilon, get_stats):
        """ Storres the q matrix for a certain number of episodes dones"""
        with open(self.__file_name, "w") as file:
            stats, max_score, max_episode = get_stats()
            
            # Writting the date + the nb of done episodes
            file.write("Date : " + str(datetime.now()) + " \n")
            file.write("Number of episodes : " + str(num_epdisodes_done) + " \n")
            file.write("Alpha : " + str(alpha) + " \n")
            file.write("Epsilon : " + str(epsilon) + " \n")
            file.write("Pipe dist            => mean : " + str(stats[0][0]) + "\t min : " + str(stats[0][1]) + "\t max : " + str(stats[0][2]) + "\t std : " + str(stats[0][3]) + "\n")
            file.write("Bird y               => mean : " + str(stats[1][0]) + "\t min : " + str(stats[1][1]) + "\t max : " + str(stats[1][2]) + "\t std : " + str(stats[1][3]) + "\n")
            file.write("Bird y velocity      => mean : " + str(stats[2][0]) + "\t min : " + str(stats[2][1]) + "\t max : " + str(stats[2][2]) + "\t std : " + str(stats[2][3]) + "\n")
            file.write("Score stats          => mean : " + str(stats[3][0]) + "\t min : " + str(stats[3][1]) + "\t max : " + str(stats[3][2]) + "\t std : " + str(stats[3][3]) + "\n")
            file.write("MAX SCORE : " + str(max_score) + "\t(episode : " + str(max_episode) + ") \n")
            
            # Storring the q matrice
            for key, value in q.items():
                file.write(str(key) + "\t")
                file.write(str(value) + "\t\n")
                
            print("Matrix saved !!!")
                
    def read_q_matrix(self):
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
                
            # Loading alpha
            line = file.readline().split()
            if len(line) >= 3:
                alpha = float(line[2])
                
            # Loading epsilon
            line = file.readline().split()
            if len(line) >= 3:
                epsilon = float(line[2])
                
            # Skipping stats lines
            file.readline()
            file.readline()
            file.readline()
            file.readline()
            file.readline()
            
            # Loading the matrix
            line = file.readline()
            while line:
                # Getting the matrix data
                items = line.split("\t")
                if items[0] != "" and items[1] != "":
                    d[eval(items[0])] = eval(items[1])
                    
                line = file.readline()
                
        return num_episodes, alpha, epsilon, d
    
    def save_data(self, q, num_episodes, alpha, epsilon, get_stats):
        """ Saves periodicaly QAlgo.COUNTER_SAVE """
        if num_episodes % self.__episode_counter_save == 0 and self.__counter_save == 0:
            self.__counter_save = 1
            self.write_q_matrix(q, num_episodes, alpha, epsilon, get_stats)
        elif num_episodes % self.__episode_counter_save == 1:
            self.__counter_save = 0