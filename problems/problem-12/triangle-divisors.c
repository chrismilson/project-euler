/* Chris and Andrew Milson April 2017
** The sequence of triangle numbers is generated by adding the natural numbers.
* So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
*
* The first ten terms would be:
*
* 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
*
* Let us list the factors of the first seven triangle numbers:
*
*  1: 1
*  3: 1,3
*  6: 1,2,3,6
* 10: 1,2,5,10
* 15: 1,3,5,15
* 21: 1,3,7,21
* 28: 1,2,4,7,14,28
*
* We can see that 28 is the first triangle number to have over five divisors.
*
* What is the value of the first triangle number to have over five hundred
* divisors?
*
* Answer :
*/

/* Chris' Approach
** I thought of two ways of approaching this.
* 1. Try to create a large triangle number with a lot of factors.
* or.
* 2. Find an algorithm that gets the number of factors of a number and use it
* on consecutive triangle numbers until there is one with over 500 factors.
*
* The second approach sounds more straightforward.
*
* We can work out a numbers factors with its prime factorisiation.
* I would work out the prime factorisation of a number by dividing it evenly
* by two until that wont work any more, then onto 3 etc. keeping track until I
* end up with 1.
*/

#include <stdio.h>
#include <stdlib.h>

int triangle(int n); // Returns the nth triangle number.



int triangle(int n) {
  return n * (n + 1) / 2;
}

int main(int argc, char **argv) {

  return 0;
}
