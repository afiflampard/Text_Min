import numpy as np
import string
import preprocessing as pre
import tfidf as weighting
import re
import naiveBayes as naive
import csv

def openFile(file):
    data=[]
    readCSV = csv.DictReader(open(file), delimiter=";")
    for row in readCSV:
        data.append(row)
    return data

def teks(data):
    dataTeks=[]
    for row in data:
        dataTeks.append(row['Teks'])
    return dataTeks

def teksDanKelas(data):
    teksDanKelas=[[],[]]
    for row in data:
        teksDanKelas[0].append(row['Teks'])
        teksDanKelas[1].append(row['Kelas'])
    return teksDanKelas

def kelas(data):
    kelas=[]
    for row in data:
        kelas.append(row['Kelas'])
    return kelas

def nkelas(kelas):
    nkelas=[]
    for i in range(len(kelas)):
        if kelas[i] not in nkelas:
            nkelas.append(kelas[i])
    return nkelas

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

def akurasi(OriginalTeks,decision):
    count = 0
    total = 0
    for i in range(0,len(OriginalTeks)):
        if OriginalTeks[i] == decision[i]:
            count += 1
    total = (count/len(OriginalTeks)) * 100
    return total

f = open('stopword.txt', 'r')
content = f.read()
spl = content.rstrip()
stop = spl.split()

read = openFile("Training2.csv")
openTeks = teks(read)

kelas = kelas(read)
kelas1 = list(map(int,kelas))

#Ambil Teks Dan Kelas Array 2D dari Data Original
readOriginal = openFile("komentar.csv")
teksDanKelas = teksDanKelas(readOriginal)

text = teksDanKelas[0]
kelasOrigin = teksDanKelas[1]
kelasOriginint = list(map(int,kelasOrigin))


textToken = pre.Tokensisasi(text)

preprocessing = pre.Tokensisasi(openTeks)
lower = pre.lowerCase(preprocessing)
filtering = pre.filtering(lower,stop)
stemming = pre.stemming(filtering)
term = pre.term(stemming)
count_term = len(term)

raw = weighting.rawWeighting(stemming,term)

gabung = zip(kelas1,raw)
gabung1 = zip(kelas1,raw)

valueKelas1 = []
valueKelas0 = []
for i in gabung1:
    if i[0]==0:
        valueKelas0.append(i[1])
    else:
        valueKelas1.append(i[1])
        
sumValueKelas0 = []        
sumValueKelas1 = []
if len(valueKelas1) == 0:
    sumValueKelas1 = []
else:
    for i in range(0,len(valueKelas1[0])):
        countValueKelas1=0
        for j in range(0,len(valueKelas1)):
            countValueKelas1+=valueKelas1[j][i]
        sumValueKelas1.append(countValueKelas1)

if len(valueKelas0) == 0:
    sumValueKelas0 = []
else:
    for i in range(0,len(valueKelas0[0])):
        countValueKelas0=0
        for j in range(0,len(valueKelas0)):
            countValueKelas0+=valueKelas0[j][i]
        sumValueKelas0.append(countValueKelas0)  

count_dokumen = []
for tup in gabung:
    count_dokumen.append(sum(tup[1]))
count_setiap_dokumen = zip(kelas1,count_dokumen)
countPerKelas = naive.countKelas(count_setiap_dokumen)

peluang0 = naive.peluang0(sumValueKelas0,countPerKelas,count_term)
peluang1 = naive.peluang0(sumValueKelas1,countPerKelas,count_term)

prior = naive.prior(kelas)

dataT = openFile("Testing2.csv")
openTeksT = teks(dataT)

preprocessingT = pre.Tokensisasi(openTeksT)
lowerT = pre.lowerCase(preprocessingT)
filteringT = pre.filtering(lowerT,stop)
stemmingT = pre.stemming(filteringT)

penampung = []
for i in range(0,len(preprocessingT)):
    for j in range(0,len(textToken)):
        if preprocessingT[i] == textToken[j]:
            penampung.append(j)
            break
        
kelasOriginal = []
for i in range(0,len(penampung)):
    kelasOriginal.append(kelasOriginint[penampung[i]])
        
rawDataT = weighting.rawWeighting(stemmingT,term)

likelihoodT = naive.likelihood(rawDataT,peluang0,peluang1,prior)
print('Decision',likelihoodT)

akurasiTot = akurasi(kelasOriginal,likelihoodT)

positiveNegative=[]
for i in range(len(likelihoodT)):
    if likelihoodT[i]==0:
        positiveNegative.append("Negative")
    else:
        positiveNegative.append("Positive")

print('positiveNegative',positiveNegative)

print('Akurasi = ',akurasiTot)