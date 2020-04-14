""" Chris Milson April 2020
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

## Solution

There are no 1 digit pandigital numbers (1 is not prime).
If the sum of the digits of a number is divisible by 3, that number will also be
divisible by 3 (this is due to 10 being congruent to 1 modulo 3).

This immediately rules out all 2, 3, 5, 6, 8, and 9-digit pandigital numbers,
since:

- 1 + 2 = 3 = 1 * 3
- 1 + 2 + 3 = 6 = 2 * 3
- 1 + 2 + 3 + 4 + 5 = 15 = 5 * 3
- 1 + 2 + 3 + 4 + 5 + 6 = 21 = 7 * 3
- 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36 = 12 * 3
- 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45 = 15 * 3

This means our remaining candidates are 4, and 7-digit pandigital numbers.
We can build these numbers easily; iterating through permutations of digits.

Answer : 7652413
"""
import math
from itertools import chain

def isPrime(n):
  task = 2
  while task * task <= n:
    if n % task == 0: return False
    task += 1
  return True

def buildNum(digits):
  result = 0
  for digit in digits:
    result *= 10
    result += digit
  return result

def swap(i, j, arr):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j]= temp

def reverse(i, j, arr):
  for k in range((j - i) // 2 + 1):
    swap(i + k, j - k, arr)

def nextPermutation(arr):
  """
  Puts the array into the next permutation lexicographically.

  Returns false if returning to the front of the permutation space.
  """
  n = len(arr)
  i = n - 2
  while i >= 0 and arr[i] > arr[i + 1]: i -= 1

  if i >= 0:
    j = i + 1
    while j + 1 < n and arr[i] < arr[j + 1]: j += 1

    swap(i, j, arr)
  reverse(i + 1, n - 1, arr)
  return i >= 0

def pandigitals(n):
  if n < 1 or n >= 10: return []
  digits = list(range(1, n + 1))
  yield buildNum(digits)
  while nextPermutation(digits): yield buildNum(digits)

pandigitalPrimes = list(filter(isPrime, chain(pandigitals(4), pandigitals(7))))

print('There are', len(pandigitalPrimes), 'pandigital primes.')
print('They are:')
print(pandigitalPrimes)
print('The largest is', max(pandigitalPrimes), end='.\n')