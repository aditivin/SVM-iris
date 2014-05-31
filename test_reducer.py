#!/usr/bin/env python

import sys
import base64
import cPickle as pickle
#from mrjob.job import MRJob
import numpy as np



def main():

    sum_ETE = None
    sum_ETDe = None

    old_key = 1
    for line in sys.stdin:
        line = line.strip()
        #print line
        key, values = line.split('\t', 1)
        key = int(key)
        
        if key == old_key:
        	key,result, sum_ETE, sum_ETDe = reducer(key,values, sum_ETE, sum_ETDe)
        	old_key = key
        else:
        	print "$".join(result.split(','))
                sum_ETE = None
                sum_ETDe = None
        	key,result, sum_ETE, sum_ETDe = reducer(key,values, sum_ETE, sum_ETDe)
        	old_key = key
    print "$".join(result.split(','))	
        	

def reducer(key, values, sum_ETE, sum_ETDe):
    mu = 0.1
    #print values
    ETE, ETDe = pickle.loads(base64.b64decode(values))

    if sum_ETE == None:
        sum_ETE = np.matrix(np.eye(ETE.shape[1])/mu)
    sum_ETE += ETE
            
    if sum_ETDe == None:
        sum_ETDe = ETDe
    else:
        sum_ETDe += ETDe

    #print "sum_ETE",sum_ETE
    #print "sum_ETDe",sum_ETDe
    #print  "sum_ETE.I",sum_ETE.I 
    result = sum_ETE.I * sum_ETDe
    #print "result",result
    return(key, str(result.tolist()), sum_ETE, sum_ETDe)
    
main()
