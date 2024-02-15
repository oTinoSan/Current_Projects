**check for tensorRT package**

dpkg -l | grep libnvinfer

result:
ii  libnvinfer-bin                                   8.2.1-1+cuda10.2                              arm64        TensorRT binaries
ii  libnvinfer-dev                                   8.2.1-1+cuda10.2                              arm64        TensorRT development libraries and headers
ii  libnvinfer-doc                                   8.2.1-1+cuda10.2                              all          TensorRT documentation
ii  libnvinfer-plugin-dev                            8.2.1-1+cuda10.2                              arm64        TensorRT plugin libraries
ii  libnvinfer-plugin8                               8.2.1-1+cuda10.2                              arm64        TensorRT plugin libraries
ii  libnvinfer-samples                               8.2.1-1+cuda10.2                              all          TensorRT samples
ii  libnvinfer8                                      8.2.1-1+cuda10.2                              arm64        TensorRT runtime libraries

TensorRT version: 8.2.1
TensorRT package revision number: -1
Cuda version compatability: +cuda10.2

**check tensorRT libraries in library path**

ldconfig -p | grep libnvinfer

**check cuda and cuDNN versions**

nvcc --version
cat /usr/include/cudnn_version.h | grep CUDNN_MAJOR -A 2

**check pytorch version**

pip3 show torch


'''
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
'''
