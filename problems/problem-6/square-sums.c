/* Chris Milson March 2017
** The sum of the squares of the first ten natural numbers is,
* 1^2 + 2^2 + ... + 10^2 = 385
*
* The square of the sum of the first ten natural numbers is,
* (1 + 2 + ... + 10)^2 = 55^2 = 3025
*
* Hence the difference between the sum of the squares of the first ten natural
* numbers and the square of the sum is 3025 − 385 = 2640.
*
* Find the difference between the sum of the squares of the first one hundred
* natural numbers and the square of the sum.
*
* Answer: 25164150.
*/

/*
** We can use the closed form of both the sum of the first n natural
* numbers and the sum of the square of the first n natural numbers. Being
* n(n + 1)/2 and n(n + 1)(2n + 1)/6 respectively.
*/

#include <stdio.h>
#include <stdlib.h>

#define N 100

int main(int argc, char **argv) {
  int sumSquares;
  int sumNums;

  printf("\nThe sum of the squares of the first %d ", N);
  printf("natural numbers is %d.\n\n", sumSquares = sumNaturalSquares(N));

  printf("The sum of the first %d natural numbers is %d.\n", N, sumNums = sumNaturals(N));
  printf("So the square of sum of the first %d natural numbers is ", N);
  printf("going to be %d^2 = %d\n\n", sumNums, sumNums * sumNums);

  int diff = sumNums * sumNums - sumSquares;
  printf("So their difference is %d\n\n", diff < 0 ? -diff : diff);
  return 0;
}

int sumNaturals(int n) {
  return (n * (n + 1)) / 2;
}

int sumNaturalSquares(int n) {
  return (n * (n + 1) * (2 * n + 1)) / 6;
}
