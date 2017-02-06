def longestCommonString(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    print(s1[:i])


def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t
