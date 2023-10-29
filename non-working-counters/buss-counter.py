import collections
from collections import defaultdict


def find_unique_sequences(sequence, k):
    unique_sequences = set()
    for i in range(len(sequence) - k + 1):
        subsequence = sequence[i:i+k]
        unique_sequences.add(subsequence)
    return unique_sequences


def compare_against_unique_sequences(unique_sequences, sequence, counts):
    for unique_sequence in unique_sequences:
        count = sequence.upper().count(unique_sequence.upper())
        counts[unique_sequence] += count


def write_output(counts, output_filename="output.txt"):
    with open(output_filename, 'w') as file:
        for seq, count in counts.items():
            file.write(f"{seq} {count}\n")
    print(f"Wrote {seq} {count} to {output_filename}")

def read_fasta_large(filename):
    counts = defaultdict(int)
    current_sequence = ""
    current_description = None
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_description:
                    compare_against_unique_sequences(current_description, current_sequence)
                current_description = line[1:]
                current_sequence = ""
            else:
                current_sequence += line
                
        if current_description:
            compare_against_unique_sequences(current_description, current_sequence)

    

if __name__ == "__main__":
    # declaring files to use
    unique_sequence_file = input("Enter the input file name with unique sequences: ")
    print(f"Ok. Unique sequences file set to: {unique_sequence_file}.")

    fasta_file = "SRR13259952.fasta"
    print(f"Using this fasta file: {fasta_file}.")
    print("\n**************\n")


    # Find the unique sequences
    with open(unique_sequence_file, 'r') as file:
        sequence = file.read().strip()
        
        k = 20 # length of the unique sequences
        unique_sequences = find_unique_sequences(sequence, k)
        # NOTE: We confirmed that these are good

    # reading and searching the fasta file via streaming
    read_fasta_large(fasta_file)

    # writing the output to file
    



# %% [markdown]
# ## These are the unique sequences in Salmon.txt
# {'AAGGtCGTAGGTTCGACTCC', 'CCGATATAGCTCAGTTGGTA', 'TAGCTCAGTTGGTAGAGCAG', 'ATGCGAAGGtCGTAGGTTCG', 'GGTTCGACTCCTATTATCGG', 'TCGACTCCTATTATCGGCAC', 'CGTAATGCGAAGGtCGTAGG', 'AGGtCGTAGGTTCGACTCCT', 'AGCGCATTCGTAATGCGAAG', 'CAGTTGGTAGAGCAGCGCAT', 'AGAGCAGCGCATTCGTAATG', 'CGATATAGCTCAGTTGGTAG', 'TCAGTTGGTAGAGCAGCGCA', 'GAGCAGCGCATTCGTAATGC', 'GCAGCGCATTCGTAATGCGA', 'CGAAGGtCGTAGGTTCGACT', 'AGCTCAGTTGGTAGAGCAGC', 'CAGCGCATTCGTAATGCGAA', 'TCGTAATGCGAAGGtCGTAG', 'AATGCGAAGGtCGTAGGTTC', 'GCCGATATAGCTCAGTTGGT', 'AGCAGCGCATTCGTAATGCG', 'GCGAAGGtCGTAGGTTCGAC', 'TAGGTTCGACTCCTATTATC', 'TTGGTAGAGCAGCGCATTCG', 'GGTAGAGCAGCGCATTCGTA', 'GCTCAGTTGGTAGAGCAGCG', 'TATAGCTCAGTTGGTAGAGC', 'AGGTTCGACTCCTATTATCG', 'GTAGGTTCGACTCCTATTAT', 'GTTGGTAGAGCAGCGCATTC', 'GTAGAGCAGCGCATTCGTAA', 'ATTCGTAATGCGAAGGtCGT', 'GTAATGCGAAGGtCGTAGGT', 'AGTTGGTAGAGCAGCGCATT', 'GCATTCGTAATGCGAAGGtC', 'ATATAGCTCAGTTGGTAGAG', 'tCGTAGGTTCGACTCCTATT', 'GATATAGCTCAGTTGGTAGA', 'TAGAGCAGCGCATTCGTAAT', 'CGACTCCTATTATCGGCACC', 'TTCGACTCCTATTATCGGCA', 'GTTCGACTCCTATTATCGGC', 'TGCGAAGGtCGTAGGTTCGA', 'CGCATTCGTAATGCGAAGGt', 'TAATGCGAAGGtCGTAGGTT', 'ATAGCTCAGTTGGTAGAGCA', 'CATTCGTAATGCGAAGGtCG', 'GACTCCTATTATCGGCACCA', 'TGGTAGAGCAGCGCATTCGT', 'GCGCATTCGTAATGCGAAGG', 'CGTAGGTTCGACTCCTATTA', 'GGtCGTAGGTTCGACTCCTA', 'CTCAGTTGGTAGAGCAGCGC', 'GtCGTAGGTTCGACTCCTAT', 'GAAGGtCGTAGGTTCGACTC', 'TTCGTAATGCGAAGGtCGTA'}
