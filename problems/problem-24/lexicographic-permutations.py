""" Chris Milson April 2020
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?

Answer : 2783915460
"""

def swap(i, j, arr):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def shift(i, j, arr):
  for k in range(j, i, -1):
    swap(k, k - 1, arr)

def factorial(n):
  result = 1
  for i in range(2, n + 1):
    result *= i
  return result


def getPermutation(p, values):
  """
  Reorders the list arr into the pth lexicographical ordering.
  """
  copy = values[:]
  n = len(copy)
  curr = factorial(n - 1)
  for i in range(n - 1):
    shift(i, i + p // curr, copy)
    p %= curr
    curr //= n - 1 - i
  return copy

arr = list('0123456789')

print(''.join(getPermutation(1000000 - 1, arr)))