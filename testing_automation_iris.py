import os


########################## first time run  ##########################################

print ("*** ACCURACY CALCULATION ON TESTDATA STARTING . . . ")

os.system("hadoop fs -rmr /user/hduser/final_result_for_testing.txt")
os.system("hadoop fs -copyFromLocal final_result /user/hduser/final_result_for_testing.txt")

print ("### TRAINING OUTPUT COPIED")

os.system("hadoop fs -rmr /user/hduser/iris_testing.data")
os.system("hadoop fs -copyFromLocal /home/aditi/SVM_iris/iris_testing2.data /user/hduser/iris_testing.data")

print('************TESTING DATA COPIED***********')

#copying cases and data file to hdfs

print ("*** removing previous output directories")

os.system("hadoop fs -rmr /user/hduser/testing_acc")


print ("### TESTING RUNNING . . .")

os.system("bin/hadoop jar contrib/streaming/hadoop-*streaming*.jar -file /home/aditi/SVM_iris/iris_test.py    -mapper /home/aditi/SVM_iris/iris_test.py -file /home/aditi/SVM_iris/iris_test_reducer.py    -reducer /home/aditi/SVM_iris/iris_test_reducer.py -cacheFile 'hdfs://localhost:54310/user/hduser/final_result_for_testing.txt#SVMvalues.txt'  -input /user/hduser/iris_testing.data -output /user/hduser/testing_acc")
#output will be /user/hduser/multi_output/part-00000
#os.system("hadoop fs -ls /user/hduser")

print ("-----------OUR FINAL ACCURACY!!!------------")
os.system("hadoop fs -cat /user/hduser/testing_acc/part-00000")


