import numpy as np
import re
from modshogun import *
def classifier():
	
	f1=open('combined_feature_vector.txt','r')
	f2=open('combined_label_vector.txt','r')
	feature_data=np.load(f1)
	label_data=np.load(f2)
	train_data=RealFeatures(feature_data)
	train_labels=MulticlassLabels(label_data)
	width=2.1
	kernel=GaussianKernel(train_data,train_data,width)
	C=1
	svm=MulticlassLibSVM(C, kernel, train_labels)
	epsilon=1e-5
	svm.set_epsilon(epsilon)
	svm.train(train_data)
	f3=SerializableHdf5File("libsvm_classifier_with_gaussain_kernel_width2_1.h5", "w")
	svm.save_serializable(f3)
	
	print 'svm is ',svm, ' and strategy is ', svm.get_multiclass_strategy(),' and support vectors are ',svm.get_num_machines()
	
if __name__=='__main__':
	print('MulticlassLibSVM')
	classifier()
