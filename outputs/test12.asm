; Symbol table GLOBAL
; name a type FLOAT location 0x20000000
; name b type FLOAT location 0x20000004
; name c type FLOAT location 0x20000008
; name d type FLOAT location 0x2000000c
; name prompt type STRING location 0x10000000 value "enter a number "
; name output1 type STRING location 0x10000004 value "a less than b"
; name output2 type STRING location 0x10000008 value " and less than c \n"
; name output3 type STRING location 0x1000000c value " but not less than c \n"
; name output4 type STRING location 0x10000010 value "a greater than or equal to b"

.section .text
;Current temp: null
;IR Code: 
LA t1, 0x10000000
PUTS t1
LA t2, 0x20000000
GETF f1
FSW f1, 0(t2)
LA t3, 0x10000000
PUTS t3
LA t4, 0x20000004
GETF f2
FSW f2, 0(t4)
LA t5, 0x10000000
PUTS t5
LA t6, 0x20000008
GETF f3
FSW f3, 0(t6)
LA t7, 0x20000000
FLW f4, 0(t7)
LA t8, 0x20000004
FLW f5, 0(t8)
FLT.S t21, f4, f5
BEQ t21, x0, else_3
LA t9, 0x10000004
PUTS t9
LA t10, 0x20000000
FLW f6, 0(t10)
LA t11, 0x20000008
FLW f7, 0(t11)
FLT.S t14, f6, f7
BEQ t14, x0, else_1
LA t12, 0x10000008
PUTS t12
J out_1
else_1:
LA t13, 0x1000000c
PUTS t13
out_1:
J out_3
else_3:
LA t15, 0x10000010
PUTS t15
LA t16, 0x20000000
FLW f8, 0(t16)
LA t17, 0x20000008
FLW f9, 0(t17)
FLT.S t20, f8, f9
BEQ t20, x0, else_2
LA t18, 0x10000008
PUTS t18
J out_2
else_2:
LA t19, 0x1000000c
PUTS t19
out_2:
out_3:
LI t22, 0
HALT


.section .strings
0x10000000 "enter a number "
0x10000004 "a less than b"
0x10000008 " and less than c \n"
0x1000000c " but not less than c \n"
0x10000010 "a greater than or equal to b"
