# -*- coding: utf-8 -*-
""" Chris Milson April 2020
Problem 31

In the United Kingdom the currency is made up of pound (£) and pence (p). There
are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p). It is possible to make £2
in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

Answer : 73682
"""

def countSums(total, coins):
  dp = [1] + [0] * total
  for coin in coins:
    for j in range(coin, total + 1):
      dp[j] += dp[j - coin]
  return dp[-1]


print(countSums(200, [1, 2, 5, 10, 20, 50, 100, 200]))