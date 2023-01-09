import numpy as np
n=2
K1="part"
M1="anjana"
M1=M1.replace(" ", " ")
M1=M1.upper()
K1=K1.upper()
m=len(M1)
K=[]
for i in range (len(K1)):
    K.append(ord(K1[i])-65)
x=np.reshape(K,(n,n)).T 
M=[]
for i in range (m):
    M.append(ord(M1[i])-65)
y=np.reshape(M,(n,m//n))
C=(np.dot(x,y))%26
C1=np.reshape(C+65,(1,m))
C2=[]
for i in range (m):
    C2.append(chr(C1[0][i]))
print("ciphertext:","".join(C2))
def modInverse(x,y):
    for i in range(1,y):
        if ((x*i))%y==1:
            return i
    return -1
x_det=int(np.linalg.det(x))%26
det_inv=modInverse(x_det, 26) 
x_adj=np.array([[x[1][1],-x[0][1]],[-x[1][0],x[0][0]]])  
x_inv=(x_det*x_adj)%26
M_dec1=(np.dot(x_inv,C))%26
M_dec2=np.reshape(M_dec1+65,(1,m)) 
M_dec=[]
for i in range (m):
    M_dec.append(chr(M_dec2[0][i]))
print("decrypted text:","".join(M_dec))
    
    