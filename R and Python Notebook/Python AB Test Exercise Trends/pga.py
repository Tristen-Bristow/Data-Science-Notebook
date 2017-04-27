# Day-of-Week Exercise Trends 
# A/B Testing of Significant Biased Variation of Time-Based Based Walking Activity
# Tristen Bristow
# 04/08/2017

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import math
import scipy.stats
import matplotlib.mlab as mlab



# Loading and preprocessing the data  

# Activity monitoring data [52K] Data downloaded from:
# https://d396qusza40orc.cloudfront.net/repdata%2Fdata%2Factivity.zip

df=pd.read_csv('activity.csv')
fmt = '%Y-%m-%d'
df['date']=pd.to_datetime(df['date'],format=fmt)


np.random.seed(12345678)






# imputing missing values
print
print("total of na for each column:")
print(df.isnull().sum())
print("fract of na for each column:")
print(df.isnull().mean())
print
# print here it is observed that 13% of the values
# in the step column are missing (labeled NaN)
# so, it seems clear that imputing these values
# would be a bad decision, as we do not have any
# additional information about the data that would
# justify such an approach. It is certain, based on
# this large percentage of missing values, that all
# statistical results will be affected by such a
# decision. The values are thus removed from the
# transformed analysis set.

df=df.dropna()







mean_steps_day = pd.pivot_table(df, index=['date'], values=['steps'], aggfunc=np.mean)
print(mean_steps_day.describe())
mean_steps_day=mean_steps_day.dropna()
print(mean_steps_day)	
x = mean_steps_day['steps'].mean()
plt.axvline(x,linewidth=3, color='k')
plt.text(x+0.2, .0355, r'$\mu$', size=20, rotation=90)


plt.hist(mean_steps_day['steps'], 10 , normed=True)

x = np.linspace(min(mean_steps_day['steps']), max(mean_steps_day['steps']), 100)
mean = np.mean(mean_steps_day['steps'])
variance = np.var(mean_steps_day['steps'])
sigma = np.sqrt(variance)
plt.plot(x, mlab.normpdf(x, mean, sigma), linewidth=3)

plt.xlabel('# Steps/day')
plt.ylabel('Frequency')
plt.title('Average Step-Rate Over Day Distribution')

# Here we see that the mean value of number of steps
# is centered in this plotted distribution, which
# indicates, also by guassian shape, that the data is sufficiently
# normal in its distribution.	

plt.show()

	
# Average daily activity pattern. Bin over 5 sec intervals
# 288 total 5 sec periods over which to aggregate.

mean_steps_act = pd.pivot_table(df, index=['interval'], values=['steps'], aggfunc=np.mean)

print
plt.xlabel('Time (seconds)')
plt.ylabel('Number of Steps')
plt.plot(range(1, 5*288, 5), mean_steps_act)
plt.title('Average Number of Steps per Interval Over a Day-Period')
avy = mean_steps_act['steps'].mean()
print(avy )
plt.axhline(y=avy , hold=None)
plt.text(1, avy , r'$\mu$', size=20, rotation=90)
plt.show()

# Are there differences in activity patterns between weekdays and weekends? 
# A decision is made to create a new class label for the data, weekend vs 
# non-weekend.


wknd = df['date'].dt.dayofweek 

wknd[wknd <= 4] = 0
wknd[wknd > 4] = 1
df['wknd'] = wknd



classA = df[df['wknd']==0]
classB = df[df['wknd']==1]



print("************")
datestepA = pd.pivot_table(classA, index=['date'], values=['steps'], aggfunc=np.mean)
datestepB = pd.pivot_table(classB, index=['date'], values=['steps'], aggfunc=np.mean)
print("************")


xx = datestepA['steps'].mean()
yy = datestepB['steps'].mean()
plt.axvline(xx,linewidth=3, color='blue')
plt.axvline(yy,linewidth=3, color='green')
glab1 = r'$\mu_1$'
glab2 = r'$\mu_2$' 
plt.text(xx+0.2, .06, glab1, size=20, rotation=90, color='blue')
plt.text(yy+0.2, .06, glab2, size=20, rotation=90, color='green')

plt.hist(datestepA['steps'], 10, normed=True, label='Weekday')
plt.hist(datestepB['steps'], 3.5, normed=True, label='Weekend')
plt.xlabel("Number of Steps")
plt.ylabel("Frequency")
plt.title('Average Steps per Interval Weekday vs. Weekend')
plt.legend(loc = 'upper right')
plt.show()

# Is there a significant difference between weekend and
# weekday activity? Since this is a binary class we're
# interested in, Logistic Regression is used to determine
# if a possible relationship exists in the data.

#	H_0: X_wkdy = X_wknd
#	H_1: X_wkdy <> X_wknd


#plt.scatter(disA['wknd'],disA['steps'],c='b')
#plt.scatter(disB['wknd'],disB['steps'],c='y')


twosample_results = scipy.stats.ttest_ind(classA['steps'], classB['steps'],equal_var=False,axis=0)

# Test for difference in mean steps/day between weekday and weekend
print("****Is p < 0.05 ?")
print(twosample_results)
print("****")

# The test result from 2-sample-t-test is 
# p = 0.0002, where the statistical 
# significance threshold for rejecting the null 
# is set to α_1 = 0.05. The test indicates p < α_1, 
# thus it is supported that
# a significant difference in means, H_1, is
# indicated over the null hypothesis H_0, that
# no significant difference exists  
# exists between average total number of steps and the 
# day, conditioned on that day being weekday or 
# weekend.

# A/B Testing

# it looks like weekday activity is greater. This poses a
# new hypothesis that the average number of steps taken
# on the weekday is greater than the average number of
# steps taken on the weekend. We assign subject label A 
# to weekday average number of steps, and label B to weekend 
# average number of steps. We are interested in testing a
# hypothesis that the average associated with A is greater
# than the average associated with B, vs the null hypothesis,
# that a discernable positive difference of A over B doesn't
# exist:
#
#	H_1: X_wkdy <> X_wknd
#	H_2: X_wknd > X_wkdy 

# The new test is a 2-Sample upper one-sided t-test, so the test 
# statistic is calculated the same way as before, only now the
# threshold for acceptance is α_2 = 0.025. As before, we reject the 
# null for the alternate hypothesis if p < α_2.

twosample_results2 = scipy.stats.ttest_ind(classB['steps'],classA['steps'],equal_var=False,axis=0)

print("****Is p_2 < 0.025 ?")
print(twosample_results2)
print("****")

# p_2 < α_2, thus The test result indicates that we reject the null 
# hypothesis for the alternate hypothesis, that the number of steps  
# taken on a weekday will be greater than the number of steps taken   
# on a weekend, on average.  