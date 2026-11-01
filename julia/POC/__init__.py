import time
start_time = time.time()

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

end_time = time.time()
print(f"Julia __init__: {end_time - start_time}")
    
