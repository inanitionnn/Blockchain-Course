def messToHex(message):
  hexVal = hex(int(str.encode(message).hex(),16))
  return hexVal[2:]
def messInBits(message):
  messInBytes = str.encode(message)
  messInBits = ""
  for byte in messInBytes:
    strByte = bin(byte)[2:]
    fullStrByte = "0" * (8 - len(strByte)) + strByte
    messInBits += fullStrByte
  return messInBits
def binToHex(b):
  return hex(int(b,2))[2:]
def strToInt(string):
  return int(string, 16)

def hexXor(a, b):    # xor two hex strings of the same length
  return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(a, b)])
def hexOr(a, b):    # xor two hex strings of the same length
  return "".join(["%x" % (int(x,16) | int(y,16)) for (x, y) in zip(a, b)])
def hexAnd(a, b):    # xor two hex strings of the same length
  return "".join(["%x" % (int(x,16) & int(y,16)) for (x, y) in zip(a, b)])
def hexNot(a):
  return hex(~int(a,16))[3:]
def leftRotate(x, n):
    x = strToInt(x)
    return hex((x << n)|(n >> (32 - n)))[2:]
def getSHA1Hash(message):
  h0 = "67452301"
  h1 = "EFCDAB89"
  h2 = "98BADCFE"
  h3 = "10325476"
  h4 = "C3D2E1F0" 
  m = messInBits(message)
  ml = len(m)
  
  if ml / 447 % 1 > 0:
    r = ml // 447 + 1
  else: r = ml // 447
  mod = 1<<32
  for i in range(r):
    currChunk512 = (m[447 * i : 447 * (i + 1)]) 
    fullChunk512 = currChunk512 + "1" + "0" * (447 - len(currChunk512)) + "0" * (66 - len(bin(ml))) + bin(ml)[2:]
    chunks32 = []
    for j in range(16):
      chunks32.append(binToHex(fullChunk512[32 * j : 32 * (j + 1)]))
    for n in range(16, 40):
      chunks32.append(leftRotate(hexXor(hexXor(chunks32[n-3], chunks32[n-8]), hexXor(chunks32[n-14],chunks32[n-16])), 5))
      a = h0
      x = h1
      y = h2
      z = h3
      e = h4
      
      for k in range(39): 
        if (0 <= k <= 19):
          f = hexOr(hexAnd(x, y), hexAnd(hexNot(x), z)) 
          # f = (b & c) | ((~b) & d)
          t = "5A827999"
        elif (20 <= k <= 39):
          f = hexXor(hexXor(x,y), z)
          # f = b ^ c ^ d
          t = "6ED9EBA1"
        elif (40 <= k <= 59):
          f = hexOr(hexOr(hexAnd(x,y), hexAnd(x, z)), hexAnd(y, z))
          # f = (b & c) | (b & d) | (c & d) 
          t = "8F1BBCDC"
        elif (60 <= k <= 79):
          f = hexXor(hexXor(x, y), z)
          # f = b ^ c ^ d
          t = "CA62C1D6"
        temp = hex(((((strToInt(leftRotate(a, 5)) + strToInt(f))%mod + strToInt(e))%mod + strToInt(t))%mod + strToInt(chunks32[n]))%mod)[2:]
        e = z
        z = y
        y = leftRotate(x, 30)
        x = a
        a = temp
      h0 = hex((strToInt(h0) + strToInt(a))%mod)[2:]
      h1 = hex((strToInt(h1) + strToInt(x))%mod)[2:] 
      h2 = hex((strToInt(h2) + strToInt(y))%mod)[2:]
      h3 = hex((strToInt(h3) + strToInt(z))%mod)[2:]
      h4 = hex((strToInt(h4) + strToInt(e))%mod)[2:]
  return hex((strToInt(h0)<<128) | (strToInt(h1)<<96) | (strToInt(h2)<<64) | (strToInt(h3)<<32) | strToInt(h4))[2:]
  
  

print(getSHA1Hash("abc"))