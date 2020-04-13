""" Chris Milson April 2020
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.

Answer : 
"""

def buildNum(digits):
  """
  Takes an array of digits and returns the number they should represent
  """
  result = 0
  mult = 1
  for d in reversed(digits):
    result += d * mult
    mult *= 10
  return result

def findCancels():
  cancels = []

  for a in range(1, 10):
    for b in range(1, 10):
      for c in range(1, 10):
        ab = buildNum([a, b])
        bc = buildNum([b, c])
        if ab != bc and ab * c == a * bc:
          cancels.append((ab, bc))
  return cancels

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def reduceFraction(fraction):
  numerator, denominator = fraction
  greatestCommonDivisor = gcd(numerator, denominator)
  return (
    numerator / greatestCommonDivisor,
    denominator / greatestCommonDivisor
  )

def multiplyFractions(fractions):
  numerator, denominator = 1, 1

  for n, d in fractions:
    numerator *= n
    denominator *= d
    
  return (numerator, denominator)

print reduceFraction(multiplyFractions(map(reduceFraction, findCancels())))[1]
  