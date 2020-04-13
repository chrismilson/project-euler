""" Chris Milson April 2020
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Answer : 748317
"""
import math

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

def truncateFront(n):
  return n % (10 ** math.floor(math.log10(n)))

def truncateBack(n):
  return n // 10

def isFrontTruncatablePrime(n):
  t = truncateFront(n)
  return t == 0 or (isPrime(t) and isFrontTruncatablePrime(t))

def isBackTruncatablePrime(n):
  t = truncateBack(n)
  return t == 0 or (isPrime(t) and isBackTruncatablePrime(t))

def findTruncatablePrimes():
  # Since there are only 11, we can stop once we have found them all.
  yetToFind = 11
  truncatablePrimes = []

  i = 4
  while yetToFind > 0:
    nextPrime()
    p = primes[i]
    if isFrontTruncatablePrime(p) and isBackTruncatablePrime(p):
      truncatablePrimes.append(p)
      yetToFind -= 1
    i += 1
  return truncatablePrimes

truncatablePrimes = findTruncatablePrimes()
print('The 11 truncatable primes are:')
print(truncatablePrimes)
print('Their sum is', sum(truncatablePrimes), end='.\n')
