import random
import time

read_file = open("전체무장.txt", "r")

all_info = []
while True:
    read_info = read_file.readline()
    if read_info != '':
        all_info.append(read_info.split())
    else:
        break

print("전체 장수 : ", len(all_info))
print("맨처음 장수 : ", all_info[0])
print("마지막 장수 : ", all_info[len(all_info)-1])
print()

my_choice = []

while True:
    select = input("명령을 선택하시오(1.검색, 2.등용, 3.해임, 4.정보, 5.전쟁, 6. 종료) : ")

    if (select == '1'):     # 장수 검색
        name = input("무장의 이름을 입력하시오 : ")
        for i in range(len(all_info)):
            if (all_info[i][0] == name):
                print(all_info[i])
                
    elif (select == '2'):   # 장수 등용
        general_list = []
        for i in range(random.randint(1, 10)):
            random_num = random.randint(1, 676)
            general_list.append(all_info[random_num])
            
            print(i+1, all_info[random_num])
            time.sleep(0.3)

        choice = int(input("무장 하나를 선택하시오 : "))

        if (choice >=1 and choice <= len(general_list)):
            my_choice.append(general_list[choice-1])
            print(general_list[choice-1][0], "를 선택하였습니다.")
            print("등용한 무장은 현재 ", len(my_choice), "입니다")
            for i in my_choice:
                print(i[0])
                
    elif (select == '3'):   # 장수 해임
        pass
    elif (select == '4'):   # 현재 상태
        pass
    elif (select == '5'):   # 전쟁
        pass
    elif (select == '6'):  # 종료
        break
    else :
        print("잘못된 입력입니다.")
    
read_file.close()


