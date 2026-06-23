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

from lingua_franca import *

# ocaml
print("#### Ocaml ####")
from lingua_franca.ocaml import *
import ocaml
print("Type:", ", ".join([str(i) for i in dir(Type) if not "__" in i]))
print("Term:", ", ".join([str(i) for i in dir(Term) if not "__" in i]))

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

# rust
print("#### Rust ####")
print(rust.fibonacci(50))

# julia
print("#### Julia ####")
print(julia.fibonacci(6))

#
my_tree = Node(5, Node(3, Empty(), Empty()), Empty())
print(tree_sum(my_tree))  # Output: 8

