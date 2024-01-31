# file: csc220a1.py

""" This file is to demonstrate how a badly designed algorithm can take a long
    time to run. We will address this probelm in Chapter 4."""

from time import time

def fib(input_value):
    """ A naive implementation of the fibonacci sequence.
        Input: an integer representing the input value.
        Returns: the computed fibonacci number. """
    if input_value < 1:
        return abs(input_value)
    return fib(input_value-1) + fib(input_value-2)

def get_base_line():
    """ This function computes the base line for using a loop.
        Input: None
        Returns: the number of seconds to executed one iteration of an empty loop. """
    start = time()
    counter = 0
    end = start + 1
    current = start
    while current < end:
        counter = counter + 1
        current = time()
    return (current - start) / counter

def time_it(input_value, baseline):
    """ This function times the execution of the fibonacci number.
        Input: input_value - the input value to the fib function.
               baseline - the time needed for implementing the loop.
        Returns: the value of the fibonacci number, and
                 the time it takes to compute the fibonacci number. """
    start = time()
    counter = 0
    end = start + 1
    current = start
    while current < end:
        counter = counter + 1
        result = fib(input_value)
        current = time()
    elapsed = (current - start) / counter - baseline
    return (result, elapsed)

def test():
    """ This is the function to execute the timing test.
        Input: None
        Returns: None """
    done = False
    baseline = get_base_line()
    input_value = 1
    while not done:
        result, elapsed = time_it(input_value, baseline)
        print(f'time = {elapsed:14.9f}s, fib ({input_value:2d}) = {result:12d}')
        done = elapsed > 3600.0
        input_value = input_value + 1

test()
