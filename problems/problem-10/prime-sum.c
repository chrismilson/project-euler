/* Chris Milson April 2017
** The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
*
* Find the sum of all primes less than two million.
*
* Answer :  142913828922
*/

/* This will be a stock standard loop that checks if a number is prime and then
** adds it to a sum.
*
* My method to check primality of n will consist of checking that the remainder
* of n when divided by m is not zero when m is less than or equal to the square
* root of n.
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX 2000000

int discreteSqrt(int number);

int isPrime(int number);

int isPrime(int p) {
  int i, root;
  root = discreteSqrt(p);
  for (i = 2; i <= root; i++) {
    if (p % i == 0) return 0;
  }
  return 1;
}

// I had to change some of the logic in here to make sure it worked on square
// numbers as I was incorectly assuming some of them were prime.
int discreteSqrt(int n) {
  int root = 0;
  while (root * root <= n) {
    root++;
  }
  return root - 1;
}

int main(int argc, char **argv) {
  int i;
  unsigned long sum = 0;

  for (i = 2; i < MAX; i++) {
    if (isPrime(i)) sum += i;
  }

  printf("\nThe sum of all primes less than %d is %lu.\n\n", MAX, sum);

  return 0;
}
