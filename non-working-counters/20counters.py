import collections

# Function to create unique 20-nucleotide sequences with a sliding window
def find_unique_sequences(sequence, length):
    unique_sequences = []
    seen_sequences = set()
    for i in range(len(sequence) - length + 1):
        sub_sequence = sequence[i:i + length]
        if sub_sequence not in seen_sequences:
            seen_sequences.add(sub_sequence)
            unique_sequences.append(sub_sequence)
    return unique_sequences

# Function to count the occurrences of unique sequences in another sequence
def count_sequence_occurrences(unique_sequences, sequence):
    sequence_counter = collections.Counter()
    for unique_sequence in unique_sequences:
        sequence_counter[unique_sequence] = sequence.count(unique_sequence)
    return sequence_counter

# Prompt the user to enter the input file names
unique_sequence_file = input("Enter the input file name with unique sequences: ")
counting_sequence_file = input("Enter the input file name to count sequences from: ")

# Prompt the user to enter the output text file name
output_file_name = input("Enter the output text file name: ")

# Read sequences from the specified files
with open(unique_sequence_file, "r") as unique_file, open(counting_sequence_file, "r") as counting_file:
    unique_sequence = unique_file.read()
    counting_sequence = counting_file.read()

# Find unique 20-nucleotide sequences using a sliding window
unique_sequences = find_unique_sequences(unique_sequence, 20)

print(unique_sequences)

# exit()
# Count the occurrences of unique sequences in the counting_sequence
sequence_counter = count_sequence_occurrences(unique_sequences, counting_sequence)

# Write the unique sequences and occurrence counts to the text file
with open(output_file_name, "w") as output_file:
    for sequence in unique_sequences:
        output_file.write(f"{sequence}: {sequence_counter.get(sequence, 0)}\n")

    print(f"Text file '{output_file_name}' has been created with the unique sequence occurrences.")
