import math

#x = array hasil filtering
#term = array hasil preprocessing

#Binary Weighting
bin=[]
def binaryWeighting(x,term):
    for i in range(len(x)):
        bin.append([])
        for k in term:
            if k in x[i]:
                bin[i].append(1)
            else:
                bin[i].append(0)
    return bin

#Raw Weighting
def count(term, array):
    n=0
    for x in array:
        if x== term:
            n+=1
    return n


def rawWeighting(document, term):
    doc = []
    for i in range(len(document)):
        word = []
        for j in range(len(term)):
            word.append(document[i].count(term[j]))
        doc.append(word)
    return doc

#Log Frequency Weighting
#array = array hasil raw weighting
log=[]
def logFrequency(array):
    for x in range(len(array)):
        log.append([])
        for y in range(len(array[x])):
            if array[x][y] == 0:
                log[x].append(0)
            else:
                z = 1 + math.log(array[x][y], 10);
                log[x].append(z)
    return(log)
    
#Document Frequency 
df=[]
def docFrequency(array):
    for x in range(len(array[0])):
        temp=0
        for y in range(len(array)):
            temp+=array[y][x]
        df.append(temp)
    return df

#Inverse Document Frequency
def idf(hasilBinary, array_hasil):
    idf=[]
    for x in range(len(hasilBinary)):
        temp=len(array_hasil)/hasilBinary[x]
        temp2=math.log(temp, 10)
        idf.append(temp2)
    return idf

#Term Frequency Inverse Document Frequency
tfidf=[]
def TFIDF(log, idf):
    for x in range(len(log)):
        tfidf.append([])
        for y in range(len(log[x])):
            tfidf[x].append(log[x][y]*idf[y])
    return tfidf