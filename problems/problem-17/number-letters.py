""" Chris Milson May 2017
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.

Answer : 21124
"""

# you may need to install inflect
import inflect

start = 1
end = 1000

def count_letters(number_in_words):
    letters = 0
    for word in number_in_words.split():
        # print(word)
        letters += len(word)
        letters -= word.count("-") # this caused me some strife.
    # print("")
    return letters

p = inflect.engine()
letter_sum = 0;

for i in range(start, end + 1):
    letter_sum += count_letters(p.number_to_words(i))

string = "The number of letters you would need to write the numbers from "
string += str(start) + " to " + str(end) + " is " + str(letter_sum)
print(string)
