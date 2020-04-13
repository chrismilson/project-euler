""" Chris Milson April 2020
Problem 36

The decimal number, 585 = 1001001001 (in binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

Answer : 872187
"""

def isPalindrome(arr):
  n = len(arr)
  for i in range(n // 2):
    if arr[i] != arr[n - i - 1]:
      return False
  return True

def getDigits(n, base):
  result = []
  while n > 0:
    result.append(n % base)
    n //= base
  result.reverse()
  return result

def multiBasePalindromes(upperBound, bases):
  palindromes = []
  for i in range(1, upperBound):
    for base in bases:
      if not isPalindrome(getDigits(i, base)): break
    else:
      palindromes.append(i)
  return palindromes

n = 1000000
palindromes = multiBasePalindromes(n, [2, 10])
print('The palindromes in decimal and binary less than', n, 'are:')
print(palindromes)
print('Their sum is', sum(palindromes), end='.\n')