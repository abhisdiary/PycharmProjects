import _pysha3

data = 'maydata'
s = _pysha3.sha3_224(data.encode('utf-8')).hexdigest()
print(s)

data2 = 'my_data'
t = _pysha3.sha3_512(data2.encode('utf-8')).hexdigest()
print(t)
