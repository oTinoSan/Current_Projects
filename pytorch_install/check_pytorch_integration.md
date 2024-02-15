**check for tensorRT package**

dpkg -l | grep libnvinfer

**check ro tensorRT libraries in library path**

ldconfig -p | grep libnvinfer

**check cuda and cuDNN versions**

nvcc --version
cat /usr/include/cudnn_version.h | grep CUDNN_MAJOR -A 2

**check pytorch version**

pip3 show torch

**include specific directory for TensorRT libraries in LD_LIBRARY_PATH**

*modifying environment variables*

*Add temporarily: LD_LIBRARY_PATH:*

bash

Copy code

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/aarch64-linux-gnu

Add permanently:
sudo nano ~/.bashrc
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/aarch64-linux-gnu
source bash or restart shell

check:
echo $LD_LIBRARY_PATH

