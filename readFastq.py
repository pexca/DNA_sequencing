import matplotlib.pyplot as plt
import collections


def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fhand:
        while True:
            fhand.readline()  # skip name line
            seq = fhand.readline().rstrip()  # read base sequence
            fhand.readline()  # skip placeholder line
            qual = fhand.readline().rstrip()  # read base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    fhand.close()
    return sequences, qualities


seqs, quals = readFastq('SRR835775_1.first1000.fastq')
# print(quals[:5])
# print(seqs[:5])


def phred33toQ(qual):  # converts ASCII-symbol to quality value
    return ord(qual) - 33  # coverts a character to its ASCII-value, an integer


phred33toQ('#')
phred33toQ('J')


def createHist(qualities):  # pass list of qualities' strings
    hist = [0] * 50  # keep track of the frequency of each quality score
    for qual in qualities:
        for phred in qual:
            q = phred33toQ(phred)  # now we have a number, associated with quality score in that position
            hist[q] += 1  # increment that value in the histogram
    return hist

h = createHist(quals)
# print(sorted(h))

plt.bar(range(len(h)), h)
# plt.show()
#  the y-values are values of the histogram, the x-values are numbers from 0 up to the length of the hist

# plot the GC-content at each position in the read to see whether the mix of different bases is changing as we move
# along the read - there should be no significant spikes of GC-content in quality reads


def findGCbyPosition(reads):
    gc = [0] * 100
    totals = [0] * 100

    for read in reads:
        for i in range(len(read)):
            if read[i] == 'G' or read[i] == 'C':
                gc[i] += 1
            totals[i] += 1

    for i in range(len(gc)):
        if totals[i] > 0:
            gc[i] /= float(totals[i])

    return gc

gc = findGCbyPosition(seqs)
plt.plot(range(len(gc)), gc)
# plt.show()

# the distribution of bases in these sequences:

count = collections.Counter()
for seq in seqs:
    count.update(seq)
# print(count)  # where 'N' means that the base caller has zero confidence and doesn't make a call

