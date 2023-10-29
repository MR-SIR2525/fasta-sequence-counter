# FASTA Sequence Counter

## File to use: `counter.py`

## Description
This Python script extracts unique nucleotide sequences from file 1 (a txt file) and counts how many times each unique sequence appears in file2 (a FASTA file), and writes the results to an output file.

The input file example here is "Salmon.txt" and the example output is "sequence_counts.txt," which was generated from counting a large fasta file that's too large for free github. 

## Notes
- **Efficient Memory Usage**: Handles large FASTA files by reading them line by line without loading the entire file into memory, letting you analyze massive 40 GB files on a typical windows pc. It works with only 8 GB of RAM for sure, probably less but I can't confirm.
- **Example Output**: Writes the count of each unique sequence to an output file like this: 
  
        sequence1   occurences1
        sequence2   occurences2
        sequence3   occurences3
        etc...

## Requirements
- Python 3.x

## Usage

1. **Input Files**:
   - The txt file with your unique nucleotide sequences (should be 20 characters long but you can change the code to do a different length).
   - The FASTA file.

2. **Run the Script and follow the prompts**:

    Windows cmd or powershell:
   ```powershell
   py counter.py
   ```

    bash:
   ```bash
   python counter.py
   ```

3. **Output**
   - After waiting for the script to run (it might take a while depending on how big the input files are), you'll get the output file called "sequence_counts.txt"
