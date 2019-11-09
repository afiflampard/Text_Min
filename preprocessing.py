from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()


def tokenization(document):
    documents = []
    for i in range(len(document)):
        for j in range(len(document[i])):
            rep = document[i][j].replace(","," ")
            spl = rep.lower().split(" ")
            documents.append(spl)
    return documents

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

