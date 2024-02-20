import importlib

def check_tensorrt():
    tensorrt_spec = importlib.util.find_spec('tensorrt')
    if tensorrt_spec is not None:
        print("TensorRT is installed.")
    else:
        print("TensorRT is not installed.")

check_tensorrt()
