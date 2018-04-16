import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,10,0.01)
data = np.array([np.cos(x),np.cos(x+0.1),np.cos(x+1)]).T
noise = np.random.laplace(loc=0.0, scale=0.01, size=np.shape(data))
from sklearn import decomposition
pca = decomposition.PCA()
plt.plot(data+noise,'black')
plt.plot(pca.fit_transform(data+noise)[:,0],label="PC1")
plt.plot(pca.fit_transform(data+noise)[:,1],label="PC2")
plt.plot(pca.fit_transform(data+noise)[:,2],label="PC3")
plt.legend()
plt.show()
