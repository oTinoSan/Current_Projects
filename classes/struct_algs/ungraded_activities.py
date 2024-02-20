"""
Chapter 2 Ungraded Activity:

Extend the Progression class we have discussed at the end of Chapter to create a Colatz progression. The progression starts with a starting value, which is passed into the constructor of the progression. The next number depends on the previous value: if the previous value is an even number, the next number is half of it; if the previous number is an odd number, the next number is three times this number plus one. The progression ends when it reach the value of 1. For example, the Colatz progression starting with 7 is: 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
"""

class ColatzProgression (Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__ (self, first=100):
        """Create a new fibonacci progression.
           first: the first term of the progression (default 100)
        """
        super().__init__ (first) # start progression at first

    def advance (self):
        """Update current value."""
        if self._current == 1:
            # reach the end of the progression, stop.
            self._current = None
        elif self._current % 2 == 0:
            # it is an even number
            self._current = self._current / 2
        else:
            # if is an odd number
            self._current = self._current * 3 + 1

# Chapter 3 Ungraded Activity is saved as a .png file

"""
Chapter 4:

Do Exercise C-4.21 on Page 182 of the textbook:

Suppose you are given an n-element sequence, S, containing distinct integers that are listed in increasing order. Given a number k, describe a
recursive algorithm to find two integers in S that sum to k, if such a pair exists. What is the running time of your algorithm?

Solution:

Our goal is to find integers a, b ∈ S such that a + b = k. Without lost of generality, we can also assume that a ≤ b. One straight forward way to implement this is to consider every pairs of values in S, and check if they sum up to k. But that will give a O(n2) algorithm.

We can do better by utilizing the property that the values in S are sorted and in ascending order. We add the first number and the last number of the list. If they sum up to k, then we find the answer and can return the result. However, if the sum is less than k, that means the first number is in no way  be able to contribute to the answer, so we can discard it and repeat. Similarly, if the sum is larger than k, then the last number is in no way be able to contribute to the answer, so we can discard it and repeat. The following is the Python implementation:
"""

def sum_to_k_v1 (S, k):
    if len (S) == 0:
        return None
    if S [0] + S [-1] == k:
        return (S [0], S [-1])
    if S [0] + S [-1] < k:
        return sum_to_k_v1 (S [1:], k)
    # else if must be the case that S [0] + S [-1] > k
    return sum_to_k_v1 (S [:-1], k)

"""
Unfortunately, this algorithm is still O(n2), due to the fact that we have to make a copy of the list during each recursive call. However, with a minor modification, we can easily fix the problem:
"""

def sum_to_k_v2 (S, k, start = 0, end = None):
    # first fix the value of end if not provided
    if end is None:
        end = len (S) - 1
    if start > end:
        return None
    if S [start] + S [end] == k:
        return (S [start], S [end])
    if S [start] + S [end] < k:
        return sum_to_k_v2 (S, k, start + 1, end)
    # else if must be the case that S [start] + S [end] > k
    return sum_to_k_v2 (S, k, start, end - 1)

# It should be easy to see that this version is O(n).

"""
As mentioned in the class, Python has a pretty efficient implementation of append operation. The same cannot be said about the prepend operation (insert at index 0). In this exercise, you are asked to derive an experiment to show that prepend is much less efficient then append.

Solution:

We will do the following, creating a list of size 1,000, 10,000, 100,000, and 1,000,000 by both the operations of append and prepend while taking timing information. Here is the code:
"""


from time import time

def listByAppend (n):
    start = time ()
    theList = []
    for i in range (n):
        theList.append (i)
    end = time ()
    return end - start

def listByPrepend (n):
    start = time ()
    theList = []
    for i in range (n):
        theList.insert (0, i)
    end = time ()
    return end - start

def experiment ():
    ns = [int (10**i) for i in range (3, 7)]
    for n in ns:
        time1 = listByAppend (n)
        time2 = listByPrepend (n)
        print ('n = %7d - append: %6.4fs, prepend: %9.4fs.' % (n, time1, time2))

"""
This is the output when I ran the code on my machine:
>>> experiment ()
n =    1000 - append: 0.0002s, prepend:    0.0036s.
n =   10000 - append: 0.0025s, prepend:    0.2520s.
n =  100000 - append: 0.0259s, prepend:   25.8120s.
n = 1000000 - append: 0.2473s, prepend: 2317.8895s.

From the output, it is pretty obvious that the append operation is an O(n) operation as explained in the class. However, the prepend operation is an 0(n**2) operation.
"""
