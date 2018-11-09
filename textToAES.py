# import libraries
import sys
from Crypto.Cipher import AES
from Crypto import Random

# default variables
default_extension = ".enc"

# capture a filename from terminal and attempt to open
try:
    if (len(sys.argv) > 1):
        my_file = sys.argv[1]
    else:
        my_file = input("Type a filename: ")
    result_file = my_file + default_extension
    with open (my_file, 'r') as f:
        data = f.read()

except:
    print("Unable to open the file.  Legal file name not specified, or file does not exist.  Exiting.")
    exit()

# see if user is ready to proceed
proceed = input("File '" + my_file +  "' will be encrypted using AES and output as '" + result_file + "'.  Type 'q' to cancel or ENTER to proceed: ")
if proceed.lower() == 'q':
    print("User canceled operation.  Exiting.")
    exit()

# encrpyt file
print("Encrypting...")

#try:
#key = b'lP11dbkRATxS8LuG'
key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
result = iv + cipher.encrypt(data.encode('utf8'))
print(result)
#except:
