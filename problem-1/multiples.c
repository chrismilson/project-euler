/* Chris Milson 17/3/2017
** Problem 1:
* If we list all the natural numbers below 10 that are multiples of 3 or 5,
* we get 3, 5, 6 and 9. The sum of these multiples is 23.
*
* Find the sum of all the multiples of 3 or 5 below 1000.
*
* Answer: 233168.
*/

/*
** I want to solve this by going through all the numbers starting at zero and
* if the number is a multiple of 3 or 5 I will add it to a "sum" variable.
*
* I made this program so that the user can decide the numbers, rather than them
* being stuck at 3, 5, and 1000.
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) {
  if (argc < 3) {
    printf("\nPlease enter numbers in the following format:\n");
    printf("First enter the upper limit of the numbers you are checking.\n");
    printf("Then enter the numbers that you want to add multiples of.\n\n");

    printf("If I wanted to know what the sum of all the multiples of 4 or 6 ");
    printf("less than 1000 I would run the following code:\n\n");
    printf("\t./multiples 1000 4 6\n\n");
    return 0;
  }

  int max;
  printf("The sum of the numbers less than %d ", max = atoi(argv[1]));
  printf("that are multiples of ");
  int i, num;
  int *numbers;
  numbers = (int *) malloc(sizeof(int) * (argc - 2));
  for (i = 2; i < argc; i++) {
    num = atoi(argv[i]);
    printf("%d ", num);
    *(numbers + i - 2) = num;
    if (!(i == argc - 1)) {
      printf("or ");
    }
  }
  printf("is %d.\n", sumMultiples(max, numbers, argc - 2));
  return 0;
}

int sumMultiples(int max, int *num1, int len) {
  int sum = 0;
  int i, j;
  for (i = 0; i < max; i++) {
    for (j = 0; j < len; j++) {
      if (!(i % num1[j])) {
        sum += i;
        break;
      }
    }
  }
  return sum;
}
