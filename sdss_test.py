#!/usr/bin/env python

import sys
import base64
import cPickle as pickle
#from mrjob.job import MRJob
import numpy as np

def main():
	
	f = open('SVMvalues.txt', 'r')
	
	omatrixList = []
	gammaList =[]

	pos_class_list = []
	neg_class_list = []
	count =0
	O = 0
	data = f.readlines()
	
	tp=0
	tn=0
	fp=0
	fn=0
	

	for line in sys.stdin:	

	
		tp, tn, fp, fn = classify_recursive(data, 1, line, tp, tn, fp, fn)
	
		
	print "0", "$", tp,"$", fp,"$", fn,"$", tn
	
		
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
    
def get_svm(line):
	line = line.strip()
	svm = line.split('$')
	omega = svm[3:-1]
	omegalist=[]
	for o in omega:
		o=float(o)
		omegalist.append(o)
		
	O = np.matrix(np.reshape(np.array(omegalist),(1, len(omegalist))))
	
	gamma = svm[-1]
	gamma=float(gamma)
	return (O, gamma)
	
def get_class(line):
	line = line.strip()
	svm = line.split('$')
	
	pos_classes = svm[0].split(',')
	pos_class_list = pos_classes[2:]
	
	neg_classes = svm[1].split(',')
	neg_class_list = neg_classes[2:]
	return(pos_class_list, neg_class_list)
	
	
def confusion_matrix(classify, category, tp, tn, fp, fn):
	if(float(classify)>0 and category > 0):
		tp+=1
	if(float(classify)>0 and category < 0):
		fp+=1
	if(float(classify)<0 and category > 0):
		fn+=1
	if(float(classify)<0 and category < 0):
		tn+=1
	return (tp,tn,fp,fn)
	

def classify_recursive(data, i, line, tp, tn, fp, fn):
	pos_class_list,neg_class_list = get_class(data[i-1])
	category,features = transform_input(line ,pos_class_list,neg_class_list)
		
	num_training_features = len(features)
	
	A = np.matrix(np.reshape(np.array(features),(1, num_training_features)))
	
	O, gamma = get_svm(data[i-1])
	classify = A * O.T - gamma
	
	if(float(classify)>0):
		
		if(2*i <= len(data)):
			
			tp, tn, fp, fn = classify_recursive(data, 2*i, line, tp, tn, fp, fn)
			return (tp,tn,fp,fn)
			
		else:
			
			tp,tn,fp,fn = confusion_matrix(classify, category, tp, tn, fp, fn)
			return (tp,tn,fp,fn)
			
	if(float(classify)<0):	
		
		if(2*i+1 <=len(data)):
			
			tp, tn, fp, fn = classify_recursive(data, 2*i+1, line, tp, tn, fp, fn)
			return (tp,tn,fp,fn)
		else:
			
			tp,tn,fp,fn = confusion_matrix(classify, category, tp, tn, fp, fn)
			
			return (tp,tn,fp,fn)
		
	

		
		
main()
