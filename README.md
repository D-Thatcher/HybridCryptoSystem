# HybridCryptoSystem
A library of functions built around PyCrypto that combines asymmetric encryption using a public key, with the symmetric encryption of files

# Purpose
One of the benefits of symmetric encryption is its efficiency. Though, often we need to separate the key that is used to encrypt the files (public key) with the key used to decrypt them (private key). This feature is a property of asymmetric encryption, but notably decreases its performance. This suggests using a combination of which, wherein, one can issue a public key that can be used to encrypt a symmetric encryption key, which can then be securely transfered. Further, we can use a new symmetric encryption key each time, without requiring another handshake as the asymmetric key pair can remain the same.

# Main Methods:

* export_data: encrypts the inputted serializable data using a fresh symmetric key, and returns it along with an encrypted version of this symmetric key. The symmetric key is encrypted using the public key passed as a parameter

* import_data: requires the private key, so it can use it to decrypt the symmetric file encryption key, which is then used to decrypt the inputted data
