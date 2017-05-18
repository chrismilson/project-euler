""" Chris Milson May 2017
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?

Answer : 104743
"""

MAXPRIME = 10001

primes = []
i = 2

while len(primes) < MAXPRIME:
    isPrime = True
    for j in primes:
        # print("i = " + str(i) + ", j = " + str(j))
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
    i = i + 1

print "The " + str(MAXPRIME) + "th prime is " + str(primes[MAXPRIME - 1])
