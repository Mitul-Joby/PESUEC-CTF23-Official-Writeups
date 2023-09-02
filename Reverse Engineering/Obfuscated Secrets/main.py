from struct import pack, unpack
def xf(f1, f2):
    rtrn = []
    a = pack('d', f1)
    b = pack('d', f2)
    for ba, bb in zip(a, b):
        rtrn.append(ba ^ bb)
    return unpack('d', bytes(rtrn))[0]

def op(lines):
    l1 = []
    for line in lines:
        l1.append(line[4:])
    l2 = []
    for i in range(0, len(l1), 5):
        l2.extend(reversed(l1[i:i+5]))
    key = float(0xEC)
    l3 = []
    for line in l2:
        l = line.split(' ')
        x = float(l[0][1:])
        ex = bytearray(str(xf(x, key)), 'utf-8')
        l3.append('X' + ex.decode('utf-8') + ' ' + l[1])
    return l3
    

with open('input', 'r') as f:
    inp = f.readlines()
output = op(inp)
with open('output', 'w') as f:
    f.writelines(output)
