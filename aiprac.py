# =====================================================================
#Perform the Frequency Analysis Attack on a Monoalphabetic Cipher
# =====================================================================
text = input("Enter cipher text: ").upper()

freq = {}

for ch in text:
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1

print("Letter Frequencies:")

for ch in sorted(freq, key=freq.get, reverse=True):
    print(ch, ":", freq[ch])
# =====================================================================
#Caesar Cipher 
# =====================================================================
text = input("Enter message: ").upper()
key = int(input("Enter key: "))

enc = ""

for ch in text:
    if ch.isalpha():
        enc += chr((ord(ch) - 65 + key) % 26 + 65)
    else:
        enc += ch

print("Encrypted:", enc)

dec = ""

for ch in enc:
    if ch.isalpha():
        dec += chr((ord(ch) - 65 - key) % 26 + 65)
    else:
        dec += ch

print("Decrypted:", dec)
# =====================================================================
#Monoalphabetic Cipher 
# =====================================================================
text = input("Enter message: ").upper()

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

enc = ""

for ch in text:
    if ch in abc:
        enc += key[abc.index(ch)]
    else:
        enc += ch

print("Encrypted:", enc)

dec = ""

for ch in enc:
    if ch in key:
        dec += abc[key.index(ch)]
    else:
        dec += ch

print("Decrypted:", dec)
# =====================================================================
#Columnar
# =====================================================================
def col(text, key, mode='enc'):
    k = len(key)
    order = sorted(range(k), key=lambda i: key[i])

    if mode == 'enc':
        while len(text) % k != 0:
            text += 'X'
        	
        res = ""
        for i in order:
            res += text[i::k]
        return res

    else:
        r = len(text) // k
        cols = [""] * k
        
        for i in order:
            cols[i] = text[:r]
            text = text[r:]  
            
        res = ""
        for row in zip(*cols):
            res += "".join(row)
        return res
text = 'bananachair'
key = 'ball'
enc = col(text, key, mode='enc')
print(f"enc is {enc}")
dec = col(enc, key, mode='dec')
print(f"dec is {dec}")
# =====================================================================
#Rsa(Rivest–Shamir–Adleman)
# =====================================================================
import hashlib

p = int(input("enter no:-"))
q = int(input("enter no:-"))

n = p * q
phi = (p - 1) * (q - 1)

e = 3
d = 7

message = 5


signature = (message ** d) % n
print("Digital Signature:", signature)

verify = (signature ** e) % n
print("Verified Message:", verify)

if verify == message:
    print("Signature is Valid")
else:
    print("Signature is not Invalid")
# =====================================================================
#Diffie hellman 
# =====================================================================
p = int(input("enter no:-"))#23
g = int(input("enter no:-"))#5

a = 6
b = 15

A = (g ** a) % p
B = (g ** b) % p

key1 = (B ** a) % p
key2 = (A ** b) % p

print("Alice's public key:", A)
print("Bob's public key:", B)
print("Alice's secret key:", key1)
print("Bob's secret key:", key2)
# =====================================================================
#Vernam cipher
# =====================================================================
def vernam_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Key must be the same length as the plaintext.")
    return ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))

def vernam_decrypt(ciphertext, key):
    
    return vernam_encrypt(ciphertext, key)


plaintext = "HELLO"
key = "XMCKL"


ciphertext = vernam_encrypt(plaintext, key)
print("Encrypted (Raw):", repr(ciphertext)) 

decrypted = vernam_decrypt(ciphertext, key)
print("Decrypted:     ", decrypted)
# =====================================================================
#Playfair cipher
# =====================================================================
def prepare_key_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    key_matrix = []
    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            key_matrix.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            key_matrix.append(char)
    return [key_matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None, None

def encrypt_digraph(digraph, matrix):
    a, b = digraph
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def prepare_plaintext(text):
    text = text.upper().replace("J", "I")
    cleaned = []
    i = 0
    while i < len(text):
        if not text[i].isalpha():
            i += 1
            continue
        a = text[i]
        
        next_char_idx = i + 1
        while next_char_idx < len(text) and not text[next_char_idx].isalpha():
            next_char_idx += 1
            
        if next_char_idx < len(text):
            b = text[next_char_idx]
            if a == b:
                cleaned.append(a + 'X')
                i += 1
            else:
                cleaned.append(a + b)
                i = next_char_idx + 1
        else:
            cleaned.append(a + 'X')
            i += 1
            
    return cleaned

def playfair_encrypt(plaintext, key):
    matrix = prepare_key_matrix(key)
    digraphs = prepare_plaintext(plaintext)
    ciphertext = ''.join(encrypt_digraph(pair, matrix) for pair in digraphs)
    return ciphertext

cipher = playfair_encrypt("Hello TYCS", "MONARCHY")
print(cipher)
# =====================================================================
#Sha1 signature(Secure Hash Algorithm 1.)
# =====================================================================
#for message
import hmac
import hashlib

key = input("Enter secret key: ")
message = input("Enter message: ")

signature = hmac.new(key.encode(), message.encode(), hashlib.sha1).hexdigest()

print("HMAC-SHA1 Signature:", signature)

#for file 
for file
import hmac
import hashlib
key = input("Enter secret key: ")
file = input("Enter file path: ")
try:
    with open(file, 'rb') as f:
        data = f.read()
    signature = hmac.new(key.encode(), data, hashlib.sha1).hexdigest()
    print("HMAC-SHA1 Signature:", signature)
except FileNotFoundError:
    print("File not found")
# =====================================================================
#DES(Data Encryption Standard)
# =====================================================================
import base64
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(8)
BS = DES.block_size  

def des_run(text, key, mode, action='enc'):
    needs_pad = mode in (DES.MODE_ECB, DES.MODE_CBC)
    
    if action == 'enc':
        cipher = DES.new(key, mode)
        data = pad(text.encode(), BS) if needs_pad else text.encode()
        iv = b"" if mode == DES.MODE_ECB else cipher.iv
        return base64.b64encode(iv + cipher.encrypt(data)).decode()
        
    else:
        raw = base64.b64decode(text)
        cipher = DES.new(key, mode) if mode == DES.MODE_ECB else DES.new(key, mode, iv=raw[:BS])
        ct = raw if mode == DES.MODE_ECB else raw[BS:]
        
        dec = cipher.decrypt(ct)
        return (unpad(dec, BS) if needs_pad else dec).decode()

message = "Hello DES! This is a test message."
modes = {
    "ECB": DES.MODE_ECB,
    "CBC": DES.MODE_CBC,
    "CFB": DES.MODE_CFB,
    "OFB": DES.MODE_OFB
}

for name, mode in modes.items():
    enc = des_run(message, key, mode, 'enc')
    dec = des_run(enc, key, mode, 'dec')
    print(f"{name} Encrypted: {enc}")
    print(f"{name} Decrypted: {dec}\n")
# =====================================================================
#AES(Advanced Encryption Standard)
# =====================================================================
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
key = get_random_bytes(32)
BS = AES.block_size  

def aes_run(text, key, mode, action='enc'):
    needs_pad = mode in (AES.MODE_ECB, AES.MODE_CBC)
    
    if action == 'enc':
        cipher = AES.new(key, mode)
        data = pad(text.encode(), BS) if needs_pad else text.encode()
        
        iv = b"" if mode == AES.MODE_ECB else cipher.iv
        return base64.b64encode(iv + cipher.encrypt(data)).decode()
        
    else:
        raw = base64.b64decode(text)
       
        cipher = AES.new(key, mode) if mode == AES.MODE_ECB else AES.new(key, mode, iv=raw[:BS])
        ct = raw if mode == AES.MODE_ECB else raw[BS:]
        
        dec = cipher.decrypt(ct)
        return (unpad(dec, BS) if needs_pad else dec).decode()


message = "Hello AES! This is a test message."
modes = {
    "ECB": AES.MODE_ECB,
    "CBC": AES.MODE_CBC,
    "CFB": AES.MODE_CFB,
    "OFB": AES.MODE_OFB
}

for name, mode in modes.items():
    enc = aes_run(message, key, mode, 'enc')
    dec = aes_run(enc, key, mode, 'dec')
    print(f"{name} Encrypted: {enc}")
    print(f"{name} Decrypted: {dec}\n")
# =====================================================================
#SSL(Secure Sockets Layer)
# =====================================================================
#cmd:- openssl req -x509 -keyout key.pem -out cert.pem -nodes -subj "/CN=a"
#server
import socket, ssl
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("cert.pem", "key.pem")
with ctx.wrap_socket(socket.create_server(("localhost", 8443))) as s:
    conn, _ = s.accept()
    print("Received:", conn.recv(1024).decode())
    conn.send(b"Hello from server!")
#client
import socket, ssl
ctx = ssl._create_unverified_context()
with ctx.wrap_socket(socket.create_connection(("localhost", 8443))) as s:
    s.send(b"Hello secure server!")
    print("Server replied:", s.recv(1024).decode())
