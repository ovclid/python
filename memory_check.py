from ctypes import string_at
from sys import getsizeof
from binascii import hexlify

a = 12314
print(hexlify(string_at(id(a), getsizeof(a))))

r = open("전체무장.txt", "r")
result = r.read()

file = open('전체무장_메모리모습.txt', 'w')
file.write(str(hexlify(string_at(id(result), getsizeof(result)))))
file.close()

for i in range(10):
	print(ord(result[i]), hex(ord(result[i])), bin(ord(result[i])))

