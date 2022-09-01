# PCA-Reduction
This project takes a dataset file and produces a screeplot for analyzing the PC components as well as the dataset projected on the first two PC components.


Some file descriptions: 
 >  - DataGenerator.py: Can generate valid .cvs files for random based testing (Some are already generated)
 >  - Nutrition.csv is a non-random dataset that works well with PCA
 >  - PCA.py: Performs PCA dimentionality reduction on given dataset

     
To use with an sklearn dataset (IRIS or BREASTCANCER): 
 > 1. python3 ./pca.py
 > 2. enter either "iris" or "breastcancer" to use the respective sklearn datasets


To use with a data file: 
> 1. python ./pca.py 
> 2. enter the name of the file ex. "Nutrition.csv"
  
Notes: 

> Currently designed to only take input data files configured in a certain way. To see configuration reference any of the .csv files in this project.  
> Make sure to have sklearn, matplotlib, and numpy libraries installed 

Pictures: 

Breastcancer context: 
![image1](output_images/Breastcancer-Projection.png?raw=true "pictransferINIT")

![image2](output_images/Breastcancer-Scree.png?raw=true "pictransferINIT")

Nutrition context: 
![image3](output_images/Nutrition-CLI.png?raw=true "pictransferINIT")

![image4](output_images/Nutrition-Projection.png?raw=true "pictransferINIT")

![image5](output_images/Nutrition-Scree.png?raw=true "pictransferINIT")





