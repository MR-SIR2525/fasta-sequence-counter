import collections
from Bio import SeqIO
import itertools

def find_unique_sequences(sequence, length=20):
    seen_sequences = set()
    for i in range(len(sequence) - length + 1):
        sub_sequence = sequence[i:i + length]
        if sub_sequence not in seen_sequences:
            seen_sequences.add(sub_sequence)
            yield sub_sequence

def count_sequence_occurrences(unique_sequences, sequence):
    sequence_counter = collections.Counter(unique_sequences)
    for subseq in sequence_counter:
        sequence_counter[subseq] = sequence.count(subseq)
    return sequence_counter

def process_records(records, unique_sequences):
    sequence_counter = collections.Counter()
    for record in records:
        print(f"Processing record: {record.id}")
        sequence = str(record.seq)
        sequence_counter += count_sequence_occurrences(unique_sequences, sequence)
    return sequence_counter

# Prompt the user to enter the input file names
unique_sequence_file = input("Enter the input file name with unique sequences: ")
counting_sequence_file = "SRR13259952.fasta"
print(f"Processing file hard coded: {counting_sequence_file}.")
batch_size = 250000

# Read the unique sequences from the first file and create a generator
with open(unique_sequence_file, 'r') as file:
    sequence = file.read().strip()
    unique_sequences = list(find_unique_sequences(sequence))

# Initialize a counter for the sequences
total_sequence_counter = collections.Counter()

# Read the sequence from the second file (FASTA format) using Biopython
record_generator = SeqIO.parse(counting_sequence_file, "fasta")
if not record_generator:
    print(f"Failed to parse file: {counting_sequence_file}.")

while True:
    # Process records in batches
    print("Entered the while loop.")
    records = list(itertools.islice(record_generator, batch_size))
    print(f"Records length = {len(records)}.")
    if not records:
        break
    total_sequence_counter += process_records(records, unique_sequences)


# Print final counts
with open("output.txt", "w") as output_file:
    for seq, count in total_sequence_counter.items():
        output_file.write(f"{seq}: {count}")

    print(f"Attempted to create '{output_file.name}'.")