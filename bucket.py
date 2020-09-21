"""
Prints out the percentages of each of the five buckets being chosen given
the current place and turn parameter. The percentages are read from
bucket_percentages.dat which contains the 240 bytes at 0x801cb0f4 in
memory.

Usage:
python bucket.py {CURRENT_PLACE} {TURN_PARAM}

Example:
python bucket.py 1 0
"""
import sys

if (len(sys.argv) != 3):
    print('Please include CURRENT_PLACE and TURN_PARAM parameters')
    sys.exit(1)

CURRENT_PLACE = int(sys.argv[1])
TURN_PARAM = int(sys.argv[2])

if (CURRENT_PLACE > 3 or CURRENT_PLACE < 0):
    print('CURRENT_PLACE must be between 0 (inclusive) and 3 (inclusive)')
    sys.exit(1)
elif (TURN_PARAM > 2 or CURRENT_PLACE < 0):
    print('TURN_PARAM must be between 0 (inclusive) and 2 (inclusive)')
    sys.exit(1)

offset = TURN_PARAM * 0x50 + CURRENT_PLACE * 0x14 # from 0x800c91a8
with open("bucket_percentages.dat", "rb") as f:
    print("Offset: 0x{:02X}\n".format(offset))
    f.seek(offset)
    word = int.from_bytes(f.read(4), byteorder='big')
    print("Bucket A: {}".format(word))
    word = int.from_bytes(f.read(4), byteorder='big')
    print("Bucket B: {}".format(word))
    word = int.from_bytes(f.read(4), byteorder='big')
    print("Bucket C: {}".format(word))
    word = int.from_bytes(f.read(4), byteorder='big')
    print("Bucket D: {}".format(word))
    word = int.from_bytes(f.read(4), byteorder='big')
    print("Bucket E: {}".format(word))
