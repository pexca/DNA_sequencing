import random

seq = ''
for _ in range(10):
    seq += random.choice('ACTG')
print(seq)

seq2 = ''.join([random.choice('ACTG') for _ in range(10)])
print(seq2)