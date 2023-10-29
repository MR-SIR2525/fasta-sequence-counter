def read_sequences(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
        sequences = [content[i:i+20] for i in range(0, len(content), 20)]
        return sequences

def count_occurrences(sequences, filename):
    with open(filename, 'r') as file:
        content = file.read()
        counts = {seq: content.count(seq) for seq in sequences}
        return counts

def write_output(counts, output_filename):
    with open(output_filename, 'w') as file:
        for seq, count in counts.items():
            file.write(f"{seq}: {count}\n")

def main():
    sequences = read_sequences("Salmon.txt")
    print(f'Read the sequences')
    counts = count_occurrences(sequences, "SRR13259952.fasta")
    write_output(counts, "output.txt")
    print("Tried to write to output.txt")

if __name__ == "__main__":
    main()
