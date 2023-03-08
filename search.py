import os
from hillclimber import HILLCLIMBER
from parallelHillClimber import PARALLEL_HILLCLIMBER
import constants as c

# for i in range(5):
#     os.system('"C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" generate.py')
#     os.system('"C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" simulate.py')

# print("Constructing : PHC")
print("In Search calling PHC")
phc = PARALLEL_HILLCLIMBER(c.bodytype, c.numBots)
#
print("In search calling phc.Evolve: ")
phc.Evolve()
#
# phc.Show_Best()
