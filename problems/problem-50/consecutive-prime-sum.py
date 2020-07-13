""" Chris Milson July 2020
Problem 50

# Consecutive Prime Sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13 This is the longest sum of consecutive primes that
adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

Answer : 997651

The sum of 543 primes starting at 7
"""

cap = 1000000

primes = [2, 3, 5]
cumSumPrimes = [0, 2, 5, 10]
def nextPrime():
  candidate = primes[-1] + 2
  while True:
    for prime in primes:
      if prime * prime > candidate:
        primes.append(candidate)
        cumSumPrimes.append(cumSumPrimes[-1] + candidate)
        return
      if candidate % prime == 0:
        break
    candidate += 2

while primes[-1] < cap:
  nextPrime()

def isPrime(candidate):
  if candidate in primes:
    return True
  for prime in primes:
    if prime * prime > candidate:
      return True
    if candidate % prime == 0:
      return False

def printSum(start, end):
  left = ' + '.join(str(p) for p in primes[start:end + 1])
  right = cumSumPrimes[end] - cumSumPrimes[start]
  print(f'{left} = {right}')

maxSoFar = 1

for start in range(len(primes)):
  lo = start + 1
  hi = len(primes)
  while lo < hi:
    mid = lo + ((hi - lo) >> 1)
    if cumSumPrimes[mid] - cumSumPrimes[start] < cap:
      lo = mid + 1
    else:
      hi = mid
  end = lo - 1
  while end > start + maxSoFar:
    if isPrime(cumSumPrimes[end] - cumSumPrimes[start]):
      printSum(start, end)
      maxSoFar = max(maxSoFar, end - start)
    end -= 1

print(maxSoFar)
