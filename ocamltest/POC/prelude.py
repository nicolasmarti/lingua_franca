
def pprint( *s ):
    import sys
    print( *s )
    sys.stdout.flush()

def import_ml( names, subfolders = [] ):
    
    import ocaml
    import os
    import time
    
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

    start_time = time.time()
    m = ocaml.compile( "\n".join(content) )
    end_time = time.time()

    #print(f"import_ml: {end_time - start_time}")
    
    return m
    
