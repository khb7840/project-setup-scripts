# python3 code
# Author: Hyunbin Kim

# import necessary libraries
import os
import datetime


class DirGenerator:
    def __init__(self):
        # Get timetag
        now = datetime.datetime.now()
        self.timetag = now.strftime("%YY%mm%dd_%HH%MM%SS")
        self.path = "./" + self.timetag + "/"
        pass

    def from_config(self, config_dict, verbose=True):
        self.path = config_dict["path"]

    def write(self, verbose=True):
        # make directory
        os.mkdir(path=self.path)
        if verbose == True:
            print("Successfully generated: " + self.path)

    def generate_n_dirs(self, prefix="./dir", n=10,
                        digits=2, base=0, verbose=True):
        # from zero to count-1
        for i in range(n):
            num = i + base
            dir_id = format(num, '0'+str(digits))
            dir_name = prefix + dir_id + "/"
            os.mkdir(dir_name)
            if verbose == True:
                print("Successfully generated: " + dir_name)


# make unmade directory in path
def make_basedir(path):
    basedir = os.path.dirname(path)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
