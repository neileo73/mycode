#!/usr/bin/python3

import csv
import json

def main():
    jsonf = open('superbirths.json', 'w')

    # open our cvs file to read in csv to python format
    with open('superbirths.csv') as csvf:
        reader = csv.DictReader(csvf)
        # for row in reader:
        json.dump(list(reader), jsonf)

    jsonf.close() # close the superbirths.json file we opened


if __name__ == "__main__":
    main()


