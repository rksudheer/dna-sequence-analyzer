from Bio import SeqIO
import csv

# Load the FASTA file
fasta_file = "dna2.fasta"
records = list(SeqIO.parse(fasta_file, "fasta"))

# Summary output
summary = []
for record in records:
    sequence = str(record.seq)
    gc_content = 100 * (sequence.count("G") + sequence.count("C")) / len(sequence)
    summary.append({
        "ID": record.id,
        "Length": len(sequence),
        "GC_Content": round(gc_content, 2)
    })

# Save to CSV
output_csv = "dna_sequence_summary.csv"
with open(output_csv, "w", newline="") as csvfile:
    fieldnames = ["ID", "Length", "GC_Content"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(summary)

# Report total records
print("Total records in file:", len(records))
