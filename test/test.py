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
from lingua_franca.ocaml import *
print(Type)

e = Test.TInt(8)
print(e, type(e))
e2 = Test.TApp(Test.TApp(Test.TAdd,e), e)

match e:
    case Test.TInt(x):
        print(x)
    case Test.TAdd:
        print("Add")
    case Test.TApp(x, y):
        print("App")
    case _:
        print(e)
    
match e2:
    case Test.TInt(x):
        print(x)
    case Test.TAdd:
        print("Add")
    case Test.TApp(x, y):
        print("App")
    case _:
        print(e2)
    

# rust
print(rust.fibonacci(50))

# julia
print(julia.fibonacci(6))
