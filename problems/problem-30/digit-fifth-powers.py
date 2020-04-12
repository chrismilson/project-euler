""" Chris Milson April 2020
Problem 30

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

```
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.
```

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

## Solution

We can say that the sum of the fifth powers of a number, n, can be bounded above
by

u(n) = log10(n) * 9^5

Since the number will have log10(n) digits that can be maximum 9. Thus we can
find an upper bound for all numbers that may be able to be written as the sum of
the fifth power of their digits by finding the point at which n > u(n).

After finding this upper bound, we can then check each number from 2 up to this
value for the digit sum property and that will be all of them.

Answer : 
"""
import math

def findUpperBound(power):
  def upper(n):
    return math.floor(math.log10(n) + 1) * 9 ** power
  i = 9 ** power
  while i < upper(i):
    i *= 2
  return i

def digitPowerSum(n, power):
  result = 0
  while n > 0:
    result += (n % 10) ** power
    n //= 10
  return result

def specialNumbers(power):
  upperBound = findUpperBound(power)

  result = []
  for i in range(2, upperBound):
    if i == digitPowerSum(i, power):
      result.append(i)

  return result

print(sum(specialNumbers(5)))

