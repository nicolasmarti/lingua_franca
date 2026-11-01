import time
start_time = time.time()

from .POC import *

end_time = time.time()
print(f"rust __init__: {end_time - start_time}")
