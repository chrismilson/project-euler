/* Chris Milson March 2017
** 2520 is the smallest number that can be divided by each of the numbers from
* 1 to 10 without any remainder.
*
* What is the smallest positive number that is evenly divisible by all of the
* numbers from 1 to 20?
*
* Answer: 232792560.
*/

/*
** First off it is obvious I dont have to check if a number is divisible by one.
* So what I will do is start with any two of the numbers and work out their
* lowest common multiple, set one of the numbers to this new number, and set
* the other number to the next number we are looking at.
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX 20

int main(int argc, char **argv) {
  int currentLCM = MAX;
  int i = 1;
  while (i < MAX) {
    currentLCM = lcm(MAX - i++, currentLCM);
  }

  printf("\nThe lowest common multiple of all the positive numbers less than ");
  printf("%d is %d\n\n", MAX, currentLCM);

  return 0;
}

/*
** Gets the lowest common multiple of two integers.
*/
int lcm(int num1, int num2) {
  // It will be nice to assume that num1 < num2.
  if (num1 > num2) {
    num1 ^= num2;
    num2 ^= num1;
    num1 ^= num2;
  }

  int answer = 1;
  int i;
  for (i = 2; i <= num1;) {
    if (!(num1 % i)) {
      answer *= i;
      num1 /= i;
      if (!(num2 % i)) {
        num2 /= i;
      }
    } else {
      i++;
    }
  }
  return answer * num2;
}
