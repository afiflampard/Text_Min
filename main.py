import pandas as pd
import numpy as np
import csv
import string
import preprocessing as pre
import tfidf as weighting
import openpyxl
import re
import naiveBayes as naive

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

def getValue(document):
    value =[]
    for i in range(len(document)):
        for j in range(len(document[i])):
            value.append(document[i][j][-1:])
    return value

f = open('stopword.txt', 'r')
content = f.read()
spl = content.rstrip()
stop = spl.split()

read = read_file("komentar.xlsx")
#print(read)
valueClass = getValue(read)
kelas = list(map(int,valueClass))
print(kelas)

# Hapus Tanda Baca
cleaner = clean(read)
print('Cleaner : ',cleaner)
print("\n")
#Filtering (menghapus kata tidak penting)
tokenization = pre.tokenization(cleaner)
print('Tokenization',tokenization)
filtering = pre.filtering(tokenization,stop)
removing = pre.remove(filtering)
print('Removing : ',removing)
print("\n")
#Stemming (Jadi kata dasar)
stemming = pre.stemming(removing)
print('Stemming :',stemming)
print("\n")
#Term hasil preprocessing
term = pre.term(stemming)
print('Term :',term)

#TF IDF
binary = weighting.binaryWeighting(stemming,term)
print("\nBinary Weighting:",binary)
raw = weighting.rawWeighting(stemming,term)
print("\nRaw Weighting:",raw)
log = weighting.logFrequency(raw)
print("\nLog Frequency:",log)
DF = weighting.docFrequency(binary)
print("\nDocument Frequency:",DF)
IDF = weighting.idf(DF,cleaner)
print("\nInverse Document Frequency :",IDF)
hasil_tfidf = weighting.TFIDF(log, IDF)
print("\ntf-idf:",hasil_tfidf)


prior = naive.prior(kelas)
print(prior)
