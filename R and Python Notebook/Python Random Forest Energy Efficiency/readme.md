### Prediction of Heating and Cooling Loads in Building Design  
### Tristen Bristow  
### capitolmotion@gmail.com  
### 05/01/2017  

#### Data download link:  
#### http://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx  
#### Downloaded on 4/30/2017  

#### To run this script, download xlsx file above and place in same folder  
#### as the python script.  

###  
### Plotform for model development and testing:  
- RStudio Version 1.0.136 – © 2009-2016 RStudio, Inc.  
- R(x64) 3.3.2  
- Windows 7 Professional 64-bit  
- Intel Core Duo Cpu T9400  @ 2.53 GHz  
- 4 GB RAM  
###  
### 

###	Data Description:  
#### number of samples: n = 768,  
#### X1 Relative Compactness (%)
#### X2 Surface Area (m²)
#### X3 Wall Area (m²)
#### X4 Roof Area (m²)
#### X5 Overall Height (m)
#### X6 Orientation (1-4)
#### X7 Glazing Area (% surface covered)
#### X8 Glazing Area Distribution (1-5):

####	1) uniform: with 25% glazing on each side,  
####	2) north: 55% on the north side and 15% on  
####	each of the other sides,  
####	3) east: 55% on the east side and 15% on each  
####	of the other sides,  
####	4) south: 55% on the south side  
####	and 15% on each of the other sides, and  
####	5) west: 55% on the west side and 15% on each  
####	of the other sides. In addition, obtained samples  
####	with no glazing areas. Finally, all shapes  
####	were rotated to face the four cardinal points  
####	y1 Heating Load (W/m²)  
####	y2 Cooling Load (W/m²)  


#### "Taking the elementary cube (3.5 × 3.5 × 3.5) we generated  
#### 12 building forms where each building form is composed of  
#### 18 elements (elementary cubes). The simulated buildings  
#### were generated using Ecotect. All the buildings have the  
#### same volume, which is 771.75 m3, but different surface areas  
#### and dimensions. The materials used for each of the 18  
#### elments are the same for all building forms." - Accurate  
#### quantitative estimation of energy performance of residential  
#### buildings using statistical machine learning tools" 
#### Athanasios Tsanas, Angeliki Xifara.  





