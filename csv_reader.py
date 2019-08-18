#!/usr/bin/python

# This is a basic CSV Reader script.
# You must change the csv filename, and insert the title of each column that shows up in row 1 of the file.

import csv

with open('CSV_FILENAME.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    try:
        for row in reader:
            print(row['first_column_title'], row['second_column_title'], row['third_column_title'])
    except csv.Error as e:
        print(e)
