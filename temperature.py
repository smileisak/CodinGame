# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys
NB_n = int(raw_input())
if NB_n == 0 :
    print 0
else:
    temperatures = map( lambda x: int(x), raw_input().split() )
    #print temperatures
    t1 = filter( lambda x : x >= 0,  temperatures )
    t2 = filter( lambda x : x < 0,  temperatures )
    v1 = min(t1) if len( t1 ) != 0 else None
    v2 = max(t2) if len( t2 ) != 0 else None
    if v1 is None:
        print( v2 )
    elif v2 is None:
        print( v1 )
    elif v1 <= abs( v2 ):
        print( v1 )
    else:
        print( v2 )
    

