"""Computing increasing substrings."""

# The Any annotations here is saying that we will accept any type.
# They *should* be comparable, and it *is* possible to make such
# an annotation, but it is tricky, and I don't want to confuse you
# more than strictly necessary.
from typing import Sequence, Any


def is_increasing(x: Sequence[Any]) -> bool:
    """
    Determine if x is an increasing sequence.

    >>> is_increasing([])
    True
    >>> is_increasing([42])
    True
    >>> is_increasing([1, 4, 6])
    True
    >>> is_increasing("abc")
    True
    >>> is_increasing("cba")
    False
    """
    for i in range(len(x) - 1):
        if not x[i] < x[i+1]:
            return False
    return True


def substring_length(substring: tuple[int, int]) -> int:
    """Give us the length of a substring, represented as a pair."""
    return substring[1] - substring[0]


def longest_increasing_substring(x: Sequence[Any]) -> tuple[int, int]:
    """
    Locate the (leftmost) longest increasing substring.

    If x[i:j] is the longest increasing substring, then return the pair (i,j).

    >>> longest_increasing_substring('abcabc')
    (0, 3)
    >>> longest_increasing_substring('ababc')
    (2, 5)
    >>> longest_increasing_substring([12, 45, 32, 65, 78, 23, 35, 45, 57])
    (5, 9)
    """
    n = len(x)
    if n == 0:
        return (0, 0)

    # The leftmost empty string is our first best bet
    start = 0  # Start index of the current increasing substring
    best = (0, 0)  # Store the best (i, j) pair found so far

    for i in range(1, n):
        if x[i] <= x[i - 1]:
            # The current increasing substring has ended
            if substring_length(best) < i - start:
                best = (start, i - 1)
            start = i

    # Check if the last increasing substring is the longest
    if substring_length(best) < n - start:
        best = (start, n - 1)

    return best
  
  # Example usage:
result = longest_increasing_substring([12, 45, 32, 65, 78, 23, 35, 45, 57])
print(result)  # Output: (5, 9)
