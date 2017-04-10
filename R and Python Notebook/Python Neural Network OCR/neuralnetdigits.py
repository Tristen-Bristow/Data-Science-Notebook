# Automatic Classification of Handwritten Digits
# Neural Networks for Optical Character Recognition
# Tristen Bristow
# 04/07/2017

from sklearn.preprocessing import Imputer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import pandas as pd

# Abstract
# This study concerns the development of an automatic classification of 
# handwritten digits by Multi-Layered Neural Network. The network a single 
# hidden layer. Optimal overall performance vs  is established empirically 
# for a variable number of hidden layer nodes, where the best network 
# architecture is evaluated for minimal complexity a maximum performance.



# Load Data

# each instance has 64 attributes, each of which can have 
# value of 0−16. The last entry on the dataframe row is 
# the class label, which is 0-9.

test_data = np.loadtxt('optdigits.tes', delimiter = ',')
train_data = np.loadtxt('optdigits.tra', delimiter = ',')

np.random.seed(1)
 
test_class = test_data[:,64]
train_class = train_data[:,64]

test_data = test_data[:,0:64]
train_data = train_data[:,0:64]

# Pre-processing Step: 
# Standardization of data. Parameters necessary for standardization
# are obtained from the training-set, which are used in training and 
# test set standardization. We consider each of the 64 attributes
# (x_i) of the character pattern a feature, and for each we transform
# (via standardization).
 
# Standardization formula:

# x_i' = (x_i - u_i) / s_i

# where u_i is the feature mean value, s_i is the feature standard
# variation, x_i is an input of index, i is the index of the input
# array ranging from 0 to 64.
  
# Condition All Data

u_i = train_data.mean(axis=0) 
s_i = train_data.std(axis=0) 

train_data = (train_data - u_i) / s_i
test_data = (test_data - u_i) / s_i


imp = Imputer(missing_values='NaN', strategy='mean', axis=0)

imp = imp.fit(train_data)
train_data = imp.transform(train_data)

imp = imp.fit(test_data)
test_data = imp.transform(test_data)

# Train classifier and run test

acc = []

# The classifier is a neural network with a single hidden layer of variable
# width. Out of sample classification accuracy is tested against various widths 
# of the hidden layer.

tot = len(train_class)
 
print("Width of Hidden Layer vs. Classification Accuracy(%)")

for width in range(1,8):
 
	mlp = MLPClassifier(hidden_layer_sizes = (width))
	mlp.fit(train_data, train_class)
	predictions = mlp.predict(train_data)

	te = 0
		
	for i in range(tot):

		if (predictions[i] == train_class[i]):
			te += 1

	ca = (te/tot)*100
	acc.append(ca)
	print(width, ca)

best_fit = max(acc)	
best_i = np.argmax(acc) + 1
print
print("Optimum Number of Hidden Nodes: ", best_i)
print("With classification accuracy:", best_fit)
print
plt.plot(acc)
plt.title("Number of Hidden Nodes Vs. Training Classification Accuracy")
plt.xlabel("Number of Neurons")
plt.ylabel("Recognition Accuracy")
plt.show()


tot = len(test_class)

print("Network performance on test set")
print(best_i, " nodes chosen:")
mlp = MLPClassifier(hidden_layer_sizes = (best_i))
mlp.fit(train_data,train_class)
predictions = mlp.predict(test_data)

te = 0

for i in range(tot):
	if (predictions[i] == test_class[i]):
		te += 1

ca = (te/tot)*100

print(ca,"% accuracy")