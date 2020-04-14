""" Chris Milson April 2020
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note
the following:

- d_2d_3d_4 = 406 is divisible by 2
- d_3d_4d_5 = 063 is divisible by 3
- d_4d_5d_6 = 635 is divisible by 5
- d_5d_6d_7 = 357 is divisible by 7
- d_6d_7d_8 = 572 is divisible by 11
- d_7d_8d_9 = 728 is divisible by 13
- d_8d_9d_10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

Answer : 16695334890
"""

def buildNum(digits):
  result = 0
  for digit in digits:
    result *= 10
    result += digit
  return result

def hasProperty(digits):
  """
  Verifies that a 0-9 pandigital number has the special property.
  """
  if buildNum(digits[1:4]) % 2: return False
  if buildNum(digits[2:5]) % 3: return False
  if buildNum(digits[3:6]) % 5: return False
  if buildNum(digits[4:7]) % 7: return False
  if buildNum(digits[5:8]) % 11: return False
  if buildNum(digits[6:9]) % 13: return False
  if buildNum(digits[7:10]) % 17: return False
  return True

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

def pandigitals():
  digits = list(range(10))
  yield digits
  while nextPermutation(digits): yield digits


specialSum = 0
print('The 0-9 pandigitals with the special property are:')
for i in map(buildNum, filter(hasProperty, pandigitals())):
  specialSum += i
  print(i)
print('Their sum is', specialSum, end='.\n')