__all__ = [
    "fibonacci"
]
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

from juliacall import Main as jl
jl.include(
    os.path.join(current_dir, "fibonacci.jl")
)

for x in ["fibonacci"]:
    locals()[x] = jl.seval(x)
    
