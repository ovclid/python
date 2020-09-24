import sys
import binascii
import ctypes
import bitstring

x = 1000
        
print(f" x = {x} 명령에 의한 {type(x)} 형의 변수 생성 과정")
print("---------------------------------------------------------------")
print(f"1 단계 : 파이썬 객체(PyObject) 하나를 생성")

hex1 = binascii.hexlify(ctypes.string_at(id(x), sys.getsizeof(x)))
print(f"2 단계 : 생성된 객체의 타입 코드를 {hex1[16:28]}로 설정, {type(x)}형 코드")

if (type(x) == int):
    print(f"3 단계 : 생성된 객체의 값을 {x}로 설정, 16진수로는 {hex(x)}")
elif (type(x) == str and len(x) == 1):
    print(f"3 단계 : 생성된 객체의 값을 {x}로 설정, 16진수로는 {hex(ord(x))}")
else:
    print(f"3 단계 : 생성된 객체의 값을 {x}로 설정")
    

print(f"4 단계 : x라 불리우는 이름 생성")

print(f"5 단계 : x의 id를 생성된 객체의 (시작)주소 {hex(id(x))}로 설정")

print(f"6 단계 : x의 참조 갯수를 1개 증가 {hex1[0:4]} ")
print("---------------------------------------------------------------")

print(f"생성된 {x} 객체 크기 : ", sys.getsizeof(x))
print(f"생성된 {x} 객체 메모리 : ", hex1)

hex_string = '0x' + hex1.decode()
print("생성된 {x} 객체 메모리(비트) : ", bitstring.BitArray(hex_string).bin)    

