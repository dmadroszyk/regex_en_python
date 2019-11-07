#!/usr/bin/env python3

import sys
import re
import codecs
import xlrd
import csv

WordFreq = {"rappel": 1, "ai pris": 1,
            "ai fait": 1, "je viens de faire": 1,
            "je suis vacciné": 1, "je me suis vaccin" : 1,
            "je vais faire" : 1, "je vais prendre" : 1}

def open_csv(file):
    inputFile = open(file, "r+", encoding="Latin1")
    csvReader = csv.reader(inputFile, dialect='excel')
    for row in csvReader:
        print(row)

def test_occurence(cols):
    score = 0
    reg =  r'\b(?:rappel|j\'ai pris|j\'ai fait|je me suis vaccine|je vais faire|je vais prendre)\b'
    res = re.findall(reg, cols)
    if res != []:
        print(res)
        score = 1
    return score

def open_xlsx(file):
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)
    for rowx in range(sheet.nrows):
        cols = sheet.row_values(rowx)
        cols[3].lower()
        if test_occurence(cols[3]) == 1:
            print(cols[3])

def main():
    if len(sys.argv) != 2:
        print ("Usage: ./ia <doc.csv>/<doc.xlsx")
        exit(84)
    try:
        if ".csv" in sys.argv[1]:
            open_csv(sys.argv[1])
        elif ".xlsx" in sys.argv[1]:
            open_xlsx(sys.argv[1])
    except:
        print("not a valid file")

if __name__ == "__main__":
    main()