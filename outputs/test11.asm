; Symbol table GLOBAL
; name cur type FLOAT location 0x20000000

.section .text
;Current temp: null
;IR Code: 
LA t1, 0x20000000
FIMM.S f1, 0.0
FSW f1, 0(t1)
loop_1:
LA t2, 0x20000000
FLW f3, 0(t2)
FIMM.S f2, 10.0
FLT.S t5, f3, f2
BEQ t5, x0, out_1
LA t4, 0x20000000
LA t3, 0x20000000
FLW f5, 0(t3)
FIMM.S f4, 4.0
FADD.S f6, f5, f4
FSW f6, 0(t4)
J loop_1
out_1:
LA t6, 0x20000000
FLW f7, 0(t6)
PUTF f7
LI t7, 0
HALT


.section .strings
