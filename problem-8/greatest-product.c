/* Chris Milson March 2017
** The four adjacent digits in the 1000-digit number that have the greatest
* product are 9 × 9 × 8 × 9 = 5832.
*
* 73167176531330624919225119674426574742355349194934
* 96983520312774506326239578318016984801869478851843
* 85861560789112949495459501737958331952853208805511
* 12540698747158523863050715693290963295227443043557
* 66896648950445244523161731856403098711121722383113
* 62229893423380308135336276614282806444486645238749
* 30358907296290491560440772390713810515859307960866
* 70172427121883998797908792274921901699720888093776
* 65727333001053367881220235421809751254540594752243
* 52584907711670556013604839586446706324415722155397
* 53697817977846174064955149290862569321978468622482
* 83972241375657056057490261407972968652414535100474
* 82166370484403199890008895243450658541227588666881
* 16427171479924442928230863465674813919123162824586
* 17866458359124566529476545682848912883142607690042
* 24219022671055626321111109370544217506941658960408
* 07198403850962455444362981230987879927244284909188
* 84580156166097919133875499200524063689912560717606
* 05886116467109405077541002256983155200055935729725
* 71636269561882670428252483600823257530420752963450
*
* Find the thirteen adjacent digits in the 1000-digit number that have the
* greatest product. What is the value of this product?
*
* Answer: 23514624000
* (The digits were 5 5 7 6 6 8 9 6 6 4 8 9 5)
*/

/*
** I realised I do not have to check the product at any point. All I have to do
* is check whether the next number I will add is more than the number I will be
* removing.
* I put the number in a text document alongside so that I can try to deal with
* it more efficiently.
*
* What I initially thought about not having to check the product was wrong.
* Since I replace every number in the "largest" array based on whether the
* current number I am looking at is larger than the last, My assumption breaks
* down. I only know if the product directly after the current one is larger,
* beyond that I cannot know without calculating the product.
*
* I got very close, but needed to change from integer to unsigned long so that
* the overflow from integer was avoided.
*/

#include <stdio.h>
#include <stdlib.h>

#define NUMBER_CONSECUTIVE 13

unsigned long product(unsigned long*);

int main(int argc, char **argv) {
  unsigned long nextAdded;
  FILE *numFile = fopen("./problem-8/number.txt", "rb");
  if(!numFile) {
    perror("File opening failed");
    return EXIT_FAILURE;
  }

  unsigned long currentCheck[NUMBER_CONSECUTIVE];
  unsigned long currentLargest[NUMBER_CONSECUTIVE];

  int i;
  for (i = 0; i < NUMBER_CONSECUTIVE; i++) {
    currentCheck[i] = currentLargest[i] = 0;
  }

  i = 0;
  while ((nextAdded = fgetc(numFile)) != EOF) {
    if(nextAdded == '\n') continue;
    nextAdded -= 48; // normailise between character and integer.
    currentCheck[i] = nextAdded;
    if (product(currentCheck) > product(currentLargest)) {
      copyArray(currentCheck, currentLargest, NUMBER_CONSECUTIVE, i);
    }
    i = (i + 1) % NUMBER_CONSECUTIVE;
  }

  printf("The numbers were ");
  for (i = 0; i < NUMBER_CONSECUTIVE; i++) {
    printf("%lu ", currentLargest[i]);
  }
  printf("and their product is %lu.", product(currentLargest));

  printf("\n");
  fclose(numFile);
  return 0;
}

unsigned long product(unsigned long *array) {
  int i;
  unsigned long product = 1;
  for (i = 0; i < NUMBER_CONSECUTIVE; i++) {
    product *= array[i];
  }
  return product;
}

int copyArray(unsigned long *from, unsigned long *to, int length, int index) {
  int i;
  for (i = 0; i < length; i++) {
    to[i] = from[(i + index + 1) % length];
    // add one since index is the last number to be entered.
  }
  return 0;
}
