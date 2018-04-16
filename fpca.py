import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, BSpline
from sklearn.decomposition import PCA
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input")
args = parser.parse_args()

INPUT_FILENAME = args.input

X = []
with open(INPUT_FILENAME) as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    # change contents to floats
    for row in reader:
        X.append(row)

feature = np.array([])
for i in range (0, 15):
    c = interp1d(np.arange(0, 31), X[i], kind = "cubic")
    # feature vector corresponding to ith record
    feature = np.append(feature, c._spline.tck[1])

feature = np.reshape(feature, (15, 31))
plt.plot(feature.T,'black')
pca = PCA()
plt.plot(pca.fit_transform(feature.T))
plt.show()
