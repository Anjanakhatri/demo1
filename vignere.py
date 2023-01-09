plaintext=input('enter plaintext message:')
keyword=input('enter kryword:')
plaintext=plaintext.upper()
keyword=keyword.upper()
def generatekey(plaintext,key):
    key=list(key)
    if len(plaintext)==len(key):
        return key
    else:
        for i in range (len(plaintext)-len(key)):
            key.append(key[i%len(key)])
        return("".join(key))   
key=generatekey(plaintext,keyword)   
 
def encrypt_fun(plaintext):
    cipher=" "
    for i in range (len(plaintext)):
        if plaintext[i]==" ":
            cipher+=" "
        else:
            cipher+=chr((ord(plaintext[i])+ord(key[i])-65)%26+65)
    return cipher
print("Cipher txt:" + encrypt_fun(plaintext))     
#decryption
ciphertext=encrypt_fun(plaintext)
def decrypt_fun(ciphertext):
    dec_plain =" "
    for i in range(len(ciphertext)):
        if ciphertext[i]==" ":
            dec_plain+=" "
        else:
            dec_plain+=chr((ord(ciphertext[i])-ord(key[i])-65)%26+65)
    return dec_plain
print("Decrypted txt:" + decrypt_fun(ciphertext))
   