/* Chris Milson March 2017
** Problem 4:
* A palindromic number reads the same both ways. The largest palindrome made
* from the product of two 2-digit numbers is 9009 = 91 × 99.
*
* Find the largest palindrome made from the product of two 3-digit numbers.
*
* Answer: 906609.
*/

/* Note that I have assumed this problem to be base-10-centric.
** I will start with the two numbers both at 999. I will then decrent them in
* a smart way to make sure that their product is as large as possible. as soon
* as their product is a palindrome I can stop.
*/

#include <stdio.h>
#include <stdlib.h>
#define DIGITS 3
#define BASE 10

char* intToString(int, int);

int main(int argc, char **argv) {
  int num1, num2;
  int maxNum1, maxNum2;
  maxNum1 = maxNum2 = 0;
  const int MAX = powi(BASE, DIGITS);
  int i;

  // I started with this naiive approach and the below code is my improvement
  // for (num1 = 1; num1 < MAX; num1++) {
  //   for (num2 = num1; num2 < MAX; num2++) {
  //     if (isPalindrome(num1 * num2, BASE) && num1 * num2 > maxNum1 * maxNum2) {
  //       maxNum1 = num1;
  //       maxNum2 = num2;
  //     }
  //   }
  // }
  int isDone = 0;
  for (num1 = MAX - 1; num1 > 0; num1--) {
    for (num2 = MAX - 1; num2 >= num1; num2--) {
      if ((num2 * num2) * 2 < maxNum1 * maxNum2) {
        isDone = 1;
        break;
      }
      if (isPalindrome(num1 * num2, BASE) && num1 * num2 > maxNum1 * maxNum2) {
        maxNum1 = num1;
        maxNum2 = num2;
      }
    }
    if (isDone) break;
  }


  printf("\nThe largest palindrome that is made from the product of two ");
  printf("%d-digit numbers in base %d is %d.\n",DIGITS, BASE, maxNum1 * maxNum2);
  printf("The numbers were %d and %d.\n\n", maxNum1, maxNum2);
}

int isPalindrome(int number, int base) {
  // First I must work out the largest power of ten of the number.
  int largestPower = 0;
  while (powi(base, ++largestPower) <= number);

  int digit1, digit2;
  int i;
  for (i = 0; i < largestPower / 2; i++) {
    digit1 = digitInPlace(number, i + 1, base);
    digit2 = digitInPlace(number, largestPower - i, base);
    if (digit1 != digit2) {
      return 0;
    }
  }
  return 1;
}

/*
** Returns the value of the digit in the specified place in the specified base.
*/
int digitInPlace(int number, int place, int base) {
  return (number % powi(base, place)) / powi(base, place - 1);
}

int powi(int a, int b) {
  int answer = 1;
  int i;
  for (i = 0; i < b; i++) {
    answer *= a;
  }
  return answer;
}
