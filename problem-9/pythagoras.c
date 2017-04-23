/* Chris Milson March 2017
** A Pythagorean triplet is a set of three natural numbers, a < b < c, for
* which, a^2 + b^2 = c^2.
*
* For example, 32 + 42 = 9 + 16 = 25 = 52.
*
* There exists exactly one Pythagorean triplet for which a + b + c = 1000.
* Find the product abc.
*
* Answer a = 375, b = 200, c = 425.
* abc = 31,875,000.
*/

/*
** I decided that I will use Euclid's method of forming pythagorean triples,
* specifically, for any two integers m > n > 0 the following is a Pythagorean
* triple:
*
*   m^2 - n^2, 2mn, m^2 + n^2
*
* "Every primitive triple arises (after the exchange of a and b, if a is even)
* from a unique pair of coprime numbers m, n, one of which is even. It follows
* that there are infinitely many primitive Pythagorean triples."
* - Joyce, D. E. (June 1997), "Book X , Proposition XXIX", Euclid's Elements
*
* So it remains only for me to produce pairs of integers, so I need to make a
* pairing function for natural numbers and then check whether the triple they
* make with Euclid's method (or multiples) form the triple that satisfies the
* original question.
*/

#include <stdio.h>
#include <stdlib.h>

#define TARGET 1000

int pair(int, int *, int *);

int main(int argc, const char **argv) {
  int a, b;

  int i;
  for (i = 0; i < TARGET; i++) {
    pair(i++, &a, &b);
    if (!checkEuclideanTriple(a, b, TARGET)) return 0;
  }

  return 0;
}

int checkEuclideanTriple(const int m, const int n, const int target) {
  if (m <= n) return 1;
  int a = m*m - n*n;
  int b = 2 * m * n;
  int c = m*m + n*n;
  // We know this is a pythagorean triple from Euclid's theorem.
  // Now we need to check that their sum is equal to the target.

  int k = 1;
  while (k*a + k*b + k*c <= target) {
    if (k*a + k*b + k*c == target) {
      printf("\nThe triple %d, %d, %d is pythagorean ", k*a, k*b, k*c);
      printf("since %d^2 + %d^2 = %d + %d ", k*a, k*b, k*k*a*a, k*k*b*b);
      printf("= %d = %d^2\n", k*k*a*a + k*k*b*b, k*c);
      printf("Also, %d + %d + %d = %d.\n", k*a, k*b, k*c, target);
      printf("And %d * %d * %d = %d\n\n", k*a, k*b, k*c, k*k*k*a*b*c);
      // printf("The pair was %d, %d and k was %d\n\n", m, n, k);
      return 0;
    }
    k++;
  }
  return 1;
}

/* Takes an integer as an input and returns a unique pair of integers.
** Also, for every pair of positive integers there will be a unique integer
* that produces that pair with this function.
*/
int pair(int input, int *a, int *b) {
  int smallestTriangle = 0;
  while (triangle(++smallestTriangle) <= input);
  *a = triangle(smallestTriangle) - input;
  *b = smallestTriangle - *a + 1;
  return 0;
}

/* Returns the triangle number of 'number' */
int triangle(int number) {
  return ((number + 1) * number) / 2;
}
