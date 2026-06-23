import os
import sys

# Retrieves the directory of the current script file
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(current_dir, "..", "..")
sys.path.append(root_dir)

def mdir(o):
    return ", ".join([
        "%s: %s" % (
            str(i),
            str(type(o.__getattribute__))
        )
        for i in dir(o)
        if not "_" in str(i)
    ])    

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

ty = Type.TyTuple(
    [Type.TyVar("s1"),
     Type.TyVar("s2"),
     Type.TyList(Type.TyInt())
     ]
)
print(
    ty, Type.tysz(ty)
)

####

te = Term.TeTuple([
    Term.TeInt(9),
    Term.TeFloat(0.0),
    Term.TeList([Term.TeInt(6), Term.TeInt(8)])
])
te_ty = Term.type_infer(te)
print( te, te_ty, Type.tysz(te_ty) )

print("--------------")

# rust
print(rust.fibonacci(50))

# julia
print(julia.fibonacci(6))

#
my_tree = Node(5, Node(3, Empty(), Empty()), Empty())
print(tree_sum(my_tree))  # Output: 8

