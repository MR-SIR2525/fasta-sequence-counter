import os

def extract_sequences(file_path):
    """
    Extracts sequences of 20 characters from a file.\n
    Returns a set of sequences extracted from the file.
    """
    sequences = set()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            for i in range(len(line) - 19):
                sequence = line[i:i+20]
                sequences.add(sequence)
    return sequences

def count_sequences_in_file(unique_sequences, file_path):
    """
    Counts the occurrences of each unique sequence in the file and returns a dictionary of 'sequences: counts'.
    
    Parameters:
        - unique_sequences (list): A list of unique DNA sequences.
        - file_path (str): The path to the file containing the DNA sequences.
    
    Returns:
        - counts (dict): A dictionary containing the counts of each unique sequence in the file.
    """
    counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            for i in range(len(line) - 19):
                sequence = line[i:i+20]
                if sequence in unique_sequences:
                    counts[sequence] = counts.get(sequence, 0) + 1
    return counts

def main():
    input_folder = "" # for specific folder
    # os.makedirs(input_folder, exist_ok=True)

    try:
        file1_path = input(
            "Enter the path to the first file (containing nucleotide sequences, 20 characters each): "
        )
        if not os.path.exists(file1_path):
            print("File 1 not found.")
            return

        file2_path = input("Enter the name (including path if needed) to the second file: ")

        if not os.path.exists(file2_path):
            print("Problem: File 2 not found.")
            return
        print(f"File 2 ({file2_path}) found.")

        # Extract unique sequences from file 1
        unique_sequences = extract_sequences(file1_path)
        print(f"Found {len(unique_sequences)} unique sequences in {file1_path}")

        # Count occurrences of unique sequences in file 2
        print("Counting occurrences of unique sequences in file 2...")
        counts = count_sequences_in_file(unique_sequences, file2_path)
        print("Finished counting.\n")


        # Declare output file then write to it
        output_file = os.path.join(input_folder, "sequence_counts.txt")

        with open(output_file, 'w') as outfile:
            for sequence, count in counts.items():
                outfile.write(f"{sequence}\t{count}\n")

            print(f"Results have been saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()