from naive import naive
import random
from naive import genome


# generate reads by taking subsequences from random positions in the given genome
def generateReads(genome, numReads, readLen):
    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome) - readLen) - 1
        reads.append(genome[start:start+readLen])
    return reads

reads = generateReads(genome, 100, 100)
numMatched = 0
for pattern in reads:
    matches = naive(pattern, genome)
    if len(matches) > 0:
        numMatched += 1
print('%d/%d matched exactly' % (numMatched, len(reads)))
