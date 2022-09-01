#Written By: Robert Briggs

#Imports
import sys
import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d 
from sklearn import datasets


def convert(letter):
    return ord(letter) - 65

def createScreePlot(C): 
    '''C is the covariance matrix of the dataset'''
    U, sigma, Vt = npla.svd(C) 
    
    numList = []
    accumList = []
    
    sumEvals = sum(sigma)
    accum = 0
    for i in range(C.shape[0]):
        num = 100*sigma[i]/sumEvals
        accum += num
        
        numList.append(num)
        accumList.append(accum)
        
    screeWindow = plt.figure()
    plt.ylim(0,100)
    ax = screeWindow.add_axes([0,0,1,1])
    
    PC_count = []

    for i in range(len(sigma)):
        string = "PC"
        string += str(i)
        PC_count.append(string)
    
    ax.bar(PC_count, numList)
    plt.plot(accumList, 'r-')
    screeWindow.show()

  

def getDataMatrix():
    '''Gets user input and produces data matrix accordingly'''

    userInput  = input("\nEnter a custom filename or enter 'iris' to use the sklearn iris dataset or 'breastcancer' to use the sklearn breast cancer dataset: ")

    if userInput.lower() == "iris":
        iris = datasets.load_iris()
        D = iris.data     
        y = iris.target  
        
    elif userInput.lower() == "breastcancer":
        breast_cancer = datasets.load_breast_cancer()
        D = breast_cancer.data     
        y = breast_cancer.target 


    else: 
        try: 
            in_data = np.loadtxt(open(userInput, "rb"), delimiter=",", skiprows=1, converters={0: convert}) 
            in_data_cols = in_data.shape[1] 
            D = in_data[:,1:in_data_cols]
            (n, p) = D.shape
            y = in_data[:,0]
            print("Data set loaded: {} observations and {} columns\n".format(n, p))
          
        except: 
            print("\nAn exception occurred, check spelling and try again (make sure to tag on .csv to the end of file).\n")
        
    return (D,y)
        
def getCovarianceMatrix(D,y,useNpCov = True):
    '''Standardizes the data and produces the covariance matrix 

    IN: -D is the dataset data
        -y is the dataset target
        -the bool useNpCov decides whether or use np.cov or manually calculate the cov matrix. (true = np.cov)

    OUT: -Returns the covariance matrix and the standardized vector Z
    '''
    n = D.shape[0]
    mu = np.mean( D, axis=0 )                     
    M = np.outer( np.ones( (n, 1) ), mu )         
    Z = (D - M)
    Z = Z / np.std(D, axis = 0)

    if useNpCov: 
        C = np.cov(Z.T, bias = False) # use bias = true for small data sets
        
    else: 
        C = (((D-M).T@(D-M))/(n))

    return C,Z; 

def performPCA(C, Z, y): 
    U, sigma, Vt = npla.svd(C)

    principalComponent0, principalComponent1 = U[:,0], U[:,1]

    x0 = Z @ principalComponent0
    x1 = Z @ principalComponent1

    # Plotting projected data.
    fig = plt.figure(dpi=140)
    ax = fig.add_subplot( 111 )

    ax.set_title( "Data Set Projected onto First Two Principal Components" )


    for i in range(np.unique(y).size):
        ax.plot( x0[y == i], x1[y == i],".", markersize=2, label="Type " + str(i))

    ax.set_xlabel( "First principal component" )
    ax.set_ylabel( "Second principal component" )
    plt.legend(loc='upper left')
    plt.ylim([-6,6])

    plt.show()




def main(): 
    D,y = getDataMatrix()
    C,Z = getCovarianceMatrix(D,y)
    createScreePlot(C)
    performPCA(C,Z,y)


main() 

