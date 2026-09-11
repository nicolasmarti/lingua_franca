from .load import *

class Type(m.Type, m.Type.T):
    pass

class Term(m.Term, m.Term.T):

    def __init__(self, te, ty = None):
        self.te = te
        if ty is None:
            self.ty = Term.type_infer(te)
        else:
            self.ty = ty

    def __str__(self):
        return "%s::%s" % (str(self.te), str(self.ty))
            
    def __add__(self, o):
        return self
