seq1 = 'atgcttcggcaagactcaaaaaaata'
seq2 = 'atgcttcggcaagactaaaaaaaata'

zip_seqs = zip(seq1,seq2)

#print(list(enum_seqs))

enum_seqs = enumerate(zip_seqs)

for i, (a,b) in enum_seqs:
    if a != b:
        print(f'index: {i}')