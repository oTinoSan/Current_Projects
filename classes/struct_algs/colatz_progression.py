"""
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