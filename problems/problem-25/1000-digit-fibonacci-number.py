""" Chris Milson April 2020
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

```
F_1 = F_2 = 1
F_n = F_n-1 + F_n-2, for n > 2
```

Hence the first 12 terms will be:

```
F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144
```

The 12th term, F_12 is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?

Answer : 4782
"""

import math

def digits(n):
  return math.floor(math.log10(n) + 1)

f_n, f_n_1 = 1, 1
n = 2
while digits(f_n) < 1000:
  f_n, f_n_1 = f_n + f_n_1, f_n
  n += 1
print(n)