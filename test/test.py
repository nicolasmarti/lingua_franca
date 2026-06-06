import os
import sys

# Retrieves the directory of the current script file
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(current_dir, "..", "..")
sys.path.append(root_dir)

import lingua_franca
for i in dir(lingua_franca):
    if "__" not in i:
        print(i)
