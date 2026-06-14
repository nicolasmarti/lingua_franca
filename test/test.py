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
import ocaml
print(ocaml.Failure)
print(Type)

e = Test.TInt(8)
print(e, type(e))
print(e("doudou"))
try:
    #not working
    print(Test.eval(e))
except ocaml.Failure as ex:
    print(1, ex)
except Exception as ex:
    print(2, ex)
except:
    import traceback
    print(traceback.format_exc())
    

e2 = Test.TApp(Test.TApp(Test.TAdd,e), e)
print(e2, type(e2))
try:
    #not working
    print(Test.eval(e2))
except ocaml.Failure as ex:
    print(1, ex)
except Exception as ex:
    print(2, ex)
except:
    import traceback
    print(traceback.format_exc())

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

#
my_tree = Node(5, Node(3, Empty(), Empty()), Empty())
print(tree_sum(my_tree))  # Output: 8

