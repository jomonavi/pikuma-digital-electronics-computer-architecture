;=====================================================
; 16-bit add using the carry flag
; $01F0 + $0020 = $0210

;    1
;   01 F0
; + 00 20
; -------
;   02 10

;=====================================================
    LDA #$F0        ; low byte of $01F0
    ADD #$20        ; + low byte of $0020 -> $10, C=1
    STA $80
    LDA #1          ; high byte of $01F0
    ADC #0          ; + high byte + C -> $02
    STA $81
    LDA $81
    OUT             ; 2   (high byte)
    LDA $80
    OUT             ; 16  (low byte)

;=====================================================
; 16-bit subtract using the carry/borrow flag
; $0210 - $0011 = $01FF

;    0
;   02 10
; - 00 11
; -------
;   01 FF

;=====================================================
                    ; Don't need to load $10 into Accumulator (previous A is already $10)
    SUB #$11        ; $10 - $11 -> $FF, borrow (C=0)
    STA $80
    LDA $81         ; Already have in address $81 the value $02
    SBC #0          ; $02 - 0 - borrow -> $01
    
    OUT             ; 01  (high byte)
    LDA $80
    OUT             ; 255 (low byte)
    HLT