from Crypto.Util.number import *

p = getPrime(2048)
q = getPrime(2048)
phi = (p-1) * (q-1)
e = 7
d = inverse(e, phi)
n = p * q
phi = (p - 1) * (q - 1)
plain_Text = 0x4B4354466A727B5235415F4C30775F4944582D34747434636B7D

print "n = %#x" % n
print "e = %#x" % e
print "c = %#x" % pow(plain_Text, e, n)