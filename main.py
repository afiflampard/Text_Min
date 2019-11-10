import pandas as pd
import numpy as np
import csv
import string
import preprocessing as pre
import openpyxl
import re

def read_file(filename):
    wb_obj = openpyxl.load_workbook(filename)
    sheet_obj = wb_obj.active 
    m_row = sheet_obj.max_row 
    temp = [] 
    for i in range(1, m_row + 1): 
        cell_obj = sheet_obj.cell(row = i, column = 1) 
        temp.append(cell_obj.value.split("\n"))
    return temp


def clean(document):
    doc = []
    translator = str.maketrans('','',string.punctuation)
    for i in range(len(document)):
        temp = []
        for j in range(len(document[i])):
            document[i][j] = document[i][j].translate(translator)
            document[i][j] = re.sub(r'\d+', '', document[i][j])
            temp.append(document[i][j])
        doc.append(temp)
    return doc


f = open('stopword.txt', 'r')
content = f.read()
spl = content.rstrip()
stop = spl.split()

read = read_file("komentar.xlsx")
cleaner = clean(read)
print(cleaner)
print("\n")
preprocessing = pre.tokenization(cleaner)
filtering = pre.filtering(preprocessing,stop)
removing = pre.remove(filtering)
print(removing)
print("\n")
stemming = pre.stemming(removing)
print(stemming)
print("\n")
term = pre.term(stemming)
print(term)




