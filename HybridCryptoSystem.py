from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP,AES
import os
import pickle

def generate_private_key(sz=1024):
    random_generator = Random.new().read
    key = RSA.generate(sz, random_generator) #generate pub and priv key
    return key

def get_public(key):
    return key.publickey()

def encrypt(public_key, data):
    encryptor = PKCS1_OAEP.new(public_key)
    return encryptor.encrypt(data)

def decrypt(key, data):
    decryptor = PKCS1_OAEP.new(key)
    return decryptor.decrypt(data)

def save_key(key, name):
    with open(name,'wb') as ef:
        ef.write(key.exportKey('PEM'))

def read_key(name):
    assert os.path.exists(name)
    with open(name,'rb') as ef:
        key = RSA.import_key(ef.read())
    return key

def generate_symmetric_pair():
    rndfile = Random.new()
    skey = rndfile.read(16)
    siv = Random.new().read(AES.block_size)
    return skey, siv

def new_symmetric_encryption(input_data, skey, siv):
    if not hasattr(input_data, "tostring"):
        data = pickle.dumps(input_data)
    else:
        data = input_data.tostring()

    cfb_cipher = AES.new(skey, AES.MODE_CFB, siv)
    enc_data = cfb_cipher.encrypt(data)
    return enc_data

def symmetric_decryption(enc_data,skey, siv):
    cfb_decipher = AES.new(skey, AES.MODE_CFB, siv)
    plain_data = cfb_decipher.decrypt(enc_data)
    return plain_data

#
if __name__ =='__main__':

    # Person 1
    #___________________________________________________
    # Generate a private key
    key = generate_private_key()

    # Using the private key, generate a corresponding public key
    public_key = get_public(key)

    # Save the public key
    save_key(public_key,'my_public_key.pem')

    # Save the private key
    save_key(key,'my_private_key.pem')

    # Person 2
    # ___________________________________________________

    # Get the public key from Person 1
    key_from_file = read_key('my_public_key.pem')

    # Generate a symmetric key & iv
    skey, siv = generate_symmetric_pair()


    import cv2,numpy
    frame = cv2.imread('UNDER-MAINTENANCE.png')
    ret, frame_jpg = cv2.imencode('.jpg', frame)

    # Encrypt our data with the symmetric key
    enc_data = new_symmetric_encryption(frame_jpg, skey, siv)

    # Encrypt our symmetric key with the public key
    enc_skey = encrypt(key_from_file,skey)
    enc_siv = encrypt(key_from_file,siv)

    # Person 1
    # ___________________________________________________

    # Get the encrypted data and encrypted symmetric key from Person 2

    # Decrypt the symmetric key with the private key
    dskey = decrypt(key, enc_skey)
    dsiv = decrypt(key, enc_siv)

    # Decrypt the data with the symmetric key
    data = symmetric_decryption(enc_data,skey,siv)

    nparr = numpy.fromstring(data, numpy.uint8)
    img = cv2.imdecode(nparr,cv2.IMREAD_COLOR)

    cv2.imshow('',frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






