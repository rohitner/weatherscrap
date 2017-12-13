import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.interpolate import UnivariateSpline
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input")
args = parser.parse_args()

INPUT_FILENAME = args.input

X = []
with open(INPUT_FILENAME) as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        X.append(row)

X_std = StandardScaler().fit_transform(X)
for k in range(1,16):
    x=np.arange(0,31)
    spl = UnivariateSpline(x, X_std[k-1])
    spl.set_smoothing_factor(0.1)
    print(spl.get_coeffs(),"\n",spl.get_knots(),"\n");
    xs=np.linspace(0,30,1000)
    plt.plot(xs, spl(xs), 'b', lw=0.5)               # we can use the spl as a function

u,s,v = np.linalg.svd(X_std.T)
eig_vecs=u
eig_vals=[]
cov_mat = np.cov(X_std.T)
for i in range (0,31):
    eig_vals.append(np.divide(cov_mat.dot(u.T[i]),u.T[i])[0])

eig_pairs = [(np.abs(eig_vals[i]), u.T[i]) for i in range(len(eig_vals))]
spl_f=UnivariateSpline(x,eig_pairs[0][1])
spl_f.set_smoothing_factor(0.1)
plt.plot(xs,spl_f(xs),'r',lw=0.5)
plt.show()
