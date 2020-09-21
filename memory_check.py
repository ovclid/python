from ctypes import string_at
from sys import getsizeof
from binascii import hexlify

a = 12314
print(hexlify(string_at(id(a), getsizeof(a))))
