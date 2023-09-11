# The `import secrets` statement is importing the `secrets` module, which provides functions for
# generating secure random numbers. This module is used to generate a random key for encryption.
import secrets
from cryptography.fernet import Fernet

# `key = Fernet.generate_key()` is generating a new key for the Fernet encryption algorithm. Fernet is
# a symmetric encryption algorithm that uses the AES encryption algorithm in CBC mode with a 128-bit
# key. 
key = Fernet.generate_key()

# The code `with open("app/Secret.key", "wb") as key_file: key_file.write(key)` is opening a file
# named "Secret.key" in binary write mode ("wb"). It then writes the contents of the `key` variable to
# the file. The `with` statement ensures that the file is properly closed after the write operation is
# complete.
with open("app/Secret.key", "wb") as key_file:
    key_file.write(key)
