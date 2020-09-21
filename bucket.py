# Begins in memory at 0x801cb0f4 and is around 240 bytes in length

iVar1 = 0 # Max 3
iVar5 = 2 # Max 2?

offset = iVar5 * 0x50 + iVar1 * 0x14 # from 0x800c91a8
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
