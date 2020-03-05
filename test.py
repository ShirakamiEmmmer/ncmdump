key_data = "60720177239789146097691462E7fT49x7dof9OKCgg9cdvhEuezy3iZCL1nFvBFd1T4uSktAJKmwZXsijPbijliionVUXXg9plTbXEclAE9Lb"
key_data = "60720177239789146097691462E7fT49x7dof9OKCgg9cdvhEuezy3iZCL1nFvBFd1T4uSktAJKmwZXsijPbijliionVUXXg9plTbXEclAE9Lb"

key_length = len(key_data)

key_data = bytes(key_data, encoding = "utf8")

key_data = bytearray(key_data)

key_box = bytearray(range(256))

c = 0

last_byte = 0

key_offset = 0

for i in range(256):
    swap = key_box[i]
    c = (swap + last_byte + key_data[key_offset]) & 0xff
    key_offset += 1
    if key_offset >= key_length: key_offset = 0
    key_box[i] = key_box[c]
    key_box[c] = swap
    last_byte = c

for i in key_box:
    print(i)
    # print("\n")