import hashlib

a = hashlib.md5('http://www.rapidtables.com/convert/number/hex-to-decimal.htm'.encode('utf-8'))
b = a.hexdigest()
print(b)


#hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
#'cd183a211ed2434eac4f31b317c573c50e6c24e3a28b82ddcb0bf8bedf387a9f' 