q=int(input('enter prime number(q):'))
a=int(input('enter primitive root(a):'))
XA=int(input('Alice secret key(XA):'))
XB=int(input('Bob secret key (XB):'))
YA=pow(a,XA,q)
YB=pow(a,XB,q)
KA=pow(YB,XA,q)
KB=pow(YA,XB,q)
print('secret key for alice is: %d'%(KA))
print('secret key for Bob is: %d'%(KB))