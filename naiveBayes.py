import math
import collections

def prior(value):
    prior = []
    counter = collections.Counter(value)
    label = list(counter.values())
    for i in range(len(label)):
        prior.append(label[i]/len(value))
    return prior
