class Progression:
    """Iterator producing a generic progression.
    Default iterator produces the whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self.current = start

    def advance(self):
        """Update self.current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self.current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self.current is None:  # our convention to end a progression
            raise StopIteration()
        else:
            answer = self.current  # record current value to return
            self.advance()  # advance to prepare for next time
            return answer  # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    """
    # This was originally given by the professor:
        def print_progression(self, n):
            #Print next n values of the progression.
            print(' '.join(str(next(self)) for j in range(n)))
    # Below is the corrected version:
    """

    def print_progression(self, n):
        """Print next n values of the progression."""
        try:
            for j in range(n):
                print(next(self), end=' ')
        except StopIteration:
            pass
        print()  # print a newline at the end

class ArithmeticProgression(Progression):  # inherit from Progression
    """Iterator producing an arithmetic progression."""
    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.
        increment the fixed constant to add to each term (default 1)
        start the first term of the progression (default 0)
        """
        super().__init__(start)  # initialize base class
        self.increment = increment

    def advance(self):  # override inherited version
        """Update current value by adding the fixed increment."""
        self.current += self.increment


class GeometricProgression(Progression):  # inherit from Progression
    """Iterator producing a geometric progression."""
    def __init__(self, base=2, start=1):
        """Create a new geometric progression.
        base the fixed constant multiplied to each term (default 2)
        start the first term of the progression (default 1)
        """
        super().__init__(start)
        self.base = base

    def advance(self):  # override inherited version
        """Update current value by multiplying it by the base value."""
        self.current *= self.base


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""
    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression.
        first the first term of the progression (default 0)
        second the second term of the progression (default 1)
        """
        super().__init__(first)  # start progression at first
        self.prev = second - first  # fictitious value preceding the first

    def advance(self):
        """Update current value by taking sum of previous two."""
        self.prev, self.current = self.current, self.prev + self.current

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
        if self.current == 1:
            # reach the end of the progression, stop.
            self.current = None
        elif self.current % 2 == 0:
            # it is an even number
            self.current = self.current / 2
        else:
            # if is an odd number
            self.current = self.current * 3 + 1


if __name__ == "__main__":
    print("Default progression:")
    Progression().print_progression(10)
    print("Arithmetic progression with increment 5:")
    ArithmeticProgression(5).print_progression(10)
    print("Arithmetic progression with increment 5 and start 2:")
    ArithmeticProgression(5, 2).print_progression(10)
    print("Geometric progression with default base:")
    GeometricProgression().print_progression(10)
    print("Geometric progression with base 3:")
    GeometricProgression(3).print_progression(10)
    print("Fibonacci progression with default start values:")
    FibonacciProgression().print_progression(10)
    print("Fibonacci progression with start values 4 and 6:")
    FibonacciProgression(4, 6).print_progression(10)
    print("Colatz progression with default start values:")
    ColatzProgression().print_progression(10)
    print("Colatz progression with start value 5:")
    ColatzProgression(5).print_progression(10)