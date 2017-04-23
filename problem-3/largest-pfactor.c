/* Chris Milson March 2017
** Problem 3:
* The prime factors of 13195 are 5, 7, 13 and 29.
*
* What is the largest prime factor of the number 600851475143?
*
* Answer: 6857.
*/

/*
** I will attempt to solve this by, starting at 2, see if the number is
* divisible by the curent number and if it is divide the larger number by it
* and ask again. if the number is not divisible by the number I will increment
* the number.
*
* I had a problem using int as the type because 600851475143 is larger than the
* max value for int, so I changed everything to unsigned long, as I knew it
* would be meaningless to ask about the prime factorisiation of a negative
* number, and I was out of trouble.
*/

#include <stdio.h>
#include <stdlib.h>

unsigned long largestPrimeFactor(unsigned long);

int main(int argc, char **argv) {
  printf("\n");
  if (argc != 2) {
    printf("\nPlease run the program by doing\n\n\t./largest-pfactor N\n\n");
    printf("Where N is the number you want to know the largest prime factor ");
    printf("of.\n");
    return 0;
  }

  unsigned long number = atol(argv[1]);
  printf("The largest prime factor of %lu ", number);
  printf("is %lu\n", largestPrimeFactor(number));
  printf("\n");
  return 0;
}

unsigned long largestPrimeFactor(unsigned long number) {
  unsigned long largestPrimeFactor = 1;
  unsigned long divisor = 2;
  unsigned long currentNumber = number;
  while (currentNumber > 1) {
    if (!(currentNumber % divisor)) {
      currentNumber /= divisor;
      largestPrimeFactor = divisor;
    } else {
      divisor++;
    }
  }
  return largestPrimeFactor;
}
