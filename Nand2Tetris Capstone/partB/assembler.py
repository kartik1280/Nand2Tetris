import sys

# ---------- Lookup tables ----------
COMP = {
    '0':'0101010','1':'0111111','-1':'0111010','D':'0001100','A':'0110000',
    '!D':'0001101','!A':'0110001','-D':'0001111','-A':'0110011',
    'D+1':'0011111','A+1':'0110111','D-1':'0001110','A-1':'0110010',
    'D+A':'0000010','D-A':'0010011','A-D':'0000111','D&A':'0000000','D|A':'0010101',
    'M':'1110000','!M':'1110001','-M':'1110011','M+1':'1110111','M-1':'1110010',
    'D+M':'1000010','D-M':'1010011','M-D':'1000111','D&M':'1000000','D|M':'1010101',
}
DEST = {'':'000','M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'}
JUMP = {'':'000','JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}

PREDEFINED = {'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576}
PREDEFINED.update({f'R{i}': i for i in range(16)})


def clean(line):
    """Remove comments and all whitespace."""
    return line.split('//')[0].replace(' ', '').replace('\t', '').strip()


def comp_bits(comp):
    """Look up comp; also accept swapped operands like A+D or M+D."""
    if comp in COMP:
        return COMP[comp]
    for op in '+&|':
        if op in comp[1:]:
            left, right = comp.split(op, 1)
            swapped = right + op + left
            if swapped in COMP:
                return COMP[swapped]
    raise ValueError(f"invalid computation '{comp}'")


def dest_bits(dest):
    """Accept dest letters in any order (e.g. DM or MD)."""
    if any(c not in 'AMD' for c in dest):
        raise ValueError(f"invalid destination '{dest}'")
    key = ''.join(sorted(dest, key=lambda c: 'AMD'.index(c)))
    if key not in DEST:
        raise ValueError(f"invalid destination '{dest}'")
    return DEST[key]


def assemble(path):
    symbols = dict(PREDEFINED)
    instructions = []        # list of (line_number, cleaned_text)
    labels_seen = set()

    # ===== FIRST READING: strip comments/blanks, record labels =====
    with open(path) as f:
        for line_no, raw in enumerate(f, 1):
            text = clean(raw)
            if not text:
                continue
            if text.startswith('(') and text.endswith(')'):
                label = text[1:-1]
                # --- Extra feature for K=29 (K mod 3 = 2): duplicate label warning ---
                if label in labels_seen:
                    print(f"Warning: line {line_no}: label '{label}' is defined more than once")
                labels_seen.add(label)
                symbols[label] = len(instructions)   # address of the next instruction
            else:
                instructions.append((line_no, text))

    # ===== SECOND READING: translate every line to 16 bits =====
    output = []
    next_variable = 16
    for line_no, text in instructions:
        try:
            if text.startswith('@'):                 # A-instruction
                value = text[1:]
                if value.isdigit():
                    address = int(value)
                else:
                    if value not in symbols:         # new variable
                        symbols[value] = next_variable
                        next_variable += 1
                    address = symbols[value]
                output.append(format(address, '016b'))
            else:                                    # C-instruction
                dest, comp, jump = '', text, ''
                if '=' in comp:
                    dest, comp = comp.split('=', 1)
                if ';' in comp:
                    comp, jump = comp.split(';', 1)
                if jump not in JUMP:
                    raise ValueError(f"invalid jump '{jump}'")
                output.append('111' + comp_bits(comp) + dest_bits(dest) + JUMP[jump])
        except ValueError as err:
            print(f"Line {line_no}: {err}")
            sys.exit(1)

    out_path = path.rsplit('.', 1)[0] + '.hack'
    with open(out_path, 'w') as f:
        f.write('\n'.join(output) + '\n')
    print(f"Wrote {out_path} ({len(output)} instructions)")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python assembler.py File.asm")
        sys.exit(1)
    assemble(sys.argv[1])
