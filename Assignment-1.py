import hashlib

i = 0
c = 0

inp=int(input())

def hexa(st2):
    hex = 0
   

    
    for i in range(len(st2)):
        stval = st2[ i ]
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
    
    if vst1 >= inp:
        c += 1

print(i-1)

