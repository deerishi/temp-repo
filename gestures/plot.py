from matplotlib.pyplot import * 
from numpy import *
from modshogun import * 


def main():
	f1=open(r'circle counterclockwise/train_cc_label1.txt','r')
	f2=open(r'swipe_left/train_swipe_left_label_minus_1.txt','r')
	fl1=open(r'circle counterclockwise/label_1cc.txt','r')
	fl2=open(r'swipe_left/label_minus_1_swipe_left.txt','r')
	f3=open(r'swipe_right/train_swipe_right_label_minus_1.txt','r')
	data3=load(f3)
	len3=len(data3[0])
	data3_train=data3[:,0:len3/2]
	data3_test=data3[:,len3/2:]
	data1=load(f1)
	data_minus1=load(f2)
	
	label1=load(fl1)
	label_minus1=load(fl2)
	len1=len(data1[0])
	len2=len(data_minus1[0])
	test_set1=data1[:,len1/2:]
	test_set_minus1=data_minus1[:,len2/2:]
	test_l1=label1[len1/2:]
	test_l_minus1=label_minus1[len2/2:]
	test_set=RealFeatures(hstack((test_set1,test_set_minus1)))  #test set data
	test_label=BinaryLabels(hstack((test_l1,test_l_minus1))) #test labels
	data1=data1[:,0:len1/2]
	data_minus1=data_minus1[:,0:len2/2]
	label1=label1[0:len1/2]
	label_minus1=label_minus1[0:len2/2]
	label=hstack((label1,label_minus1))
	data=hstack((data1,data_minus1))
	print 'the length of data is ',len(data[0]),' and the length of label is  ', len(label)
	f,axes=subplots(2,2)
	axes[0,0].plot(data1[0],data1[1],'*')
	axes[0,0].plot(data3_train[0],data3_train[1],'^')
	axes[0,0].plot(data_minus1[0],data_minus1[1],'x')
	axes[0,0].set_ylabel('Sum of means')
	axes[0,0].set_xlabel('length of dataset')
	axes[0,0].set_title('Training dataset with plot')
	#show()
	gray()

	#show()
	C=1
	epsilon=1e-3
	feats_train=RealFeatures(data)
	labels=BinaryLabels(label)
	svm=LibLinear(C,feats_train,labels)
	svm.set_liblinear_solver_type(L2R_L2LOSS_SVC)
	svm.set_epsilon(epsilon)
	svm.train()
	f3=SerializableHdf5File("liblinear_svm_classifier_with_C_1.h5", "w")
	svm.save_serializable(f3)
	w=svm.get_w()
	b=svm.get_bias()
	print 'w is ',(w)
	x1=linspace(20,40,100)
	x2=-(((w[0])*x1 + b )/w[1]) 
	axes[0,1].scatter(data[0],data[1],c=label)
	axes[0,1].set_ylabel('Sum of means')
	axes[0,1].set_xlabel('length of dataset')
	axes[0,1].set_title('Training dataset with scatter and separating hyperplane with c=1')
	axes[0,1].plot(x1,x2,linewidth=2)
	show()
	predictions=svm.apply(test_set)
	#metric
	evaluator=ROCEvaluation()
	evaluator.evaluate(predictions,test_label)
	print 'the auc is ', evaluator.get_auROC()#,' and ',evaluator.get_ROC()
	print 'the pridicted labels are ', predictions.get_labels()
	print 'the test labels are ',test_label.get_labels()
		
	
	
	
if __name__=='__main__':
	main()
