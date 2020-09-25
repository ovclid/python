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

if __name__ == '__main__':

    f = open("전체무장.txt", "r")

    all_string = []
    all_string_split = []
    
    for i in range(0, 5):
        
        mem_info(all_string, "readline 스트링")
        print(all_string)

        mem_info(all_string_split, "readline 스트링 -> split -> []")
        print(all_string_split)
        
        temp = f.readline()
        all_string.append(temp)
        all_string_split.append(temp.split())
        
        #mem_info(li[i], f"li + {i}")
	
