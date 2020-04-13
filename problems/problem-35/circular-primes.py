""" Chris Milson April 2020
Problem 35

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?

Answer : 55
"""

def buildNum(digits):
  result = 0
  mult = 1
  for digit in digits:
    result += digit * mult
    mult *= 10
  return result

def getDigits(n):
  result = []
  while n > 0:
    result.append(n % 10)
    n //= 10
  return result

def rotate(arr, steps = 1):
  return arr[steps:] + arr[:steps]

primes = [2, 3, 5, 7]
primeSet = set(primes)
def nextPrime():
  candidate = primes[-1] + 2
  while True:
    for task in primes:
      if task * task > candidate:
        primes.append(candidate)
        primeSet.add(candidate)
        return candidate
      if candidate % task == 0:
        break
    candidate += 2

def isPrime(n):
  while n > primes[-1]: nextPrime()
  return n in primeSet

def isCircularPrime(n):
  if not isPrime(n): return False
  
  digits = getDigits(n)
  k = len(digits)

  for i in range(1, k):
    rotated = buildNum(rotate(digits, i))
    if not isPrime(rotated):
      return False

  return True

def circularPrimes(upperBound):
  circular = []
  for i in range(1, upperBound):
    if isCircularPrime(i):
      circular.append(i)
  return circular

n = 1000000
circular = circularPrimes(n)
print('The circular primes less than', n, 'are:')
print(circular)
print('There are', len(circular), 'of them.')

