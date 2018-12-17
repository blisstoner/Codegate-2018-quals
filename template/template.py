# 0x6161 -> 'AA'
def hexint2str(x):
  import binascii
  s = hex(x)[2:]
  if len(s) % 2 == 1: s = '0'+s
  return binascii.unhexlify(s).decode()

def gcd(a, b):
  if a == 0: return b
  return gcd(b%a, a)

def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  g, y, x = egcd(b%a,a)
  return (g, x - (b//a) * y, y)

def inv(a, m):
  g, x, y = egcd(a, m)
  if g != 1:
    raise Exception('No modular inverse')
  return x%m

# x**2 = a (mod m), m is prime
def quad_congruence_equation(a, m):
  assert((m+1)%4 == 0)
  return pow(a, (m+1)//4, m)

# m must satisfies pairwise relatively prime
def crt(a, m):
  n = len(m)
  ret = a[0]
  mod = m[0]
  for i in range(1,n):
    m1 = mod
    mod *= m[i]
    m2inv = inv(m[i],m1)
    m1inv = inv(m1,m[i])
    ret = (ret*m[i]*m2inv+a[i]*m1*m1inv)%mod
  return ret