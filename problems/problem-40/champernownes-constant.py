""" Chris Milson April 2020
Problem 40

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d(n) represents the nth digit of the fractional part, find the value of the
following expression.

d(1) × d(10) × d(100) × d(1000) × d(10000) × d(100000) × d(1000000)

## Solution

There are 9 numbers with 1 digit and thus there are 9 * 1 digits first.

Then there are 90 numbers with 2 digits, so there are 90 * 2 digits next.

Then there are 900 numbers with 3 digits, so there are 900 * 3 digits next.

We can iteratively subtract these counts, while our number is definitely in the
next group, and we will be left with an offset from 10^g where g was the group
number that the number was in.

Answer : 210
"""

def d(n):
  """
  Returns the nth digit of champernowne's constant.
  """
  group = 1
  groupSize = 9
  while n >= groupSize * group:
    n -= groupSize * group
    group += 1
    groupSize *= 10
  n -= 1
  # This is the number that the index is inside of
  number = 10 ** (group - 1) + n // group
  # this is the index of the digit (from the right) that we want
  digit = group - n % group - 1
  number //= (10 ** digit)
  return number % 10
  
indicies = [1, 10, 100, 1000, 10000, 100000, 1000000]
digits = list(map(d, indicies))

print('The digit at the respective index in Champernowne\'s constant is:')
product = 1
for index, digit in zip(indicies, digits):
  product *= digit
  print(index, digit)
print('The product of those digits is', product, end='.\n')