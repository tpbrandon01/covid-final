import socket
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

# 可以加密並上傳(位置、id、時間戳)給server
# 可以回報自己確診
# 可以拉下公告資料 確定自己沒有受感染

def public_key_encrypt(public_key_pos):
    with open(public_key_pos) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_en = cipher.encrypt(temp.encode('utf-8'))
        cipher_text = base64.b64encode(cipher_en)
    return cipher_text

def private_key_decrypt(private_key_pos, cipher_text):
    random_generator = Random.new().read
    with open(private_key_pos) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(cipher_text), random_generator)
    return text



# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)
# 
# print('Received', repr(data))

if __name__ == "__main__":
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server
        
    temp = {}
    temp['_id'] = 'sexycat'
    temp['location'] = 'W hotel'
    temp = str(temp)
    print(temp)
    
    crypted_temp = public_key_encrypt('key_data/master-public.pem')
    de_crypted_temp = private_key_decrypt('key_data/master-private.pem', crypted_temp)
    print(crypted_temp)
    print(de_crypted_temp)