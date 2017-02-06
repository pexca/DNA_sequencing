from readGenome import readGenome
from readFastq import readFastq
from seqfunc import reverseComplement
from timeit import timeit

genome = readGenome('phix.fa')


def naive(pattern, text):
    occurences = []
    for i in range(len(text) - len(pattern) + 1):  # loop over alignments
        match = True
        for j in range(len(pattern)):  # loop over characters
            if text[i+j] != pattern[j]:
                match = False
                break
        if match:
            occurences.append(i)
    # print(occurences)
    return occurences

phix_reads, _ = readFastq('ERR266411_1.first1000.fastq')  # no need to return qualities, therefor lower space


def finalFunc(numMatched, n):
    # numMatched = 0
    # n = 0  # count total number of reads that we've processed

    for read in phix_reads:
        read = read[:30]  # take only first 30 bases
        matches = naive(read, genome)
        matches.extend(naive(reverseComplement(read), genome))
        n += 1
        if len(matches) > 0:
            numMatched += 1
    print('%d/%d reads matched the genome!' % (numMatched, n))

print(timeit(lambda: finalFunc(0, 0), number=1))
