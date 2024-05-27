import hashlib
import random
from constants import p, n, Gx, Gy
from ec_point import ECPoint

# Хэш-функция ГОСТ (используем SHA-256 для примера)
def gost_hash(message):
    return hashlib.sha256(message).digest()

class ECSignature:
    @staticmethod
    def generate_signature(message, private_key):
        e = int.from_bytes(gost_hash(message), byteorder='big')
        if e == 0:
            e = 1
        while True:
            k = random.randrange(1, n)
            G = ECPoint(Gx, Gy)
            R = G.mul(k)
            r = R.x % n
            if r == 0:
                continue
            s = (r * private_key + k * e) % n
            if s != 0:
                break
        return (r, s)

    @staticmethod
    def verify_signature(message, signature, public_key):
        r, s = signature
        if not (1 <= r < n and 1 <= s < n):
            return False
        e = int.from_bytes(gost_hash(message), byteorder='big')
        if e == 0:
            e = 1
        v = pow(e, -1, n)
        z1 = (s * v) % n
        z2 = (-r * v) % n
        G = ECPoint(Gx, Gy)
        R = G.mul(z1) + public_key.mul(z2)
        if R.x % n == r:
            return True
        return False

def sign_file(file_path, key_pair):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    signature = ECSignature.generate_signature(file_data, key_pair.d)
    return signature

def verify_file(file_path, signature, key_pair):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    is_valid = ECSignature.verify_signature(file_data, signature, key_pair.Q)
    return is_valid
