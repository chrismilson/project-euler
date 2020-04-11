""" Chris Milson April 2020
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

```
1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1
```

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.

Answer : 983
"""

def lengthOfReciprocalCycle(target):
  # This is somewhat similar to long division, and we keep going until we get
  # the same remainder twice.
  seen = {}
  task = 1
  runs = 0
  while task not in seen:
    if task == 0: return 0
    seen[task] = runs
    while task < target:
      task *= 10
      runs += 1
    task %= target
  
  return runs - seen[task]
  
maxSoFar = 0
culprit = 1
for i in range(1, 1000):
  length = lengthOfReciprocalCycle(i)
  if length > maxSoFar:
    maxSoFar = length
    culprit = i

print culprit, 'has a reciprocal cycle', maxSoFar, 'digits long.'