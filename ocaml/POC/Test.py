from .load import *


class Test(m.Test):

    # @staticmethod
    # def TInt(x: int) -> Self:
    #     return Self(


    def __call__(self, args, **kargs):
            print("app", self, str(args), str(kargs))
            
    pass

print("###########################")
d_ = dir(m.Test)
print( d_, type(d_))
for x in d_:
    print(x, m.Test.__getattribute__(m.Test, x))
print("###########################")

for subclass in [
        "tterm", "TAdd", "TApp", "TInt"
]:    
    m.Test.TInt.__getattribute__(m.Test, subclass).__call__ = Test.__call__
            
