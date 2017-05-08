#!/bin/bash

# Go to Cholesky folder to run codes
cd Cholesky

echo "Running Scipy Cholesky code..." 
python scipy_cholesky.py

echo "Running DAAL Cholesky code..."
python daal_cholesky.py

# Go back to main folder (Benchmarks)
cd ..

# Go to Yatch Linear Regression folder to run codes
cd LinearRegression/Yatch

echo "Running Scipy LR code..."
python scipy_LR.py

echo "Running DAAL LR code..."
python daal_LR.py

# End execution back to main folder
cd ../..

