from time import time
start_time = time()
# Code to be timed
end_time = time()
elapsed_time = end_time - start_time

# find the number of primitive ops in the code below:
def find_max(data):
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest
'''
Step1: 2 ops, 3: 2ops, 4: 2n ops, 
5: 2n ops, 6: 0 to n ops, 7: 1 ops
'''
# video 21:24

