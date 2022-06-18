binary_sequence = input().split(',')

# Divisible by 5, with 4 digit binary sequence, only 0101 is divisible by 5

matching_sequences = []

for sequence in binary_sequence:
    representation_in_mod_10 = int(sequence, 2)

    if not representation_in_mod_10 % 5:
        matching_sequences.append(sequence)


print(','.join(matching_sequences))

