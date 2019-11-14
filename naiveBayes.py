import math
import collections

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