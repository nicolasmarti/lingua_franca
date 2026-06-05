from .load import *

class Ty(object):

    def __init__(self, o):
        self.__o = o
        
Int = Ty(m.Type.Int)
Float = Ty(m.Type.Float)
