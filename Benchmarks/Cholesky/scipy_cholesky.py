import time
import numpy as np
import scipy.linalg as linalg

start = time.time()
matrix = np.loadtxt(open("cholesky.csv", "rb"), delimiter=",")

z = np.dot(matrix, matrix.T)
linalg.cholesky(z, lower=True)

print("Time!: ", time.time()-start)
