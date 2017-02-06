def readGenome(filename):
    with open(filename, 'r') as f:
        genome = ''
        for line in f:
            if not line.startswith('>'):
                genome += line.rstrip()
        counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        for base in genome:
            counts[base] += 1
    f.close()
    # print(genome[:100])
    # print(len(genome))
    # print(counts)
    return genome

genome = readGenome('lambda_virus.fa')


# or:
# import collections
# collections.Counter(genome)
# the enzyme that attaches the corresponding molecule to the base is called DNA-polymerase ('incorporates complementary
# bases, making a single-stranded template into a double-stranded molecule')

