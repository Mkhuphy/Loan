import hashlib
import time

i = 0
c = 0
inpt=int(input())
s=time.time()
def hexa(st2):
    hex = 0

    for i in range(len(st2)):
        stval = st2[i]
        if (ord(stval) == 48):
            hex += 1
        else:
            break
    return (hex)


while (c == 0):
    st = "iitk" + str(i)
    i += 1
    st1 = hashlib.sha256(st.encode('utf-8')).hexdigest()
    vst1 = hexa(st1)

    if vst1 >= inpt:
        c += 1
e=time.time()
print(i - 1)
print("Time elapsed= "+str(e-s))

