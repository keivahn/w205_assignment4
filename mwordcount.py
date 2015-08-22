#!/usr/bin/env python

# Alex Smith
# MIDS W205
# Assignment #4

import csv      # import the CSV module to work with the CSV file of tweets

CSV_FILE_NAME = "tweets\WC2015.csv"    # name of CSV file
TEXT_INDEX = 4                         # text index in CSV file

# open the CSV file
filename = open(CSV_FILE_NAME,"r")
filename = csv.reader(filename)

# iterate through each line in the CSV file
for line in filename:

    # grab the text field in each line
    text = line[4]

    # split the text field into separate words using spaces
    words = text.split()

    # iterate through each word and print it with the number 1 following
    for word in words:
        print word + "\t" + str(1)
