import hashlib

i = 0
c = 0



def hexa(st2):
    hex = 0
    p = 1

    l = len(st2)
    for i in range(len(st2)):
        stval = st2[l - i - 1]
        if (ord(stval) < 60):
            val = ord(stval) - 48
        else:
            stval.lower()
            val = ord(stval) - 87
        hex += p * val
        p *= 16
    return (hex)


while (c == 0):
    st = "iitk" + str(i)
    i += 1
    st1 = hashlib.sha256(st.encode('utf-8')).hexdigest()
    vst1 = hexa(st1)
    hex1 = hexa("0000"+("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF").lower())
    if vst1 < hex1:
        c += 1

print(i-1)

