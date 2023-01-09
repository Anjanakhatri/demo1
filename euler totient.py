def gcd(p,q):
    while q!=0:
        p,q=q,p%q
    return p
    
x=int(input('enter the number for totient function:'))
n=[]
for y in range(1,x):
    if gcd(x,y)==1:
        n.append(y)
print('the value of euler totient function ={}'.format(len(n)))
#print(n)
    
    