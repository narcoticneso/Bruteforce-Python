Brute-Force Cryptanalysis

Author: Nebojsa Simic
Date: 11/20/2025

DESCRIPTION:
------------
This program performs a brute-force attack on the EncryptForFun.py encryption
scheme to recover the encryption key. It systematically tries all possible
2-character keys composed of digits (0-9) and letters (a-z, A-Z), totaling
3,844 possible combinations.

FILES INCLUDED:
---------------
- BRUTEFORCE.py         : Main brute-force attack program
- EncryptForFun.py      : Original encryption script
- DecryptForFun.py      : Original decryption script
- BitVector.py          : BitVector module required for encryption/decryption
- plain.txt             : Original plaintext file
- encrypted.txt         : Encrypted version of plain.txt
- README                : This file

REQUIREMENTS:
-------------
- Python 3.x
- BitVector module (included)

HOW TO RUN:
-----------
1. Ensure all files are in the same directory

2. Run the brute-force attack program:
   $ python3 BRUTEFORCE.py

   OR
   
   $ python BRUTEFORCE.py

3. The program will:
   - Try all 3,844 possible 2-character keys
   - Display progress every 100 attempts
   - Print the found key when successful

EXPECTED OUTPUT:
----------------
The program will display progress updates and eventually output:

============================================================
KEY FOUND!
============================================================
Encryption key: ZZ
Total attempts: 3844
============================================================

ALGORITHM:
----------
1. Read the encrypted file (encrypted.txt) and expected plaintext (plain.txt)
2. Generate all possible 2-character keys from charset: 
   '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
3. For each key:
   a. Reduce key to 16-bit BitVector
   b. Perform differential XOR decryption (same as DecryptForFun.py)
   c. Compare decrypted text with expected plaintext
   d. If match found, display key and exit
4. If no match found after all attempts, report failure

VERIFICATION:
-------------
To verify the found key works correctly:
$ echo "ZZ" | python3 DecryptForFun.py encrypted.txt recovered.txt
$ diff plain.txt recovered.txt

If diff produces no output, the files are identical and the key is correct.

TIME COMPLEXITY:
----------------
- Key space: 62 × 62 = 3,844 keys
- Running time: Approximately 5-10 seconds on typical hardware

NOTES:
------
- The effective key size is 16 bits with BLOCKSIZE=16
- The program uses the same PassPhrase as the original scripts:
  "Hopes and dreams of a million years"
- No external libraries beyond BitVector are required
- The program handles exceptions for invalid decryption attempts
