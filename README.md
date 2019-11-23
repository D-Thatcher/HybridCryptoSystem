# HybridCryptoSystem
A library of functions built around PyCrypto that combines asymmetric encryption using a public key, with the symmetric encryption of files

# Purpose
The main motivation of symmetric encryption is its efficiency. While, the benefit of asymmetric encryption is that a different key is used to encrypt files (public key) than is used to decrypt them (private key). This suggests using a combination of which, wherein, one can issue a public key that can be used to encrypt a symmetric encryption key, which can then be securely transfered.

# Main Methods:

* export_data: encrypts the inputted serializable data using a fresh symmetric key, and returns it along with an encrypted version of this symmetric key. The symmetric key is encrypted using the public key passed as a parameter

* import_data: requires the private key, so it can use it to decrypt the symmetric file encryption key, which is then used to decrypt the inputted data
