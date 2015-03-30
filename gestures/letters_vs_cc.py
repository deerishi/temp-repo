import numpy as np
import re
from modshogun import RealFeatures,BinaryLabels,LibLinear,ROCEvaluation,AccuracyMeasure,SerializableHdf5File

from matplotlib.pylab import *

from mpl_toolkits.mplot3d import Axes3D

def main():
	fright=open(r'circle counterclockwise/train_cc_10_dim.txt','r')
	fleft=open(r'letters/Z/train_Z_10_dim.txt','r')
	data_right=np.load(fleft)
	data_left=np.load(fright)
	lenr=len(data_right[0])
	lenl=len(data_left[0])
	dim=10
	endr=int(0.9*lenr)
	endl=int(0.9*lenl)
	data_right_train=data_right[:,0:endr]
	data_left_train=data_left[:,0:endl]
	data_right_test=data_right[:,endr:]
	data_left_test=data_left[:,endl:]
	
	len_right_train=len(data_right_train[0])
	len_left_train=len(data_left_train[0])
	len_right_test=len(data_right_test[0])
	len_left_test=len(data_left_test[0])
	
	label_right_train=np.ones(len_right_train)
	label_right_test=np.ones(len_right_test)
	
	label_left_train=-1*np.ones(len_left_train)
	label_left_test=-1*np.ones(len_left_test)
	
	C=10
	
	train_dataset=np.hstack((data_right_train,data_left_train))
	normalization_mean=[]
	normalization_std=[]
	
	for i in range(0,dim):
		mean1=np.mean(train_dataset[i])
		std1=np.std(train_dataset[i])
		train_dataset[i]=(train_dataset[i]-mean1)/std1
		normalization_mean.append(mean1)
		normalization_std.append(std1)
	feats_train=RealFeatures(train_dataset)
	f,axes=subplots(2,2)
	fig = figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(data_right_train[0],data_right_train[1],data_right_train[2],c='r')
	ax.scatter(data_left_train[0],data_left_train[1],data_left_train[2],c='b')
	ax.set_xlabel('STD X')
	ax.set_ylabel('STD Y')
	ax.set_zlabel('STD Z')
	ax.set_title('3D PLOT OF STD')
	axes[0,0].plot(data_right_train[0],data_right_train[1],'*')
	axes[0,0].plot(data_left_train[0],data_left_train[1],'x')
	axes[0,0].set_xlabel('STDX')
	axes[0,0].set_ylabel('std y')
	axes[0,0].set_title('STDX VS stdy')
	axes[0,1].plot(data_right_train[1],data_right_train[2],'*')
	axes[0,1].plot(data_left_train[1],data_left_train[2],'x')
	axes[0,1].set_xlabel('std Y')
	axes[0,1].set_ylabel('std Z')
	axes[0,1].set_title('stdY  VS stdZ')
	axes[1,0].plot(data_right_train[0],data_right_train[2],'*')
	axes[1,0].plot(data_left_train[0],data_left_train[2],'x')
	axes[1,0].set_xlabel('std X')
	axes[1,0].set_ylabel('std z')
	axes[1,0].set_title('std X VS stdz')
	show()
	train_labels=np.hstack((label_right_train,label_left_train))
	test_dataset=np.hstack((data_right_test,data_left_test))
	normalization_file=open('normalization_parameters_letters_vs_cc.txt','w')
	norm_params=[normalization_mean,normalization_std]
	norm_params=np.asarray(norm_params)
	np.save(normalization_file,norm_params)
	
	for i in range(0,dim):
		test_dataset[i]=(test_dataset[i]-normalization_mean[i])/normalization_std[i]
	
	labels_train=BinaryLabels(train_labels)
	
	
	print 'the length of test_dataset is ',len(test_dataset[0])
	feats_test=RealFeatures(test_dataset)
	
	test_labels=np.hstack((label_right_test,label_left_test))
	print 'the length is test_labels is ',len(test_labels)
	labels_test=BinaryLabels(test_labels)
	
	svm=LibLinear(C,feats_train,labels_train)
	epsilon=1e-3
	svm.set_epsilon(epsilon)
	svm.train()
	predictions=svm.apply(feats_test)
	predictions_on_train=svm.apply(feats_train)
	evaluator1=ROCEvaluation()
	evaluator2=AccuracyMeasure()
	
	evaluator1.evaluate(predictions_on_train,labels_train)
	evaluator2.evaluate(predictions,labels_test)
	file_name="letters_vs_cc/ZLabel1accuracy="+ str(evaluator2.get_accuracy()) + " liblinear_cc_vs_Z_svm_classifier_with_C_10_and_normalized.h5"
	
	f3=SerializableHdf5File(file_name, "w")
	svm.save_serializable(f3)
	p_test=predictions.get_labels()
	for i in range(0,len(test_labels)):
		print 'predicted : ',p_test[i] ,' and actual ',test_labels[i] 
	print 'the Area under the curve is ',evaluator1.get_auROC()
	print 'the accuracy is ',evaluator2.get_accuracy()*100
	evaluator1.evaluate(predictions,labels_test)
	print 'the auc for test set is  ',evaluator1.get_auROC()
if __name__=='__main__':
	main()
	
	
