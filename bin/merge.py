# If you have a large dataset, this Python script reads your CSV, 
# detects rows with an empty first cell, appends their contents to 
# the cell directly above, and deletes the empty row.

import csv
import sys

# Ensure enough arguments were passed to prevent IndexError
if len(sys.argv) < 3:
    print("Error: Please provide at least two arguments.")
    sys.exit(1)

# Retrieve the first and second arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# print("input_file:" + input_file + " output_file:" + output_file)
# sys.exit(1)

# input_file = "output4.csv"
# output_file = "merged_output2.csv"

processed_rows = []

with open(input_file, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    
    for row in reader:
        # Check if the row has content and if the first cell is empty
        if row and not row[0].strip():
            if processed_rows:
                # Append the text of each column to the corresponding column in the row above
                for i in range(len(row)):
                    if i < len(processed_rows[-1]) and row[i].strip():
                        # Add a space and append the text
                        processed_rows[-1][i] += f" {row[i].strip()}"
        else:
            # If the first cell has a value, keep it as a new row
            processed_rows.append(row)

# Save the newly cleaned data
with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(processed_rows)
