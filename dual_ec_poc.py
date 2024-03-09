from sage.all import *
from Crypto.Util.number import bytes_to_long
from tqdm import tqdm
import os

# Define P-256 NIST curve
F = GF(0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF)
E = EllipticCurve(F, [0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC, 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B])
G = E(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296, 0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5)

# Define our backdoored parameters
P = E(82608569474992041160607468321330734781976984380007427368012865557687600622709, 35069256181227824748874498744049288021402083829396944376506375002277135146766)
Q = E(68591188472354879747328317058906844645177467663739837928564927062831392289075, 15888879496168196980339481261464724364252576207648998829690789725407441371252)
backdoor = 123456789 # psst... this is a secret!! Q = 123456789 * P (only we know about this relationship)

state = bytes_to_long(os.urandom(16)) # some random initial state

def get_random_num(): # returns 30-byte long random number using a military grade dice throwing mechanism
    global state
    r = (state * P)[0] # x coordinate of s*P
    state = (r * P)[0] # x coordinate of r*P

    return int((r * Q)[0]) & (2**240 - 1) # x coordinate of r*Q, we remove the first two bytes to make it look secure

r1 = get_random_num()
r2 = get_random_num()

for i in tqdm(range(2**16)):
    guess = Integer((i << 240) | r1)

    try:
        point = E.lift_x(guess)
    except: # no point on curve with given x coordinate
        continue
    
    state = (pow(backdoor, -1, E.order()) * point)[0]
    r = (state * P)[0]
    out = int((r * Q)[0]) & (2**240 - 1)

    if out == r2:
        print("Found state", state)
        break