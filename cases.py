# -*- coding: cp1252 -*-
#önly error is code has to be changed a little for more no of classes i.e above 10
import math
import sys
#method to find out nCn/2 combintaions
def ncn(num):
    res=((math.factorial(num))/((math.factorial(num/2)) * (math.factorial(num-num/2))))
    return res
#for subtracting 2 lists
def sub_list(list1,list2):
    res=[]
    for i in list1:
        res.append(i)
    for i in list1:
        for j in list2:
            if i==j:
                res.remove(i)
    return res          
 
 
# ^^^^^^^^^^^^^^^^^ path change required here ^^^^^^^^^^^^^^^^^^^^^^^^                
cla_file = open("/home/aditi/SVM_iris/cases.txt","w")
print sys.argv
#this we should take input from keyboard here hard coded
#and creatng the all nCn/2 combinations and writing them in a file
no_of_cls=int(sys.argv[1])
count=0
fun=ncn(no_of_cls)
print fun
cla_range =[]
total=[]
end1=((no_of_cls+1)/2)-1
end2=1
for i in range(1,(no_of_cls+3)/2):
    cla_range.append(i)
for i in range(1,no_of_cls+1):
    total.append(i)    
n=no_of_cls/2
if(no_of_cls%2==0):
	for i in range(1,fun/2+1):
	    a=[]
	    for z in range(0,(no_of_cls+1)/2):
	        a.append(cla_range[z])
	    b= sub_list(total,a)
	    for k in range(0,(no_of_cls+1)/2):
	        cla_file.write(str(sys.argv[cla_range[k]+1])+",")
	    cla_file.write("\t")
	    for k in range(0,len(b)):
	        cla_file.write(str(sys.argv[b[k]+1])+",")
	    cla_file.write("\n")
	    if(cla_range[end1]<no_of_cls):
	        cla_range[end1]=cla_range[end1]+1
	    else:
	        for k in range(1,(no_of_cls+3)/2):
	            if(cla_range[end1-k]<(no_of_cls-k)):
	                cla_range[end1-k]=cla_range[end1-k]+1
	                break 
	        for r in range(end1-k+1,end1+1):
	            cla_range[r]=cla_range[r-1]+1	
                
    	count=count+1
else:
	for i in range(1,fun+1):
	    a=[]
	    for z in range(0,(no_of_cls+1)/2):
	        a.append(cla_range[z])
	    b= sub_list(total,a)
	    for k in range(0,(no_of_cls+1)/2):
	        cla_file.write(str(sys.argv[cla_range[k]+1])+",")
	    cla_file.write("\t")
	    for k in range(0,len(b)):
	        cla_file.write(str(sys.argv[b[k]+1])+",")
	    cla_file.write("\n")
	    if(cla_range[end1]<no_of_cls):
	        cla_range[end1]=cla_range[end1]+1

	    else:
	        for k in range(1,(no_of_cls+3)/2):
	            if(cla_range[end1-k]<(no_of_cls-k)):
	                cla_range[end1-k]=cla_range[end1-k]+1
	                break 
	        for r in range(end1-k+1,end1+1):
	            cla_range[r]=cla_range[r-1]+1	
                
    	count=count+1                
cla_file.close()
#here reading each combination from the file and seperating each class and sending the input file 


