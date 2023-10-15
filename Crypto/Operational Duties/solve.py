import random

def obfuscate_key(shared_key):
    obfuscated_key = shared_key.to_bytes((shared_key.bit_length() + 7) // 8, byteorder='big')
    return int.from_bytes([x ^ 0xFF for x in obfuscated_key], byteorder='big')

def deobfuscate_key(obfuscated_key, shared_key):
    obfuscated_bytes = obfuscated_key.to_bytes((obfuscated_key.bit_length() + 7) // 8, byteorder='big')
    deobfuscated_bytes = bytes([x ^ 0xFF for x in obfuscated_bytes])
    return int.from_bytes(deobfuscated_bytes, byteorder='big') ^ shared_key

# Given values
p = 137
q = 11
alice_secret = random.randint(1, q - 1)
bob_secret = random.randint(1, q - 1)
alice_shared_key = pow(p, alice_secret, q)
bob_shared_key = pow(p, bob_secret, q)
obfuscated_alice_key = obfuscate_key(alice_shared_key)

# Given encrypted flag
encrypted_flag = 7091022811630043496454715564459978004849567585581799855855165734358

# De-obfuscate Alice's key using Bob's shared key
deobfuscated_alice_key = deobfuscate_key(obfuscated_alice_key, bob_shared_key)
