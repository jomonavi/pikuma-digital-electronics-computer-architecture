;====================================================
; Count down from 10 and start over when reaches 0
;====================================================
    LDA #1          ; A = 1
    STA $80         ; $80 = A
RESET:    
    LDA #10         ; A = 10
    
LOOP:
    OUT             ; Display current value
    SUB $80         ; A = A - 1

    BEQ RESET       ; If A==0: start the loop over
    JMP LOOP        ; Else: continue looping¡™¡™¡

    HLT
