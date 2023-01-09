plaintext=input('Enter plaintext')
s=int(input("Enter number of shift:"))
plaintext = plaintext.upper()
def encrypt_fun(plaintext):
    cipher=" "
    for i in range (len(plaintext)):
        if plaintext[i]==" ":
            cipher+=" "
        else:
            cipher+=chr((ord(plaintext[i])+s-65)%26+65)
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
            dec_plain+=chr((ord(ciphertext[i])-s-65)%26+65)
    return dec_plain
print("Decrypted txt:" + decrypt_fun(ciphertext))
   
            