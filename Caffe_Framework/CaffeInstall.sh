####################################################################################################
####################################################################################################
####################################################################################################
######################### Installing Intel Caffe Framework and      ################################
######################### Running with Python Anaconda Distribution ################################
####################################################################################################
####################################################################################################
####################################################################################################




####################################################################################################
# 1) INITIAL PREPARATIONS
####################################################################################################

sudo apt-get update &&
sudo apt install openssh-server &&
sudo apt-get -y install build-essential git cmake &&
sudo apt-get -y install libprotobuf-dev libleveldb-dev libsnappy-dev &&
sudo apt-get -y install libopencv-dev libhdf5-serial-dev protobuf-compiler &&
sudo apt-get -y install --no-install-recommends libboost-all-dev &&
sudo apt-get -y install libgflags-dev libgoogle-glog-dev liblmdb-dev &&
sudo apt-get -y install libatlas-base-dev && 

####################################################################################################
# 2) INTEL MKL PRE CONFIGURATION ON BASHRC FILE: YOU NEED TO INSTALL MKL LIBRARY
####################################################################################################

echo 'source /opt/intel/bin/compilervars.sh intel64' >> ~/.bashrc &&

####################################################################################################
# 3) GETTING INTEL CAFFE FRAMEWORK FROM GITHUB
####################################################################################################

git clone https://github.com/intel/caffe.git &&
cd caffe &&
echo "export CAFFE_ROOT=`pwd`" >> ~/.bashrc &&
source ~/.bashrc && 
cp Makefile.config.example Makefile.config &&

####################################################################################################
# 4) EDITING MAKEFILE.CONFIG TO POINT BLAS AND PYTHON LIBS AND INCLUDES: PAY ATTENTION TO COMMENTS!
####################################################################################################

gedit Makefile.config

####################################################################################################
# 5) BUILDING TIME!
####################################################################################################

NUM_THREADS=$(($(grep 'core id' /proc/cpuinfo | sort -u | wc -l)*2)) &&
make -j $NUM_THREADS &&

####################################################################################################
# 6) PREPARING CAFFE FOR PYTHON
####################################################################################################

sudo apt-get -y install gfortran python-dev python-pip &&
cd ~/caffe/python &&
for req in $(cat requirements.txt); do sudo pip install $req; done &&
sudo pip install scikit-image &&
sudo ln -s /usr/include/python2.7/ /usr/local/include/python2.7 &&
sudo ln -s /usr/local/lib/python2.7/dist-packages/numpy/core/include/numpy/ \
  /usr/local/include/python2.7/numpy &&
cd ~/caffe &&
make pycaffe -j NUM_THREADS &&
echo "export PYTHONPATH=$CAFFE_ROOT/python" >> ~/.bashrc &&
source ~/.bashrc &&

####################################################################################################
# 7) TESTING CAFFE ENVIROMENT BY RUNNING SEVERAL TESTS
####################################################################################################

make test -j $NUM_THREADS &&
make runtest #"YOU HAVE <some number> DISABLED TESTS" output is OK


####################################################################################################
# 8) RUN EVERY TIME YOU LOG OUT OR OPEN A NEW TERMINAL
####################################################################################################

NUM_THREADS=$(($(grep 'core id' /proc/cpuinfo | sort -u | wc -l)*2)) &&
make -j $NUM_THREADS &&
make pycaffe -j NUM_THREADS

####################################################################################################
# 9) ANACONDA ENVIRONMENT ADJUSTMENTS
####################################################################################################

conda install -c https://conda.anaconda.org/anaconda protobuf

