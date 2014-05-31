#!/usr/bin/env python

import base64
import cPickle as pickle
#from mrjob.job import MRJob
import numpy as np
import sys


def main():
	for line in sys.stdin:
		line_in = line.strip()
		f=open('cases.txt','r')
		count=0
		for line in f:
			if (line != "\n"):
				count=count+1
        			line_case = line.rstrip('\n')
        			class_t = line_case.split('\t',1)
				class_t[0]=class_t[0].rstrip(',')
        			class_t[1]=class_t[1].rstrip(',')
       				#print class_t
        			class_1 = str(class_t[0]).split(',',1000)
        			class_2 = str(class_t[1]).split(',',1000)			
				#print "line_in",line_in
				flag = check_if_belongs_to_category(line_in, class_1, class_2)
    				if flag>0:
    					#print (" computed, ", flag)
    					category,features = transform_input(line_in,class_1,class_2)
					mapper(count,category,features)
				else: 
					#print ("continued, ", flag)
					continue
		

def check_if_belongs_to_category(line, neg, pos):
	array = line.split(',')
	categ = array[-1].strip()
	category = map_category(categ)
	if category in pos or category in neg:
		#print category
		return category
	else:
		#print 0
		return 0



def map_category(category):
	if (category == 'Iris-setosa'):
		return '1'
	elif (category == 'Iris-versicolor'):
		return '2'
	else:
		return '3'


def numerify_feature(feature):
    if feature == '?':
        feature = 0.0
    return float(feature)

def extract_features(array):
    features = array[0:-1]
    return [numerify_feature(f) for f in features]

def extract_category(array, neg, pos):
    categ = array[-1].strip()
    category = map_category(categ)
    if category in neg: 
	return -1.0 
    elif category in pos:  
	return 1.0
    else: 
	return 0


def transform_input(value,pos,neg):
    array = value.split(',')
    features = extract_features(array)
    category = extract_category(array, neg, pos)
    return(category, features)

def mapper(key, category, value):
    num_training_features = len(value)
    #print num_training_features
    A = np.matrix(np.reshape(np.array(value),(1, num_training_features)))
    #print category
    D = np.diag([category])
    e = np.matrix(np.ones(len(A)).reshape(len(A), 1))
    E = np.matrix(np.append(A, -e, axis = 1))

    value = base64.b64encode(pickle.dumps((E.T*E, E.T*D*e)))
    #print("outputkey", value)
    print '%d\t%s' % (key,value)
   

main()


