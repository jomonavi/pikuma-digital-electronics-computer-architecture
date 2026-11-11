import sys

OPCODES = {
    "NOP":  0b00000,
    "LDA#": 0b00001,  # LDA #imm
    "LDA":  0b00010,  # LDA $addr
    "ADD":  0b00011,
    "SUB":  0b00100,
    "STA":  0b00101,
    "JMP":  0b00110,
    "XOR#": 0b00111,
    "XOR":  0b01000,
    "NOT":  0b01001,
    "OUT":  0b01010,
    "AND#": 0b01011,
    "AND":  0b01100,
    "OR#":  0b01101,
    "OR":   0b01110,
    "SHR":  0b10000,
    "SHL":  0b10001,
    "BEQ":  0b10010,
    "BNE":  0b10011,
    "BPL":  0b10100,
    "BMI":  0b10101,
    "BCS":  0b10110,
    "BCC":  0b10111,
    "HLT":  0b11111,
}

def assemble(lines):
    #TODO:...
    pass

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 assembler.py <source.asm> [-b|--bin]")
        sys.exit(1)

    filename = sys.argv[1]
    binary = "-b" in sys.argv or "--bin" in sys.argv

    try:
        with open(filename) as f:
            lines = f.readlines()
    except OSError as e:
        print(f"Error opening {filename}: {e}")
        sys.exit(1)

    assemble(lines)

if __name__ == "__main__":
  main()