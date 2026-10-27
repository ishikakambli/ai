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
#Rsa
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
