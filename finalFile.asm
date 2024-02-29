	j L24

L1: 
	sw ra,(sp)

L2: 
	lw t1,-12(sp)
	li t2,1
	ble,t1,t2,L4

L3: 
	j L6

L4: 
	lw t1,-12(sp)
	lw t0,-8(sp)
	sw t1,(t0)
	lw ra,(sp)
	jr ra

L5: 
	j L16

L6: 
	lw t1,-12(sp)
	li t2,1
	sub,t1,t1,t2
	sw t1,-16(sp)

L7: 
	lw t0,-16(sp)
	sw t0,-12(fp)

L8: 
	addi t0,sp,-20
	sw t0,-8(fp)

L9: 
	lw t0,-4(sp)
	sw t0,-4(fp)
	addi sp,sp,36
	jal L1
	addi sp,sp,-36

L10: 
	lw t1,-12(sp)
	li t2,2
	sub,t1,t1,t2
	sw t1,-24(sp)

L11: 
	lw t0,-24(sp)
	sw t0,-8(fp)

L12: 
	addi t0,sp,-28
	sw t0,-8(fp)

L13: 
	lw t0,-4(sp)
	sw t0,-4(fp)
	addi sp,sp,36
	jal L1
	addi sp,sp,-36

L14: 
	lw t1,-20(sp)
	lw t2,-28(sp)
	add,t1,t1,t2
	sw t1,-32(sp)

L15: 
	lw t1,-32(sp)
	lw t0,-8(sp)
	sw t1,(t0)
	lw ra,(sp)
	jr ra

L16: 
	lw ra,(sp)
	jr ra

L17: 
	sw ra,(sp)

L18: 

L19: 
	lw t0,-12(sp)
	sw t0,-8(fp)

L20: 
	addi t0,sp,-16
	sw t0,-8(fp)

L21: 
	sw sp,-4(fp)
	addi sp,sp,36
	jal L1
	addi sp,sp,-36

L22: 

L23: 
	lw ra,(sp)
	jr ra

L24: 
	addi sp,sp,12
	mv gp,sp

L25: 
	sw sp,-4(fp)
	addi sp,sp,20
	jal L17
	addi sp,sp,-20

L26: 

L27: 
