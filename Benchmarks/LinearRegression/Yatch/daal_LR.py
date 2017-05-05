#This code is only focused on finding the coeficients for the linear equation, not testing!


import time
import numpy as np
import math
from numpy import genfromtxt
from daal.data_management import BlockDescriptor_Float64, readOnly, HomogenNumericTable
start = time.time()
data = np.genfromtxt('yacht_hydrodynamics.csv')

sample = np.random.choice(len(data), size=math.floor(.8*len(data)), replace=False)

select = np.in1d(range(data.shape[0]), sample)

numpy_train_data = data[select,:]
#numpy_test_data = data[~select,:]

train_data_table = HomogenNumericTable(data[select,:])
#test_data_table = HomogenNumericTable(data[~select,:])

train_data_dependent_variable = numpy_train_data[:,6].reshape(246,1)

#print("Dimension of the train_data dependent variable: {}".format(train_data_dependent_variable.shape))

train_data = np.delete(numpy_train_data, (6), axis=1)
#print("Dimension of the train_data: {}".format(train_data.shape))


# We need to do the same with the test_data

#test_data_dependent_variable = numpy_test_data[:,6].reshape(62,1)

#print("Dimension of the test_data dependent variable: {}".format(test_data_dependent_variable.shape))

#test_data = np.delete(numpy_test_data, (6), axis=1)
#print("Dimension of the test_data: {}".format(test_data.shape))

from daal.algorithms.linear_regression import training

train_data_table = HomogenNumericTable(train_data)
train_outcome_table = HomogenNumericTable(train_data_dependent_variable)

algorithm = training.Batch_Float64NormEqDense()
                                                                                                   
algorithm.input.set(training.data, train_data_table)

algorithm.input.set(training.dependentVariables, train_outcome_table)

trainingResult = algorithm.compute()

beta = trainingResult.get(training.model).getBeta()

block_descriptor = BlockDescriptor_Float64()

beta.getBlockOfRows(0, beta.getNumberOfRows(), readOnly, block_descriptor)

beta_coeficients = block_descriptor.getArray()

beta.releaseBlockOfRows(block_descriptor)

print("Time!!: ", time.time()-start)
#print("Coeficients: {}".format(beta_coeficients))
