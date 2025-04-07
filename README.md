# DNA Sequence Analyzer

This project is a simple Python script that analyzes DNA sequences from a multi-FASTA file using Biopython.

## Features
- Parses multiple DNA sequences from a `.fasta` file
- Calculates:
  - Sequence length
  - GC content (%)
- Outputs summary in a CSV file

## Files Included
- `dna_analyzer.py`: Python script for analysis
- `dna2.fasta`: Sample multi-FASTA input file
- `dna_sequence_summary.csv`: Output summary file
- `README.md`: Project documentation

## Requirements
- Python 3
- Biopython

## ▶ How to Run
```bash
pip install biopython
python dna_analyzer.py
```

## Output Example
A CSV file with fields:
- `ID`
- `Length`
- `GC_Content`

## Author
Made with AI and 💻 by sudheer aluru
