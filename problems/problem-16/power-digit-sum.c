/* Chris Milson May 2017
** Problem 16
*
* 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
*
* What is the sum of the digits of the number 2^1000?
*
* Answer :
*/

/*
** Firstly, this is a base 10 problem, so what it is really asking me to do is
* find the sum of a0 a1 a2 a3 a4... when
* a0 + a1 *10 + a2 *100 + a3 *1000 + ... = 2^1000
*
* also notice that
* a0 = 2^1000 % 10
* a1 = (2^1000 / 10) % 10
* a2 = (2^1000 / 100) % 10
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define BASE_A 2
#define BASE_B 10
#define POWER 10000

int main(int argc, char **argv) {
	const int SIZE = (int) (POWER * (log(BASE_A)/log(BASE_B)) + 1);
	char digits[SIZE]; // will be 1000 bytes large; not in excess of the
	// C standard requirement of 65,535 bytes.
	char carry[SIZE];
	int i, j;
	unsigned long long sum;
	int foundStart;

	for (i = 0; i < SIZE; i++) {
		carry[i] = 0;
		digits[i] = 0;
	}
	digits[0] = 1;

	for (i = 0; i < POWER; i++) {
		for (j = 0; j < SIZE; j++) {
			digits[j] *= BASE_A;
			if (j) {
				digits[j] += carry[j - 1];
				carry[j - 1] = 0;
			}
			if (digits[j] >= BASE_B) {
				carry[j] = digits[j] / BASE_B;
				digits[j] %= BASE_B;
			}
		}
	}

	sum = 0;
	i = 0;
	foundStart = 0;
	printf("%d^%d = ", BASE_A, POWER);
	for (i = SIZE - 1; i >= 0; i--) {
		if (!foundStart) {
			if (digits[i]) {
				foundStart = 1;
			} else {
				continue;
			}
		}
		printf("%d", digits[i]);
		sum += digits[i];
	}
	printf("\n");

	printf("The sum of the digits of %d^%d", BASE_A, POWER);
	printf(" in base %d is 1.\n", BASE_A);
	printf("The sum of the digits of %d^%d", BASE_A, POWER);
	printf(" in base %d is %llu.\n", BASE_B, sum);

	return 0;
}
