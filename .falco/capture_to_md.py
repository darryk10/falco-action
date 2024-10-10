import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Convert a CSV list to a Markdown table.")
parser.add_argument('file', type=str, help='Path to the file containing the CSV data')

# Parse arguments
args = parser.parse_args()

# Open and read the file
with open(args.file, "r") as file:
    lines = file.readlines()


output = []

# Append the Markdown table header
output.append("| Bytes | Proto | Connection | ")
output.append("|-------|-------|------------| ")

# Skip the first two lines (header and separator)
for line in lines[2:]:
    # Split each line by spaces and handle cases with missing protocol
    columns = [col for col in line.split() if col]
    if len(columns) >= 3:
        bytes_transferred, proto, connection = columns[0], columns[1], ' '.join(columns[2:])
    else:
        bytes_transferred, proto, connection = columns[0], '<NA>', '<unknown>'
    
    # Print formatted Markdown row
    output.append(f"| {bytes_transferred:<9} | {proto:<5} | {connection:<48} | ")


for line in output:
    print(line)