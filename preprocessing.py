from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

factory = StemmerFactory()
stemmer = factory.create_stemmer()


def Tokensisasi(documents):
    #Tokensisasi
    tokenized=[]
    for i in range(len(documents)):
        documents[i] = re.sub(r'[^\w\s]','',documents[i])
    for i in range(len(documents)):
        documents[i] = re.sub(r'[\d]','',documents[i])
    for i in range(len(documents)):
        x=documents[i].split()
        tokenized.append(x)   
    return tokenized

def lowerCase(document):
    doc = []
    for i in range(len(document)):
        temp = []
        for j in range(len(document[i])):
            temp.append(document[i][j].lower())
        doc.append(temp)
    return doc

def filtering(document, stop):
    doc = []
    for documents in document:
        word = []
        for temp in documents:
            if temp not in stop:
                word.append(temp)
        doc.append(word)
    return doc



def remove(document):
    doc = []
    for documents in document:
        rem = list(filter(None,documents))
        doc.append(rem)
    return doc

def stemming(document):
    doc = []
    for documents in document:
        word = []
        for temp in documents:
            word.append(stemmer.stem(temp))
        doc.append(word)
    return doc

def term(document):
    doc = []
    for documents in document:
        for word in documents:
            if word not in doc:
                doc.append(word)

    return doc

