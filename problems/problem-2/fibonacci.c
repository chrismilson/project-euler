/* Chris Milson March 2017
** Problem 2:
* Each new term in the Fibonacci sequence is generated by adding the previous
* two terms. By starting with 1 and 2, the first 10 terms will be:
* 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
*
* By considering the terms in the Fibonacci sequence whose values do not exceed
* four million, find the sum of the even-valued terms.
*
* Answer: 4613732.
*/

/*
** I want to do this with two variables, in order to calculate the next number.
* Each time I calculate the next number I will add it to the sum if it is even.
* Checking whether a number is even in c is simple because it only needs to
* check one bit.
* Firstly I will need to check that the max unsigned integer value is at least
* as large as 4 million.
*/

#include <stdio.h>
#include <stdlib.h>
#define MAX 4000000

int main(int argc, char **argv) {
  printf("\n");
  if (sizeof(int) < 3) {
    printf("The integer type cannot hold numbers big enough for this.");
    return 0;
  }

  int num1, num2;
  num1 = num2 = 1;

  int sum = 0;

  while (num1 < MAX) {
    sum += num1 * (1 - (num1 % 2));
    num1 += num2;
    // the following three lines use XOR to swap their value
    num1 ^= num2;
    num2 ^= num1;
    num1 ^= num2;
  }
  printf("The sum of the fibonacci numbers less than %d ",  MAX);
  printf("that are even is %d.\n", sum);
  printf("\n");
  return 0;
}
