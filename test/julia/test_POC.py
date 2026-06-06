import os
import sys

# Retrieves the directory of the current script file
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(root_dir)

from lingua_franca.julia import *
print(jl.fibonacci(6))
