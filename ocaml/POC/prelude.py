
def pprint( *s ):
    import sys
    print( *s )
    sys.stdout.flush()

def import_ml( names, subfolders = [] ):
    
    import ocaml
    import os
    
    folders = os.path.normpath(__file__).split( os.sep )[:-1]
    
    content = []
    if isinstance( names, str ):
        names = [names]

    for name in names:
        f = open(
            os.path.join(
                *(["/"] + folders + subfolders + ["%s.ml" % name] )),
            "r"
        )
        content.append( f.read() )
        f.close()
        
    m = ocaml.compile( "\n".join(content) )
    
    return m
    
