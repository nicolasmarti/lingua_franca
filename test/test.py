import os
import sys
import time

n = 1000000000

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
from lingua_franca.ocamltest import Type, Term

print("\n\n*** DIR ***")
print("Full:", ", ".join([str(i) for i in dir(lingua_franca) if not "__" in i]))
print("ocaml:", ", ".join([str(i) for i in dir(lingua_franca.ocamltest) if not "__" in i]))
print("rust:", ", ".join([str(i) for i in dir(lingua_franca.rust) if not "__" in i]))
print("julia:", ", ".join([str(i) for i in dir(lingua_franca.julia) if not "__" in i]))

# ocaml
start_time = time.time()
print("\n\n#### Ocaml ####")
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

te = Term(
    Term.TeTuple([
        Term.TeInt(9),
        Term.TeFloat(0.0),
        Term.TeList([Term.TeInt(6), Term.TeInt(8)])
    ])
)
    
te_ty = Term.type_infer(te.te)
print( te, type(te) )
print( te_ty, type(te_ty) )
print( Type.tysz(te_ty) )
print(te + te)
end_time = time.time()
print(f"--- ocaml test: {end_time - start_time}")

print("#### Python ####")
start_time = time.time()
my_tree = Node(5, Node(3, Empty(), Empty()), Empty())
print(my_tree, tree_sum(my_tree))  # Output: 8
end_time = time.time()
print(f"--- python test2: {end_time - start_time}")

print("\n\n#### Fibonacci ####")

# rust
start_time = time.time()
start_time = time.time()
x = rust.fibonacci(n)
end_time = time.time()
print(f"--- rust: {end_time - start_time}")

start_time = time.time()
x = lingua_franca.ocamltest.fibonacci(n)
end_time = time.time()
print(f"--- ocaml: {end_time - start_time}")

start_time = time.time()
x = julia.fibonacci(n)
end_time = time.time()
print(f"--- julia[pre JIT]: {end_time - start_time}")

start_time = time.time()
x = julia.fibonacci(n)
end_time = time.time()
print(f"--- julia[post JIT]: {end_time - start_time}")

    # start_time = time.time()
    # x = fibonacci(n)
    # end_time = time.time()
    # print(f"--- python: {end_time - start_time}")

start_time = time.time()
x = fibonacci2(n)
end_time = time.time()
print(f"--- python2[pre JIT]: {end_time - start_time}")

start_time = time.time()
x = fibonacci2(n)
end_time = time.time()
print(f"--- python2[post JIT]: {end_time - start_time}")
