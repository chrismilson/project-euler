""" Chris Milson April 2020
Problem 42

The nth term of the sequence of triangle numbers is given by, t(n) = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t(10). If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?

## Solution

If a number t is a triangle number, then we will have t = ½n(n+1) for some n >
0. This is just a quadratic equation in n, which when rearranged gives:

n^2 + n - 2t = 0

By the quadratic formula, n = ½(sqrt(1 + 8t) - 1), we will call this function
T(t).

For any given k, we can calculate T(k). If T(k) is a whole number then k must be
a triangle number; specifically the T(k)th triangle number. For T(k) to be a
whole number, sqrt(1 + 8t) - 1 must be divisible by 2, so sqrt(1 + 8t) must be
odd. The expression 1 + 8t is odd for all t, so this is true for all 1 + 8t that
are perfect squares. Now we have '1 + 8t is a perfect square' is a
characterisation for 't is a triangle number'. We can calculate 1 + 8t in O(1)
time, and we can check that it is a perfect square in O(log(t)) time (with a
binary search)

Answer : 
"""

def isTriangle(n):
  """
  Uses a characterisation of whether a number is triangular, described in the
  block comment at the top.

  Runs in O(log(n)) time with O(1) space.
  """
  # This is so that we can start the binary search with hi = n
  if n < 8: return n == 1 or n == 3 or n == 6

  target = 1 + 8 * n
  lo = 0
  hi = n
  while lo < hi:
    mid = lo + ((hi - lo) >> 1)
    sq = mid * mid
    if sq == target: return True
    elif sq > target: hi = mid
    else: lo = mid + 1
  return False

def wordScore(word):
  # ord('A') = 65, and A should be worth 1 point
  return sum(ord(c) - 64 for c in word)

with open('words.txt') as file:
  words = map(lambda x: x.replace('"', ''), file.readline().split(','))
  triangleWords = list(filter(lambda x: isTriangle(wordScore(x)), words))
  print(
    'There are',
    len(triangleWords),
    'words in the list whose word value is a triangular number.'
  )
  