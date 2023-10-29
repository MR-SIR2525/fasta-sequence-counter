import collections
from Bio import SeqIO

# Function to create unique 20-nucleotide sequences with a sliding window
def find_unique_sequences(sequence, length=20):
    seen_sequences = set()
    for i in range(len(sequence) - length + 1):
        sub_sequence = sequence[i:i + length]
        if sub_sequence not in seen_sequences:
            seen_sequences.add(sub_sequence)
            yield sub_sequence

# Function to count the occurrences of unique sequences in another sequence
def count_sequence_occurrences(unique_sequences, sequence):
    sequence_counter = collections.Counter(unique_sequences)
    for subseq in sequence_counter:
        sequence_counter[subseq] = sequence.count(subseq)
    return sequence_counter

# Prompt the user to enter the input file names
unique_sequence_file = input("Enter the input file name with unique sequences: ")
# counting_sequence_file = input("Enter the input file name to count sequences from: ")
counting_sequence_file = "SRR13259952.fasta"
print(f"Processing file set to: {counting_sequence_file}")

# Read the unique sequences from the first file and create a generator
with open(unique_sequence_file, 'r') as file:
    sequence = file.read().strip()
    unique_sequences = list(find_unique_sequences(sequence))

# Initialize a counter for the sequences
total_sequence_counter = collections.Counter()

# Read the sequence from the second file (FASTA format) using Biopython
for record in SeqIO.parse(counting_sequence_file, "fasta"):
    print(f"Processing record: {record.id}")
    sequence = str(record.seq)
    sequence_counter = count_sequence_occurrences(unique_sequences, sequence)
    total_sequence_counter += sequence_counter

# Print final counts
with open("output.txt", "w") as output_file:
    for seq, count in total_sequence_counter.items():
        output_file.write(f"{seq}: {count}")

    print(f"Text file '{output_file.name}' has been created with the unique sequence occurrences.")
