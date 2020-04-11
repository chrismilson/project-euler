""" Chris Milson April 2020
Problem 20

n! means n * (n - 1) * ... * 3 * 2 * 1.

For example, 10! = 10 * 9 * ... * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Answer : 648
"""

def factorialDigits(n):
  """
  Returns a number with the same digits as n! but with the zeros clipped off.
  """
  assert(n >= 0)
  dp = 1
  for i in range(1, n + 1):
    dp *= i
    while not dp % 10: dp //= 10
  return dp

def digitSum(n):
  result = 0
  while n > 0:
    result += n % 10
    n //= 10
  return result

print(digitSum(factorialDigits(100)))