/* Chris Milson May 2017
** Problem 14
* The following iterative sequence is defined for the set of positive integers:
*
*   n → n/2 (n is even)
*
*   n → 3n + 1 (n is odd)
*
* Using the rule above and starting with 13 we generate the following sequence
*
*   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
*
* It can be seen that this sequence (starting at 13 and finishing at 1)
* contains 10 terms. Although it has not been proved yet (Collatz Problem),
* it is thought that all starting numbers finish at 1.
*
* Which starting number, under one million, produces the longest chain?
*
* Answer : 837799
* The length of the sequence was 524
*/

/* Firstly I will create a function the will advance the current number once
** along its Collatz "trajectory". Then I will go and count for each of the
* integers from 2 to 1 million.
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX 1000000

unsigned long long nextCollatz(unsigned long long number);

unsigned long long nextCollatz(unsigned long long n) {
  return (n % 2 ? 3 * n + 1 : n / 2);
}

#define NEXT_COLLATZ(n) n = (n % 2 ? 3 * n + 1 : n / 2)

int main(int argc, char **argv) {
  int current, largestNumber, largestSize = 0;
  int i;
  unsigned long long n;

  for (i = 2; i < MAX; i++) {
    n = i;
    current = 0;
    while (n != 1) {
      NEXT_COLLATZ(n);
      // doing it with a marco is slightly faster as there is not as much
      // overhead memory.
      // n = nextCollatz(n);
      current++;
    }
    if (current > largestSize) {
      largestSize = current;
      largestNumber = i;
    }
  }

  // Makes a file with the longest sequence in it.
  // FILE *f = fopen("sequence.txt", "w");
  // n = largestNumber;
  // while (n != 1) {
  //   fprintf(f, "%llu\n", n);
  //   NEXT_COLLATZ(n);
  // }
  // fclose(f);


  printf("\nThe number with the longest collatz sequence below");
  printf(" %d is %d with a length of %d\n\n", MAX, largestNumber, largestSize);

  return 0;
}
