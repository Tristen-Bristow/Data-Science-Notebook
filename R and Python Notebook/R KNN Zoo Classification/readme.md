## A K-Nearest Neighbor Classification Model of Specified Animal Species by Outwardly Observable Phenotypes  
###  
#### Tristen Bristow  
#### capitolmotion@gmail.com  
#### 04/05/2017  
###  
### Sources of data for study:  
###  
####  The following data files for this study (downloaded on 4/4/2017), and include,  
#### http://archive.ics.uci.edu/ml/machine-learning-databases/zoo/zoo.data  
#### http://archive.ics.uci.edu/ml/machine-learning-databases/zoo/zoo.names  
##  
#### To run this script, download zoo.data from the URL above, place in same directory as  
#### the script, run 'animal traits.R' script.  


###  
### Platform for model development and testing:
- RStudio Version 1.0.136 – © 2009-2016 RStudio, Inc.  
- R(x64) 3.3.2  
- Windows 7 Professional 64-bit  
- Intel Core Duo Cpu T9400  @ 2.53 GHz  
- 4 GB RAM  
###  
### Origin of source data: Richard S. Forsyth (donated 5/15/1990) 
###  
### Relevant Information:  
####  Number of instances: 101,  number of traits: 17,  
####      Class# Set of animals:  
####     
####           1 (41) aardvark, antelope, bear, boar, buffalo, calf,  
####                  cavy, cheetah, deer, dolphin, elephant,  
####                  fruitbat, giraffe, girl, goat, gorilla, hamster,  
####                  hare, leopard, lion, lynx, mink, mole, mongoose,  
####                  opossum, oryx, platypus, polecat, pony,  
####                  porpoise, puma, pussycat, raccoon, reindeer,  
####                  seal, sealion, squirrel, vampire, vole, wallaby,wolf  
####           2 (20) chicken, crow, dove, duck, flamingo, gull, hawk,  
####                  kiwi, lark, ostrich, parakeet, penguin, pheasant,  
####                  rhea, skimmer, skua, sparrow, swan, vulture, wren  
####           3 (5)  pitviper, seasnake, slowworm, tortoise, tuatara  
####           4 (13) bass, carp, catfish, chub, dogfish, haddock,  
####                  herring, pike, piranha, seahorse, sole, stingray, tuna  
####           5 (4)  frog, frog, newt, toad  
####           6 (8)  flea, gnat, honeybee, housefly, ladybird, moth, termite, wasp  
####           7 (10) clam, crab, crayfish, lobster, octopus,  
####                  scorpion, seawasp, slug, starfish, worm  
####  
#### Sample size: 101, no missing attributes  
####  
#### Number of Attributes: 18 (animal name, 15 Boolean attributes, 2 numerics)  
####
#### Attribute Information: (name of attribute and type of value domain)  
####   1. animal name:      Unique for each instance  
####   2. hair		Boolean  
####   3. feathers		Boolean  
####   4. eggs		Boolean  
####   5. milk		Boolean  
####   6. airborne		Boolean  
####   7. aquatic		Boolean  
####   8. predator		Boolean  
####   9. toothed		Boolean  
####  10. backbone		Boolean  
####  11. breathes		Boolean  
####  12. venomous		Boolean  
####  13. fins		Boolean  
####  14. legs		Numeric (set of values: {0,2,4,5,6,8})  
####  15. tail		Boolean  
####  16. domestic		Boolean  
####  17. catsize		Boolean  
####  18. type		Numeric (integer values in range [1,7])  





   
