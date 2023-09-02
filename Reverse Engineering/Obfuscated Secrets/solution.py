from struct import pack, unpack
def xf(f1, f2):
    rtrn = []
    a = pack('d', f1)
    b = pack('d', f2)
    for ba, bb in zip(a, b):
        rtrn.append(ba ^ bb)
    return unpack('d', bytes(rtrn))[0].__format__('.4f')


def undo_op(lines):    
    key = 0xEC
    l1 = []
    for line in lines:
        l = line.split(' ')
        ex = float(l[0][1:])
        x = bytearray(str(xf(ex, key)), 'utf-8')
        l1.append('X' + x.decode('utf-8') + ' ' + l[1])

    l2 = []
    for i in range(0, len(l1), 5):
        l2.extend(reversed(l1[i:i+5]))

    l3 = []
    for line in l2:
        l3.append('G01 ' + line)
    return l3

with open('output', 'r') as f:
    inp = f.readlines()

original_gcode = undo_op(inp)

with open('original.gcode', 'w') as f:
    f.writelines(original_gcode)
    