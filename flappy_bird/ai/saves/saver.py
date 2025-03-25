from datetime import date

class Saver:
    """ Stores data into a file. Specifically designed for q matrices """
    
    def __init__(self, file_name):
        self.__file_name = file_name
        
    def write_q_matrix(self, q, nb_epdisodes_done):
        """ Storres the q matrix for a certain number of episodes dones"""
        with open(self.__file_name, "w") as file:
            # Writting the date + the nb of done episodes
            file.write("Date : " + str(date.today()) + "\n")
            file.write("Number of episodes : " + str(nb_epdisodes_done) + "\n")
            
            # Storring the q matrice
            for key, value in q.items:
                file.write(str(key) + "\t")
                file.write(str(value) + "\n")
                
    def read_q_matrix(self):
        """ Reads the q matrix saved and returns it as a dict """
        d = {}
        with open(self.__file_name, "r") as file:
            # Skips the first two lines
            line = file.readline()
            file.readline()
            
            while line:
                line = file.readline()
                
                # Getting the matrix data
                items = line.split("\n")
                d[items[0]] = items[1]
                
        return d