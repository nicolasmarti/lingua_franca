import time
start_time = time.time()

__all__ = [
    'Type',
    'Term',
    'fibonacci'
]

from .TypeTerm import *

m = import_ml([
    "fibonacci", 
], ["src"])

fibonacci = m.fibonacci

end_time = time.time()
print(f"ocaml __init__: {end_time - start_time}")
