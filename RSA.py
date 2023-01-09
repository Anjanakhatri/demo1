import random
p=int(input('enter first prime number p:'))
q=int(input('enter second prime number q:'))
n=p*q
phi=(p-1)*(q-1)
def gcd(p,q):
    while q!=0:
        p,q=q,p%q
    return p
def euler_fun(x):
    if x==1:
        return 1
    else:
        phi_list=[y for y in range(1,x) if gcd(x,y)==1]
        return phi_list
for i in range(2,phi):
    e=random.choice(euler_fun(phi))
    if gcd(e,phi)==1:
        break
def modInverse(x,y):
    for i in range(1,y):
        if ((x*i)%y==1):
            return i
    return -1
d=modInverse(e,phi)
print('public key pair=({},{})'.format(n,e))    
print('private key pair=({} {})'.format(n,d))
M1=input('enter the message:')
M1=M1.upper()
cipher=""
result=""
for i in range(len(M1)):
    M=ord(M1[i])
    C=pow(M,e,n)
    cipher+=chr(C)
    M_decrypted=pow(C,d,n)
    result+=chr(M_decrypted)
print('the encrypted  message:'+cipher)
print('the decrypted message:'+result)    
    

    
    
    
    