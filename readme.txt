################### ABOUT THE PROJECT ###################################

This project is a modified version of the SVM (Support Vector Machine) algorithm. Three key aspects of the traditional algorithm have been altered here:
	-> The computations are now optimized to work in distributed environments (this code is built for Hadoop)
	-> SVMs can be built for multi-class datasets
	-> The algorithm has been modified to reduce the time to test new data points. The time for testing a new data point is more than halved as compared to any of the traditional multi-class SVM methods (one-vs-one and one-vs-all).
	-> The algorithm has also shown a marked increase in accuracy over the one-vs-one and one-vs-all multi-class SVM methods for non-skewed datasets. For skewed datasets, I'm working on a modification of the algorithm that will show accuracies comparable to the other two methods.



#################### NOTE : FILES AND DIRECTORIES ####################

All files except final_automate_iris.py and testing_automation_iris.py should be stored in a folder named 'SVM_iris'

------------------------------------------------**************-------------------------------------------



1) FILE LOCATIONS:
	-> The SVM_iris folder must be stored in the Home directory ('/home/aditi' in this case)
	-> final_automate_iris.py must be stored in the Hadoop directory ('/usr/local/hadoop' in this case)


-------------------------------------------------------------------***-------------------------------------

2) CHANGES TO BE MADE IN THE CODES:
	-> final_automate_iris.py
		- Change the paths to the directory where the SVM_iris folder is present. Places where a change is required have been indicated by comments
		- (In case of a multi-node cluster) - Change the hostname from 'localhost' to the name of the Master node. Places where a change is required have been indicated by comments.
		
	-> cases.py
		- Change the file path to the directory where the SVM_iris folder is present. Indicated by a comment.
		
------------------------------------------------------**************-----------------------------------------		

3) RUNNING THE CODE:
	-> Go to the Hadoop home directory ('/usr/local/hadoop' in this case)
	-> Run the script - ('python final_automate_iris.py')
	

------------------------------------------*****************----------------------------------------------
	
4) THE INDIVIDUAL CODES AND THEIR OUTPUTS:
	-> cases.py:
		- input: in the form of command line arguments. Number of classes followed by the class labels - ('python /home/aditi/SVM_iris/cases.py 3 1 2 3')
		- output: a file called cases.txt with the different combinations of classes.
		
	-> test.py:
		- 1st mapper for TRAINING - takes input as rows of data and computes a base64 encoded matrix with the feature set of each row
	-> test_reducer.py:
		- 1st reducer for TRAINING - takes input from the 1st mapper as base64 encoded matrices and outputs the combined SVM for each combination of class labels.
		
	-> svm_test.py:
		- 2nd mapper for TRAINING - takes input as rows of data and computes the confusion matrix for each combination of SVM labels. Outputs one row in the format 'true_positive false_positive false_negative true_negative' for each combination of class labels.
	-> svm_test_reducer.py:
		- 2nd reducer for TRAINING - takes input from the 2nd mapper and outputs the SVM with highest accuracy along with the corresponding class label. This is stored in the file '/usr/local/hadoop/final_result'
		
		
	-> iris_test.py:
		- mapper for TESTING - takes input as rows of data from the testing data and outputs the confusion matrix that was computed using the SVMs from '/usr/local/hadoop/final_result'
	-> iris_test_reducer.py:
		- reducer for TESTING - takes input from the mapper above and outputs the FINAL ACCURACY!
		
		
------------------------------------------*****************--------------------------------------------------

  
		
	
