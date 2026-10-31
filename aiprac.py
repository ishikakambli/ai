# =====================================================================
#encryption
# =====================================================================
def encrypt(text,s):
result= ""
for i in range(len(text)):
char = text[i]
if (char.isupper()):
result += chr((ord(char) + s-65) % 26 +65)
else:
result += chr((ord(char) + s - 97) % 26 + 97)
return result
text = "ATTACKATonce"
s = 4
enc = encrypt(text,s)
print("Text: ",text)
print("Shift: ", s)
print("Cipher Text: ",enc)
# =====================================================================
#decryption
# =====================================================================
def decrypt(text,s):
result = ""

for i in range(len(text)):
char = text[i]
if (char.isupper()):
result += chr((ord(char) - s-65) %26 +65)
else:
result += chr((ord(char) - s - 97) % 26 + 97)
return result
text = "EXXEGOEXsrgi"
s = 4
print("Encypted Text: ",text)
print("Shift: ", s)
print("Decrypted Code: ",decrypt(text,s))
# =====================================================================
#hashing
# =====================================================================
import bcrypt
password = b'MyPassword'
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)
print("Salt:")
print(salt)
print("Hashed:")
print(hashed)
# =====================================================================
#server
# =====================================================================
import socket

s = socket.socket()
print("Socket created successfully !")
s.bind(('0.0.0.0', 8080))
print("Socket binded to 8080")
s.listen(5)
print("Socket is listening...")

while True:
    c, addr = s.accept()
    print("Got connection from ", addr)
    c.send(b'Thank you for connecting! ')
    c.close()
# =====================================================================
#client
# =====================================================================
import socket

s = socket.socket()
s.connect(('127.0.0.1', 8080))
print(s.recv(1024).decode())
# =====================================================================
#tcp.port==8080(zenmap)
# =====================================================================
