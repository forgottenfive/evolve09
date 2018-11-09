# contributors: chum8
# https://github.com/chum8
# Evolve Security Academy Module 9 - homework assigment
# Copyright (c) 2018-2019

# import libraries
import sys
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

# default variables
default_extension = ".enc"
default_extension_public = ".pub"

# capture names of keys from terminal
try:
    # first argument = name of key
    # second argument = name of plaintext file
    if (len(sys.argv) == 2):
        pub_file = sys.argv[1]
        text_file = str(input("Enter the name of the plaintext file: "))
    elif (len(sys.argv) > 2):
        pub_file = sys.argv[1]
        text_file = sys.argv[2]
    else:
        pub_file = str(input("Enter the name of the public key file: "))
        text_file = str(input("Enter the name of the plaintext file: "))
    write_file = text_file + default_extension

except:
    print("Could not stat public key and plaintext file names.\nExiting.")
    sys.exit()

# see if user is ready to proceed
proceed = input("Your public key file name is\n" + pub_file + "\nYour plaintext file name is\n" + text_file + "\nType 'q' to cancel or ENTER to proceed to encryption: ")
if proceed.lower() == 'q':
    print("User canceled operation.\nExiting.")
    sys.exit()

# attempt to encrypt the file using the key given
#try:

print("Reading public key.")
with open(pub_file, 'r') as f1:
    key = RSA.importKey(f1.read())
    # print(key) # debug line

print("Encrypting plaintext.")
with open(text_file, 'r') as f2:
    data = f2.read().encode()
    # print(data) # debug line

# do the encryption
# referred to pycryptodome.readthedocs.io/en/latest/src/examples.html
session_key = get_random_bytes(16)
cipher_rsa = PKCS1_OAEP.new(key)
enc_session_key = cipher_rsa.encrypt(session_key)

cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

print("Writing to file.")
with open(write_file, 'wb') as f3:
    [ f3.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
print("Success! Encrypted data written to '" + write_file + "'.\nExiting.")

#except:
#print("There was a problem encrypting the plaintext!\nExiting.")
sys.exit()

