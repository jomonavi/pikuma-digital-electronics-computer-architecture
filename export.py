import csv
import re

###############################################################################
# This script reads a CSV with the definition of our control unit ROM and
# generates a .hex output in the correct forma expected by Logisim ROM input.
###############################################################################
INPUT_CSV = "rom-cu.csv"
OUTPUT_HEX = "output.hex"
WORDS_PER_LINE = 8

HEX_RE = re.compile(r"^[0-9A-Fa-f]+$")

def read_cell_data(csv_path):
    cell_data = []
    with open(csv_path, newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
        last_col = len(rows[0]) - 1
        for row in rows:
            value = row[last_col].strip()
            # Skip header or any non-hex entries
            if not HEX_RE.match(value):
                continue
            cell_data.append(value.zfill(8).upper()) # Force 32-bit hex value with zero left-padding
    return cell_data

def write_hex_file(words, output_path):
    with open(output_path, "w") as f:
        f.write("v3.0 hex words addressed\n")
        address = 0
        for i in range(0, len(words), WORDS_PER_LINE):
            chunk = words[i:i + WORDS_PER_LINE]
            f.write(f"{address:02X}: " + " ".join(chunk) + "\n")
            address += WORDS_PER_LINE

def main():
    words = read_cell_data(INPUT_CSV)
    write_hex_file(words, OUTPUT_HEX)

if __name__ == "__main__":
    main()
    
