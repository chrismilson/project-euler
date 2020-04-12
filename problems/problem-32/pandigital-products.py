# -*- coding: utf-8 -*-
""" Chris Milson April 2020
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

Answer : 45228
"""

def swap(i, j, arr):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

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

def buildNum(arr):
  result = 0
  multiplier = 1
  for v in reversed(arr):
    result += v * multiplier
    multiplier *= 10
  return result

def checkForProducts(p):
  products = set()
  n = len(p)
  for i in range(1, n):
    for j in range(i + 1, n):
      multiplicand = buildNum(p[:i])
      multiplier = buildNum(p[i:j])
      product = buildNum(p[j:])
      if multiplicand * multiplier == product:
        print multiplicand, 'x', multiplier, '=', product
        products.add(product)
  return products

a = [1,2,3,4,5,6,7,8,9]
union = set()
while True:
  union = union.union(checkForProducts(a))
  if not nextPermutation(a):
    break
print 'The sum of the products of this form is', sum(union)