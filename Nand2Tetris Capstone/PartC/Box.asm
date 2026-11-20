// Part C: Keyboard-controlled black box
// K = 29
// Top row = 29, height = 20 rows, width = 32 pixels (2 words)
// Left edge of the screen

(LOOP)
    @KBD
    D=M
    @DRAW
    D;JGT
    @CLEAR
    0;JMP

(DRAW)
    // SCREEN + 32*29 = 16384 + 928 = 17312
    @17312
    D=A
    @R13
    M=D

    @20
    D=A
    @R14
    M=D

(DRAW_ROW)
    // Draw the first 16-pixel word.
    @R13
    A=M
    M=-1

    // Draw the second 16-pixel word.
    @R13
    M=M+1
    A=M
    M=-1

    // R13 points to word 2. Add 31 to reach word 1 of next row.
    @R13
    D=M
    @31
    D=D+A
    @R13
    M=D

    @R14
    MD=M-1
    @DRAW_ROW
    D;JGT

    @LOOP
    0;JMP

(CLEAR)
    // Reset pointer to the first word of row 29.
    @17312
    D=A
    @R13
    M=D

    @20
    D=A
    @R14
    M=D

(CLEAR_ROW)
    // Clear the first 16-pixel word.
    @R13
    A=M
    M=0

    // Clear the second 16-pixel word.
    @R13
    M=M+1
    A=M
    M=0

    // R13 points to word 2. Add 31 to reach word 1 of next row.
    @R13
    D=M
    @31
    D=D+A
    @R13
    M=D

    @R14
    MD=M-1
    @CLEAR_ROW
    D;JGT

    @LOOP
    0;JMP
