import numpy


# Document class for saving term frequencies and document classification
class Document:
    def __init__(self, term_frequencies, classification):
        self.frequencies = term_frequencies
        self.classification = classification