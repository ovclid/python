import sys
import binascii
import ctypes
import bitstring

def mem_info(var_x, var_name = "변수 정보"):
    print()
    print(f"------------- {var_name} -----------")
    print("타입 : ", type(var_x))

    if (type(var_x) == int):
        print("값(10진수), 값(16진수) : ", var_x, hex(var_x))

    #print("메모리 주소(10진수) : ", id(var_x))
    print("메모리 주소(16진수) : ", hex(id(var_x)))
    #print("메모리 주소(16진수) : ", var_x.__str__)

    print("메모리 사이즈(바이트) : ", sys.getsizeof(var_x))
    
    print("메모리 내용(바이트) : ", binascii.hexlify(ctypes.string_at(id(var_x), sys.getsizeof(var_x))))

    hex1 = binascii.hexlify(ctypes.string_at(id(var_x), sys.getsizeof(var_x)))
    hex_string = '0x' + hex1.decode()
    
    #print("메모리 내용(비트) : ", bitstring.BitArray(hex_string).bin)


def f2(x):
    mem_info(x, "[[[3. f2(x) 함수 호출!!!]]] f2(x)의 매개변수 x")
    
    x = x + 1
    mem_info(x, "[[[3. f2(x) 함수]]] x = x + 1")
    
    return x
    mem_info(x, "[[[3. f2(x) 함수]]] return x")

def f1(x):
    mem_info(x, "[[2. f1(x) 함수 호출!!!]] f1(x)의 매개변수 x")
             
    x = x * 2
    mem_info(x, "[[2. f1(x) 함수]] x = x *2 명령 -> x 정보")
        
    y = f2(x)
    mem_info(y, "[[2. f1(x) 함수]] y = f2(x) 명령 -> y 정보")
    
    return y
    mem_info(y, "[[2. f1(x) 함수]] return y 명령 -> y 정보")


if __name__ == '__main__':
    
    print(f"------------- [1. 메인함수] 호출!!! -----------")
    mem_info(__name__, "[1. 메인함수]")
    
    y = 5
    mem_info(y, "[1. 메인함수] y = 5 명령 -> y 정보")

    print(id(f1))
          
    z = f1(y)
    mem_info(z, "[1. 메인함수] z = f1(y) 명령 -> z 정보")


    li = ["가규", "25", "54", "100"]
    mem_info(li, "li")

    for i in range(len(li)):
        mem_info(li[i], f"li + {i}")
	
