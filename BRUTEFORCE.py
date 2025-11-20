#!/usr/bin/env python
### Name: Nebojsa Simic
###  BRUTEFORCE.py
###  Brute-force attack on EncryptForFun.py encryption
###  Tries all possible 2-character keys (digits and letters)

import sys
from BitVector import *

# Read the encrypted file
FILEIN = open('encrypted.txt')
encrypted_bv = BitVector(hexstring = FILEIN.read())
FILEIN.close()

# Read the expected plaintext
FILEIN = open('plain.txt')
expected_plaintext = FILEIN.read()
FILEIN.close()

# Constants
PassPhrase = "Hopes and dreams of a million years"
BLOCKSIZE = 16
numbytes = BLOCKSIZE // 8

# Reduce the passphrase to a bit array of size BLOCKSIZE
bv_iv = BitVector(bitlist = [0]*BLOCKSIZE)
for i in range(0, len(PassPhrase) // numbytes):
    textstr = PassPhrase[i*numbytes:(i+1)*numbytes]
    bv_iv ^= BitVector(textstring = textstr)

# Create the character set: digits (0-9) and letters (a-z, A-Z)
charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("Starting brute-force attack...")
print("Total keys to try: 3844 (62 x 62)")
print()

# Try all possible 2-character combinations
attempts = 0
found = False

for char1 in charset:
    if found:
        break
    for char2 in charset:
        key = char1 + char2
        attempts += 1
        
        # Show progress every 100 attempts
        if attempts % 100 == 0:
            print(f"Tried {attempts} keys. Current: {key}")
        
        # Reduce the key to a bit array of size BLOCKSIZE
        key_bv = BitVector(bitlist = [0]*BLOCKSIZE)
        for i in range(0, len(key) // numbytes):
            keyblock = key[i*numbytes:(i+1)*numbytes]
            key_bv ^= BitVector(textstring = keyblock)
        
        # Create a bitvector for storing the decrypted plaintext bit array
        msg_decrypted_bv = BitVector(size = 0)
        
        # Carry out differential XORing of bit blocks and decryption
        previous_decrypted_block = bv_iv
        for i in range(0, len(encrypted_bv) // BLOCKSIZE):
            bv = encrypted_bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]
            temp = bv.deep_copy()
            bv ^= previous_decrypted_block
            previous_decrypted_block = temp
            bv ^= key_bv
            msg_decrypted_bv += bv
        
        # Extract plaintext from the decrypted bitvector
        try:
            outputtext = msg_decrypted_bv.get_text_from_bitvector()
            
            # Check if the decrypted text matches the expected plaintext
            if outputtext == expected_plaintext:
                print()
                print("="*60)
                print("KEY FOUND!")
                print("="*60)
                print(f"Encryption key: {key}")
                print(f"Total attempts: {attempts}")
                print("="*60)
                found = True
                break
        except:
            # Skip keys with invalid texts
            continue

print()
if not found:
    print("Key not found after trying all possibilities.")