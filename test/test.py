import os
import sys

# Retrieves the directory of the current script file
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(current_dir, "..", "..")
sys.path.append(root_dir)

import lingua_franca
for i in dir(lingua_franca):
    if "__" not in i:
        print("%s: %s" % (
            i, ", ".join([
                str(j)
                for j in dir(lingua_franca.__getattribute__(i))
                if not "_" in str(j)
            ])
        ))

from lingua_franca import *

# ocaml
print(ocaml.Int)

# rust
print(rust.fibonacci(50))

# julia
print(julia.fibonacci(6))
