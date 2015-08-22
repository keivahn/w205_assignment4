#!/usr/bin/env python

# Alex Smith
# MIDS W205
# Assignment #4

import sys          # import the system module to read from the console

MINIMUM = 10000     # the minimum number of word count that is acceptable

def wcount(prev_word,counts):
    """method to count based on the previous word"""

    # if the previous word has been assigned print the word and its associated count
    if prev_word is not None:

        # only print the count if meets the minimum we have set
        if count >= MINIMUM:
            print prev_word + " count is " + str(count)

prev_word = None
count = 0

# iterate through the lines outputed by the map function
for line in sys.stdin:
    # read in the tuple, splitting by the tab character
    word, value = line.split("\t",1)

    # if the word is different than the previous word
    if word != prev_word:
        # count the previous word
        wcount(prev_word,counts)

        # set the previous word to the current word and return the count to 0
        prev_word = word
        count = 0
    # increment the count by the value next the word, in this case 1
    count = count + eval(value)

# make sure to count the last word
wcount(prev_word,count)
