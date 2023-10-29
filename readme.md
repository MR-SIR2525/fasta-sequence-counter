# FASTA Sequence Counter

## Description
This Python script extracts unique nucleotide sequences from file 1 (a txt file) and counts how many times each unique sequence appears in file2 (a FASTA file), and writes the results to an output file.

The input file example here is "Salmon.txt" and the example output is "sequence_counts.txt," which was generated from counting a large fasta file that's too large for free github. 

## Notes
- **Efficient Memory Usage**: It handles large FASTA files without loading the entire file into memory, which is good for letting you analyze files on a typical windows pc. 
- **Example Output**: Writes the count of each unique sequence to an output file like this: CGATATAGCTCAGTTGGTAG	[# of occurences]

## Requirements
- Python 3.x

## Usage

1. **Input Files**:
   - Have a txt file ready with your unique nucleotide sequences. Each sequence should be 20 characters long.
   - Ensure your FASTA formatted file is available.

2. **Run the Script**:
   ```Windows
   py counter.py

   ```bash
   python counter.py

3. **Output**
   - After waiting for the script to run (it might take a while depending on how big the input files are), you'll get the output file called "sequence_counts.txt"


## Input File Format
- Unique Sequences File: A plain text file with nucleotide sequences. Each sequence should be exactly 20 characters long, but you can switch this in the python code if needed. 
- FASTA File: A standard FASTA formatted file containing nucleotide sequences.
