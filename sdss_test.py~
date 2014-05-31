#!/usr/bin/env python

import sys
import base64
import cPickle as pickle
#from mrjob.job import MRJob
import numpy as np

def main():
	#f1 = open("/home/aditi/Downloads/SVM_MR/Snabler-master/psvm/testdata.txt")
	f = open('SVMvalues.txt', 'r')
	#f2 = open('cases', 'r')
	omatrixList = []
	gammaList =[]

	pos_class_list = []
	neg_class_list = []
	count =0
	O = 0
	data = f.readlines()
	#print data
	#cases = f2.readlines()
	tp=0
	tn=0
	fp=0
	fn=0
	
	'''	
	for line in f:
		#current_case = cases[count]
		
		
		print data
		
		count+=1
		line = line.strip()
		svm = line.split()
		#print svm
		
		pos_classes = svm[0].split(',')
		pos_class_list = pos_classes[2:]
		
		neg_classes = svm[1].split(',')
		neg_class_list = neg_classes[2:]
		
		
		current_case = current_case.strip()
		
		class_t = current_case.split('\t',1)
		class_t[0]=class_t[0].rstrip(',')
        	class_t[1]=class_t[1].rstrip(',')
       		#print class_t
        	class_1 = str(class_t[0]).split(',',1000)
        	class_2 = str(class_t[1]).split(',',1000)			
		#print "line_in",line_in
		#pos_class_list.append(class_1)
		#neg_class_list.append(class_2)
		
		
		omega = svm[3:-1]
		omegalist=[]
		for o in omega:
			o=float(o)
			omegalist.append(o)
			#print "omegalist ", omegalist
	
		O = np.matrix(np.reshape(np.array(omegalist),(1, len(omegalist))))
		#print "Omega", O
		gamma = svm[-1]
		gamma=float(gamma)
		tp=0
		tn=0
		fp=0
		fn=0
		#G = np.matrix(np.reshape(np.array(gamma),(1, len(gamma))))
	
	'''
	for line in sys.stdin:	


		#print "A", A
		#print "THIS IS IN MAIN", line
		tp, tn, fp, fn = classify_recursive(data, 1, line, tp, tn, fp, fn)
		#print "THIS IS IN MAIN", tp, tn, fp, fn
		#print len(data)

		
	#print classifyList	
	#print '0',"\t", pos_class_list,"\t", neg_class_list,"\t", tp,"\t", fp,"\t", fn,"\t", tn, "\t", str(O.tolist()), "\t", str(gamma)
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
		#print "omegalist ", omegalist
	O = np.matrix(np.reshape(np.array(omegalist),(1, len(omegalist))))
	#print "Omega", O
	gamma = svm[-1]
	gamma=float(gamma)
	return (O, gamma)
	
def get_class(line):
	line = line.strip()
	svm = line.split('$')
	#print svm
	
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
	#print "category", category
	#print "pos_class_list[i]", pos_class_list
	#print "neg_class_list[i]", neg_class_list
	
	num_training_features = len(features)
	#print num_training_features
	A = np.matrix(np.reshape(np.array(features),(1, num_training_features)))
	
	
	O, gamma = get_svm(data[i-1])
	#print O
	#print gamma
	#print A
	classify = A * O.T - gamma
	#print "classify, categ, i, len(data)", classify, category, i, len(data)
	
	if(float(classify)>0):
		#print "here now"
		if(2*i <= len(data)):
			#print 2*i, data[2*i-1]
			tp, tn, fp, fn = classify_recursive(data, 2*i, line, tp, tn, fp, fn)
			return (tp,tn,fp,fn)
			
		else:
			#print "final class, categ", classify, category
			tp,tn,fp,fn = confusion_matrix(classify, category, tp, tn, fp, fn)
			return (tp,tn,fp,fn)
			
	if(float(classify)<0):	
		#print "here 2 now"
		if(2*i+1 <=len(data)):
			#print 2*i+1, data[2*i+1-1]
			tp, tn, fp, fn = classify_recursive(data, 2*i+1, line, tp, tn, fp, fn)
			return (tp,tn,fp,fn)
		else:
			#print "final class, categ", classify, category
			tp,tn,fp,fn = confusion_matrix(classify, category, tp, tn, fp, fn)
			#print tp,tn,fp,fn
			return (tp,tn,fp,fn)
		
	

		
		
main()
