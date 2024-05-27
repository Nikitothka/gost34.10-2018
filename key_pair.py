import random
from constants import n, Gx, Gy
from ec_point import ECPoint

class ECKeyPair:
    def __init__(self):
        self.d = random.randrange(1, n)
        G = ECPoint(Gx, Gy)
        self.Q = G.mul(self.d)

def generate_keys():
    return ECKeyPair()
