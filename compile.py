#!/usr/bin/python3

print('''
-- Copyright (C) 1991-2008 Altera Corporation
-- Your use of Altera Corporation's design tools, logic functions 
-- and other software and tools, and its AMPP partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Altera Program License 
-- Subscription Agreement, Altera MegaCore Function License 
-- Agreement, or other applicable license agreement, including, 
-- without limitation, that your use is for the sole purpose of 
-- programming logic devices manufactured by Altera and sold by 
-- Altera or its authorized distributors.  Please refer to the 
-- applicable agreement for further details.

-- Quartus II generated Memory Initialization File (.mif)
''')

width = 16
depth = 256

print('''
WIDTH=%d;
DEPTH=%d;

ADDRESS_RADIX=UNS;
DATA_RADIX=HEX;
''' % (width, depth))

cmds = {
	'NOP':         0x00,
	'READ':        0x01,
	'WRITE':       0x02,
	'READ_ADDR':   0x03,
	'WRITE_ADDR':  0x04,

	'SET':         0x08,
	'COPY_ADDR':   0x09,
	'SET_ADDR':    0x0A,

	'JUMP':         0x10,
	'JUMP_IF':      0x11,
	'JUMP_ADDR':    0x12,
	'JUMP_ADDR_IF': 0x13,
	
	'ADD':          0x20,
	'SUB':          0x21,
	'ADD_ADDR':     0x22,
	'SUB_ADDR':     0x23,

	'RESET':        0xFF
}

print('CONTENT BEGIN')
index = 0
for line in open('program.asm'):
	parts = line.strip().split()
	if len(parts) > 0:
		cmd = cmds[parts[0].upper()]
		arg = 0;
		if len(parts) > 1:
			arg = int(parts[1])
		print('\t%d : %02X%02X;' % (index, cmd, arg))
		index += 1
print('\t[%d..%d] : 0000;' % (index, depth - 1))
print('END;')
