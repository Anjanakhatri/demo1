import random
#p=int(input('enter first prime number p:'))
#q=int(input('enter second prime number q:'))
q=353;a=3;XA=97
M1=input('enter the message:')
M1=M1.upper()
def modInverse(x,y):
    for i in range(1,y):
        if ((x*i)%y==1):
            return i
    return -1
cipher1=""
cipher2=""
result=""
for i in range(len(M1)):
    M=ord(M1[i])
    YA=pow(a,XA,q)
    k=random.randint(2,q-1)
    KB=pow(YA,k,q)
    C1=pow(a,k,q)
    cipher1+=chr(C1)
    C2=(KB*M)%q
    cipher2+=chr(C2)
 
    KA=pow(C1,XA,q)
    KA_inv=modInverse(KA, q)
    MA=(C2*KA_inv)%q
    result+=chr(MA)
print('the encrypted  message:'+(cipher1+cipher2))
print('the decrypted message:'+result)    
