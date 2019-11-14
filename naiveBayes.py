import math
import collections

def multiplyList(myList):
    result=1
    for x in myList:
        result=result*x
    return result

def prior(value):
    prior = []
    counter = collections.Counter(value)
    label = list(counter.values())
    for i in range(len(label)):
        prior.append(label[i]/len(value))
    return prior

def gabung(kelas,raw):
    return zip(kelas,raw)
    
    
def countKelas(count_setiap_dokumen):
    listKelas = []
    class0 = 0
    class1 = 0
    for kelas,jumlah in count_setiap_dokumen:
        if kelas==0:
             class0 +=jumlah
        elif kelas==1:
            class1 +=jumlah
    listKelas.append(class0)
    listKelas.append(class1)
    return listKelas    

valueKelas1=[]
valueKelas0=[]
def memisahkanKelas(gabung):
    for i in gabung:
        if i[0] == 0:
            valueKelas0.append(i[1])
        elif i[0] == 1:
            valueKelas1.append(i[1])

def peluang0(sumValueKelas0,countKelas,panjangTerm):
    p0=[]
    pxa=0
    for i in range(len (sumValueKelas0)):
        pxa=(sumValueKelas0[i]+1)/(countKelas[0]+panjangTerm)
        p0.append(pxa)
    return p0
        
def peluang1(sumValueKelas1,countKelas,panjangTerm):
    p1=[]
    pxa=0
    for i in range(len (sumValueKelas1)):
        pxa=(sumValueKelas1[i]+1)/(countKelas[1]+panjangTerm)
        p1.append(pxa)
    return p1

def likelihood(rawData,peluang0,peluang1,prior):
    likelihood0 = []
    for i in range(0,len(rawData)):
        count = 0
        temp = []
        for j in range(0,len(rawData[i])):
            count = rawData[i][j] * peluang0[j]
            if count != 0:
                temp.append(count)
        likelihood0.append(temp)
        
    likelihood1 = []
    for i in range(0,len(rawData)):
        count = 0
        temp = []
        for j in range(0,len(rawData[i])):
            count = rawData[i][j] * peluang1[j]
            if count != 0:
                temp.append(count)
        likelihood1.append(temp)
    
    lkhood0Total=[]
    for i in range(len(likelihood0)):
        lkhood0Total.append(multiplyList(likelihood0[i]))
        
    lkhood1Total=[]
    for i in range(len(likelihood1)):
        lkhood1Total.append(multiplyList(likelihood1[i]))
      
    prior0xlikelihood0 = []
    for i in range(len(lkhood0Total)):
        prior0xlikelihood0.append(lkhood0Total[i]*prior[0])
    
    prior1xlikelihood1 = []
    for i in range(len(lkhood1Total)):
        prior1xlikelihood1.append(lkhood1Total[i]*prior[1])
    
    decision = []
    for i in range(0,len(prior0xlikelihood0)):
        if prior0xlikelihood0[i] > prior1xlikelihood1[i]:
            decision.append(0)
        else:
            decision.append(1)
    return decision
            
    
    