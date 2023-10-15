import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt

p = 233970423115425145524320034830162017933
Gx = 182
Gy = 85518893674295321206118380980485522083
Qx = 7856

# Given ciphertext
cs_b64 = "1JtwWPLfoVoUxK6TnRqyMIz00GldXbM0/dsaqBgWCO8hMlSRJITRknKVHhIGONYxgTBRyjIwIdVXn+ohLHBy2A=="
cs = base64.b64decode(cs_b64)

# Extract IV, ciphertext, and salt from cs
iv = cs[:16]
ciphertext = cs[16:-16]
salt = cs[-16:]

# Calculate private key k
k = (Qx - Gx) * pow(Gy, -1, p) % p

# Derive key using scrypt
key = scrypt(k.to_bytes((k.bit_length() + 7) // 8, 'big'), salt, 32, N=16384, r=8, p=1)

# Decrypt the ciphertext
cipher = AES.new(key, AES.MODE_CBC, iv)
flag_padded = cipher.decrypt(ciphertext)

# Remove padding
padding_len = flag_padded[-1]
flag = flag_padded[:-padding_len]

print("Decrypted Flag:", flag.decode('utf-8'))
