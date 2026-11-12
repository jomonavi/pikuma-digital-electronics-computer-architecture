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
    "ADD#": 0b01111,
    "SHR":  0b10000,
    "SHL":  0b10001,
    "BEQ":  0b10010,
    "BNE":  0b10011,
    "BPL":  0b10100,
    "BMI":  0b10101,
    "BCS":  0b10110,
    "BCC":  0b10111,
    "SUB#": 0b11000,
    "ADC":  0b11001,  # ADC $addr : A = A + mem + C
    "SBC":  0b11010,  # SBC $addr : A = A - mem - (1 - C)
    "ADC#": 0b11011,  # ADC #imm  : A = A + imm + C
    "SBC#": 0b11100,  # SBC #imm  : A = A - imm - (1 - C)
    "HLT":  0b11111,
}

def instruction_size(mnemonic):
    if mnemonic in {"NOP", "OUT", "NOT", "SHL", "SHR", "HLT"}:
        return 1
    else:
        return 2
    
def parse_number(token):
    if token.startswith("$"):
        return int(token[1:], 16) # hexadecimal
    return int(token)             # decimal

def assemble(lines):
    labels = {}
    pc = 0

    ############################
    ## PASS 1: collect labels:
    ############################
    for line in lines:
        line = line.split(";")[0].strip()
        if not line:
            continue

        if line.endswith(":"):
            label = line[:-1]
            labels[label] = pc
            continue

        mnemonic = line.split()[0].upper()
        pc += instruction_size(mnemonic)

    ############################
    ## PASS 2: generate code
    ############################
    code = []
    pc = 0

    for line in lines:
        line = line.split(";")[0].strip()
        if not line or line.endswith(":"):
            continue

        parts = line.split(None, maxsplit=1)
        mnemonic = parts[0].upper()
        operand = parts[1] if len(parts) > 1 else None

        opcode = None
        value = None

        if operand:
            operand = operand.strip()
            if operand.startswith("#"):
                opcode = OPCODES[mnemonic + "#"]
                value = parse_number(operand[1:])
            else:
                opcode = OPCODES[mnemonic]
                if operand in labels:
                    value = labels[operand]
                else:
                    value = parse_number(operand)
        else:
            opcode = OPCODES[mnemonic]

        code.append(opcode & 0xFF)

        if value is not None:
            code.append(value & 0xFF)

        pc += instruction_size(mnemonic)

    return code

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

    code = assemble(lines)

    for b in code:
        if binary:
            print(f"{b:08b}")
        else:
            print(f"{b:02X}")

if __name__ == "__main__":
  main()
