import sys
import binascii
import ctypes
import bitstring

def mem_info(var_x, var_name):
    print(f"------------- 변수 {var_name} 정보 -----------")
    print("타입 : ", type(var_x))

    if (type(var_x) == int):
        print("값(10진수), 값(16진수) : ", var_x, hex(var_x))

    print("메모리 주소(10진수) : ", id(var_x))
    print("메모리 주소(16진수) : ", hex(id(var_x)))
    print("메모리 주소(16진수) : ", var_x.__str__)

    print("메모리 사이즈(바이트) : ", sys.getsizeof(var_x))
    
    print("메모리 내용(바이트) : ", binascii.hexlify(ctypes.string_at(id(var_x), sys.getsizeof(var_x))))

    hex1 = binascii.hexlify(ctypes.string_at(id(var_x), sys.getsizeof(var_x)))
    hex_string = '0x' + hex1.decode()
    
    print("메모리 내용(비트) : ", bitstring.BitArray(hex_string).bin)


x = 10

mem_info(x, 'x')


y = x
mem_info(y, 'y')
if (id(x) == id(y)):
    print(" x and y refer to the same object")

x = x + 1
mem_info(x+1, 'x+1')
if (id(x) != id(y)) :
    print(" x and y refer to the Different object")

z = 10
mem_info(z, 'z')
if (id(y) == id(x)):
    print("y and z point to the Same memory!!")
else:
    print("y and z point to Different memory!!")
