;==============================
; Fibonacci Loop (1..255)
;==============================
START:
LDA #1          ; A = 1
STA $80         ; prev = 1
STA $81         ; curr = 1
OUT             ; output 1

LOOP:
    LDA $81         ; A = curr
    OUT             ; Display current value

    STA $82         ; temp = curr
    ADD $80         ; A = curr + prev
    BCS RESET       ; if overflow (>255), reset

    STA $81         ; curr = sum
    LDA $82         ; A = old curr
    STA $80         ; prev = old curr
    JMP LOOP

RESET:
    LDA #1          ; restart sequence
    STA $80         ; prev = 1
    STA $81         ; curr = 1
    OUT             ; output 1
    JMP LOOP