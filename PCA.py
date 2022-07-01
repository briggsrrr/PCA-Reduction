#Written By: Robert Briggs

#Imports
import sys
import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d 


def convert(letter):
    return ord(letter) - 65

def createScreePlot(C): 
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
    


   

my_data = np.loadtxt(open("GeneralFormat12Col.csv", "rb"), delimiter=",", skiprows=1, converters={0: convert})  

D = my_data[:,1:9]
y = my_data[:,0]
(n, p) = D.shape
print("Data set loaded: {} observations and {} columns\n".format(n, p))

mu = np.mean( D, axis=0 )                     
M = np.outer( np.ones( (n, 1) ), mu )         
Z = (D - M)

Z = Z / np.std(D, axis = 0)

C = np.cov(Z.T, bias = False)

#finding evals and evecs
evals, evecs = npla.eig(C)

#We need to sort evals and evecs since both are not presented in a sorted fashion
#by numpy, so when comparing to sigma, we need to sort them in descending order

sorted_evals = evals[evals.argsort()[::-1]].real
sorted_evecs = evecs[:,evals.argsort()[::-1]]

createScreePlot(C)




U, sigma, Vt = npla.svd(C)

principalComponent0, principalComponent1 = U[:,0], U[:,1]

x0 = Z @ principalComponent0
x1 = Z @ principalComponent1


# Plotting projected data.
fig = plt.figure(dpi=140)
ax = fig.add_subplot( 111 )

ax.set_title( "Pizza Data Set Projected onto First Two Principal Components" )

for i in range(10):
    ax.plot( x0[y == i], x1[y == i],".", markersize=2, label="Type" + str(i))

ax.set_xlabel( "First principal component" )
ax.set_ylabel( "Second principal component" )
plt.legend(loc='upper left')
plt.ylim([-3,3])
plt.show()

