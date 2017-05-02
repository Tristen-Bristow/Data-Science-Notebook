# Prediction of Heating and Cooling Loads in Building Design
# Tristen Bristow
# capitolmotion@gmail.com
# 05/01/2017

# Data download link:
# http://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx
# Downloaded on 4/30/2017


# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# Load Data
np.random.seed(1)

wb = pd.read_excel("ENB2012_data.xlsx")

# Data Cleaning

# X1 Relative Compactness
# X2 Surface Area
# X3 Wall Area
# X4 Roof Area
# X5 Overall Height
# X6 Orientation
# X7 Glazing Area
# X8 Glazing Area Distribution
# y1 Heating Load
# y2 Cooling Load


wb.columns = ['Compactness', 'Surface', 'Wall', 'Roof', 'Height', 'Orientation', 'Glazing', 'Glazing Dist.', 'Heating', 'Cooling']

# Summary Statistics
print(wb.describe())

# Check for NA/missing values
print(wb.isnull().any())


# Check output variables for normality

plt.suptitle('Heating and Cooling Load Distributions (Watts per Squre Meter)', fontsize=18)
plt.hist(wb['Heating'], 50, normed = True)
plt.hist(wb['Cooling'], 50, normed = True)
plt.ylabel('Frequency')
plt.xlabel('Load Amount')
plt.show()

# Output histograms 'Heating' and 'Cooling' distributions both show 
# non-normality

plt.figure(figsize=(8, 7))
plt.suptitle('All Factors Vs. Heating Load (Watts per Square-Meter)', fontsize=18)
plt.subplot(2, 4, 1).set_title('Compactness')
plt.xticks(np.arange(min(wb['Compactness']), max(wb['Compactness']), .3))
plt.plot(wb['Compactness'], wb['Heating'], "o")
plt.subplot(2, 4, 2).set_title('Surface')
#50 - 80
plt.xticks(np.arange(min(wb['Surface']), max(wb['Surface']), 150))
plt.plot(wb['Surface'],wb['Heating'], "o")
plt.subplot(2, 4, 3).set_title('Wall')
#240-420
plt.xticks(np.arange(min(wb['Wall']), max(wb['Wall']), 100))
plt.plot(wb['Wall'],wb['Heating'], "o")
plt.subplot(2, 4, 4).set_title('Roof')
#100-240
plt.xticks(np.arange(min(wb['Roof']), max(wb['Roof']), 70))
plt.plot(wb['Roof'],wb['Heating'], "o")
plt.subplot(2, 4, 5).set_title('Height')
#3.5-7
plt.xticks(np.arange(min(wb['Height']), max(wb['Height']), 2))
plt.plot(wb['Height'],wb['Heating'], "o")
plt.subplot(2, 4, 6).set_title('Orientation')
#2-5
plt.xticks(np.arange(min(wb['Orientation']), max(wb['Orientation']), 1))
plt.plot(wb['Orientation'],wb['Heating'],"o")
plt.subplot(2, 4, 7).set_title('Glazing')
#0-.45
plt.xticks(np.arange(min(wb['Glazing']), max(wb['Glazing']), .1))
plt.plot(wb['Glazing'],wb['Heating'],"o")
plt.subplot(2, 4, 8).set_title('Glazing Dist.')
#0-5
plt.plot(wb['Glazing Dist.'],wb['Heating'],"o")

plt.show()


plt.figure(figsize=(8, 7))
plt.suptitle('All Factors Vs. Cooling Load (Watts per Square Meter)', fontsize=18)
plt.subplot(2, 4, 1).set_title('Compactness')
plt.xticks(np.arange(min(wb['Compactness']), max(wb['Compactness']), .3))
plt.plot(wb['Compactness'], wb['Cooling'], "o")
plt.subplot(2, 4, 2).set_title('Surface')
#50 - 80
plt.xticks(np.arange(min(wb['Surface']), max(wb['Surface']), 150))
plt.plot(wb['Surface'],wb['Cooling'], "o")
plt.subplot(2, 4, 3).set_title('Wall')
#240-420
plt.xticks(np.arange(min(wb['Wall']), max(wb['Wall']), 100))
plt.plot(wb['Wall'],wb['Cooling'], "o")
plt.subplot(2, 4, 4).set_title('Roof')
#100-240
plt.xticks(np.arange(min(wb['Roof']), max(wb['Roof']), 70))
plt.plot(wb['Roof'],wb['Cooling'], "o")
plt.subplot(2, 4, 5).set_title('Height')
#3.5-7
plt.xticks(np.arange(min(wb['Height']), max(wb['Height']), 2))
plt.plot(wb['Height'],wb['Cooling'], "o")
plt.subplot(2, 4, 6).set_title('Orientation')
#2-5
plt.xticks(np.arange(min(wb['Orientation']), max(wb['Orientation']), 1))
plt.plot(wb['Orientation'],wb['Cooling'], "o")
plt.subplot(2, 4, 7).set_title('Glazing')
#0-.45
plt.xticks(np.arange(min(wb['Glazing']), max(wb['Glazing']), .1))
plt.plot(wb['Glazing'],wb['Cooling'], "o")
plt.subplot(2, 4, 8).set_title('Glazing Dist.')
#0-5
plt.plot(wb['Glazing Dist.'],wb['Cooling'], "o")

plt.show()

# Scatter plots of independantly varying factors vs 
# measured Heating and Cooling Loads indicates a varying dependence
# in the latter. The relationships appear to, in instances, be at
# times linear, and others non-linear. In certain relationships (compactness,
# surface, and wall, verses roof and heating and cooling loads), it appears
# that a discontinuous separation can be observed in the dynamics, 
# suggesting the existence of underlying independent-factor threshold-levels that define
# multliple dynamic modes in the system. The modes separated, examined unto themselves,
# appear to generally show linear relationships with heating and cooling load outputs. 
# As these discontinuities appear to manefest at specific threshold levels for each
# factor, where relative linearity and simplicity is otherwise observed, it is clear
# that a random forests is a well-advised approach, as the system could possibly 
# be easily described by a machine-learning method that can maximally utilize information from these 
# discontinuities, and encompass the releative simplicity of dynamic expression between 
# them (owing to linearity and their limited number of discrete states, in addition to
# a limited number of potentially relevant factors to be considered).

# Random Forest modeling
# As the relevant aspects of cross-validation are inherent in the Random Forest algorithnm 
# train and test splits are un-necessary to produce an out-of-sample estimate, as well as any
# externally applied cross-validation. Though this is the case, it appears to be a common
# practice to demonstrate random-forest performance via a train-test splitting, and thus it is 
# applied here to further elaborate out-of-sample performance. 

# need to split data into input verses target values

wb_train = wb[ : int(.75 * len(wb))]
wb_test = wb[int(.75 * len(wb)) : ]

d_ind = wb_train.iloc[:,:8]
d_target = wb_train.iloc[:,8:10]

t_ind = wb_test.iloc[:,:8]
t_target = wb_test.iloc[:,8:10]


mdl = RandomForestRegressor(n_estimators = 8,
							max_features = 'auto',
							max_depth = None,
							min_samples_split = 2,
							min_samples_leaf = 1,
							min_weight_fraction_leaf = 0,
							max_leaf_nodes = None,
							n_jobs = -1)
							
mdl.fit(d_ind, d_target)
result = mdl.predict(t_ind)

res = mdl.score(t_ind, t_target)
print(res*100)

# Performance on the test data is measured at 98% accuracy.

# With a well fitted model, it is possible to establish the relative importance of the
# included factors.

importance = mdl.feature_importances_
name = list(d_ind)

# print("Type		Importance")	
# for i in range(8):
#	print (name[i], "	", importance[i])

y_pos = np.arange(len(name))
plt.figure(figsize=(9,10))
plt.bar(y_pos, importance)
plt.xticks(y_pos, name)
plt.ylabel('Importance')
plt.title('Importance of Factors Related to Heating and Cooling Load')
plt.show()

# Discussion

# Out of sample prediction accuracy is measured at 98%. Results indicate the most important 
# factors related to Heating and Cooling Loads are: Compactness and Height. These values differ 
# significantly from the others. Surface-Area and Roof-Area can also show as important factors, 
# and over many runs they show not to be stable as especially-pronounced features as the other two.
# These relative-importances should be interpreted as efficiently deduced for the purposes of
# predictive modeling, where it is highly recommended that established design conclusions follow
# from the direct utilization of this model.  

# Conclusion
# The results of this study indicate the existence of significant design features that can inform 
# a practical perspective. The Random Forest model is highly effective for the ends of Heating and 
# Cooling Load prediction, and can be used to predict these quantities provided all relevant feature-
# values are included.

