# This script will read through an existing csv file, then write specific information to a brand new file.
# Very useful if you need to break up a master csv/excel file instead of using filters.

#!/usr/bin/python

import csv, sys

# CSV filename that will be read.
file1 = "blah.csv"

# Column keys from file1.
dict = {
    "A",
    "B",
    "C"
}

# Open file1 with the DictReader in read-only mode.
with open(file1, "r") as f1:
    reader = csv.DictReader(f1)

    try:

# Create a CSV file for each key in the dict dictionary.
        print("Creating individual files...")
        for id in dict:
            f2 = open(id + ".csv", "w+")
            f2.close()

# For each file previously created, strip any commas (,) from the specified column, then write the format to the file.
        for row in reader:
            for id in dict:
                print("Writing to... " + id + ".csv")
                f2 = open(id + ".csv", "a")
                strip_a = row["col1_name"]
                strip_a = strip_a.replace(",","")
                f2.write(row["column_name"] + "," + strip_a)
                f2.close()

# Error catching.
    except csv.Error as e:
        sys.exit("file %s, line %d: %s" % (file1, reader.line_num, e))

f1.close()
