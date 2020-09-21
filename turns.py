# 
"""
Prints out the turn_param for bucket percentage modifiers. turn_param is calculated
using a formula of the total number of turns in the game compared to the current turn
number. The total number of turns must be between 10 and 50 turns. This is enforced
by the game itself.

Usage:
python turns.py {TOTAL_NUM_OF_TURNS} {CURRENT_TURN}

Example:
python turns.py 20 5
"""
import sys

TOTAL_NUM_OF_TURNS = int(sys.argv[1])
CURRENT_TURN = int(sys.argv[2])

DAT_801cb1e4 = [0xa, 0xf, 0x14, 0x19, 0x1e, 0x23, 0x28, 0x2d, 0x32]
DAT_801cb208 = [0x3, 0x6, 0x5, 0xa, 0x5, 0xf, 0x8, 0x10, 0xa, 0x14, 0xa, 0x14, 0xd, 0x1a, 0xf, 0x1e, 0xf, 0x23]

index4 = 0
while (index4 < 8 and DAT_801cb1e4[index4] < TOTAL_NUM_OF_TURNS):
    index4 = index4 + 1
#print("index4: {}".format(index4))
iVar4 = 0
while (iVar4 < 2 and DAT_801cb208[iVar4 + index4 * 2] <= CURRENT_TURN):
    iVar4 = iVar4 + 1
print("turn_param: {}".format(iVar4))
