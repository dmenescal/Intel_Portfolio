#===============================================================================
# Copyright 2014-2017 Intel Corporation All Rights Reserved.
#
# The source code,  information  and material  ("Material") contained  herein is
# owned by Intel Corporation or its  suppliers or licensors,  and  title to such
# Material remains with Intel  Corporation or its  suppliers or  licensors.  The
# Material  contains  proprietary  information  of  Intel or  its suppliers  and
# licensors.  The Material is protected by  worldwide copyright  laws and treaty
# provisions.  No part  of  the  Material   may  be  used,  copied,  reproduced,
# modified, published,  uploaded, posted, transmitted,  distributed or disclosed
# in any way without Intel's prior express written permission.  No license under
# any patent,  copyright or other  intellectual property rights  in the Material
# is granted to  or  conferred  upon  you,  either   expressly,  by implication,
# inducement,  estoppel  or  otherwise.  Any  license   under such  intellectual
# property rights must be express and approved by Intel in writing.
#
# Unless otherwise agreed by Intel in writing,  you may not remove or alter this
# notice or  any  other  notice   embedded  in  Materials  by  Intel  or Intel's
# suppliers or licensors in any way.
#===============================================================================

## <a name="DAAL-EXAMPLE-PY-CHOLESKY_BATCH"></a>
## \example cholesky_dense_batch.py

import time
#from os import environ
#from os.path import join as jp
from daal.data_management import FileDataSource, DataSourceIface
from daal.algorithms.cholesky import Batch, choleskyFactor, data

#import sys, os.path
#utils_folder = os.path.realpath(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
#if utils_folder not in sys.path:
#    sys.path.insert(0, utils_folder)
#from utils import printNumericTable

#DAAL_PREFIX = jp('..', 'data')
#  Input data set parameters
dataFileName =  'cholesky.csv' 
#jp(DAAL_PREFIX, 'batch', 'cholesky.csv')

if __name__ == "__main__":
    start = time.time()
    # Initialize FileDataSource to retrieve input data from .csv file
    dataSource = FileDataSource(
        dataFileName,
        DataSourceIface.doAllocateNumericTable,
        DataSourceIface.doDictionaryFromContext
    )

    # Retrieve the data from input file
    dataSource.loadDataBlock()

    # Create algorithm to compute cholesky factor using default method
    algorithm = Batch()

    # Set input arguments of the algorithm
    algorithm.input.set(data, dataSource.getNumericTable())

    # Get computed cholesky factor
    res = algorithm.compute()

    # Print results
    print("Time!: ", time.time() - start)
    #printNumericTable(res.get(choleskyFactor))
