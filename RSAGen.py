# contributors: chum8
# https://github.com/chum8
# Evolve Security Academy Module 9 - homework assigment
# Copyright (c) 2018-2019

# import libraries
import sys
from Crypto.PublicKey import RSA

# default variables
default_extension_public = ".pem"
default_extension_private = ".key"

# capture names of keys from terminal
try:
    # if one argument given, both keys have same name.
    # if two arguments, name the public key according to the second argument.
    if (len(sys.argv) == 2):
        private_key_name = sys.argv[1]
        public_key_name = sys.argv[1]
    elif (len(sys.argv) > 2):
        private_key_name = sys.argv[1]
        public_key_name = sys.argv[2]
    else:
        private_key_name = str(input("Enter a name for the private key file (no extension): "))
        public_key_name = str(input("Enter a name for the public key file (no extension): "))
    prv_file = private_key_name + default_extension_private
    pub_file = public_key_name + default_extension_public

except:
    print("There was an error creating the key names.\nExiting.")
    sys.exit()

# see if user is ready to proceed
proceed = input("Your private key file name is\n" + prv_file + "\nYour public key name is\n" + pub_file + "\nKeys will be generated.\nType 'q' to cancel or ENTER to proceed: ")
if proceed.lower() == 'q':
    print("User canceled operation.\nExiting.")
    sys.exit()

# attempt to generate keys and save to files
try:
    print("Generating private key.")
    my_private_key = RSA.generate(2048)
    print("Generating public key.")
    my_public_key = my_private_key.publickey()
    with open(prv_file, 'wb') as f1:
        f1.write(my_private_key.exportKey('PEM'))
    with open(pub_file, 'wb') as f2:
        f2.write(my_public_key.exportKey('PEM'))
    print("Writing keys to files.")
    print("Success! Keys may be found at '" + prv_file + "' and '" + pub_file + "'.\nExiting.")

except:
    print("There was a problem generating the keys!\nExiting.")

sys.exit()

