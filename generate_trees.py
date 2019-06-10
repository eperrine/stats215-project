from random import randint, random
import math

alphabet = ('A', 'C', 'T', 'G')
alphabet_len = len(alphabet)
max_num_taxa = 50
seq_len = 20
initial_seq = [randint(0, alphabet_len - 1) for i in range(seq_len)]
tree = [initial_seq]
mu = 0.1

def generate_mutations(seq):
    mutated_seq = seq.copy()
    num_mutations = len(seq)
    for i, char in enumerate(mutated_seq):
        mutate_prob = 0.25 - 0.25 * math.exp(-1 * mu)
        p = random()
        if p < mutate_prob:
            mutated_seq[i] = (char + 1) % alphabet_len
        elif p < 2 * mutate_prob:
            mutated_seq[i] = (char + 2) % alphabet_len
        elif p < 3 * mutate_prob:
            mutated_seq[i] = (char + 3) % alphabet_len
        else:
            num_mutations -= 1
    return (mutated_seq, num_mutations)

while len(tree) < max_num_taxa:
    mutations = []
    for seq in tree:
        mutated_seq, num_mutations = generate_mutations(seq)
        if num_mutations > seq_len / 10:
            mutations.append(mutated_seq.copy())
        else:
            seq = mutated_seq.copy()
    tree.extend(mutations)

for i, seq in enumerate(tree):
    print('>unknown %d' % i)
    print(''.join([alphabet[i] for i in seq]))
