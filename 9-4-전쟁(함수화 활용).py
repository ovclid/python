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
    print("---------------------------------------------------------------------")
    select = input("명령을 선택하시오(1.검색, 2.등용, 3.해임, 4.정보, 5.전쟁, 6. 종료) : ")

    if (select == '1'):     # 장수 검색
        search_select = input("검색 방법을 선택하시오(1. 이름, 2. 번호, 3. 능력) : ")
        
        if (search_select == '1'):   # 장수 검색 - 이름으로 검색
            name = input("무장의 이름을 입력하시오 : ")
            for i in range(len(all_info)):
                if (all_info[i][0] == name):
                    print(all_info[i])

        elif (search_select == '2'):  # 장수 검색 - 번호로 검색
            start = int(input("시작 번호(1~" + str(len(all_info)) + ") : "))
            end = int(input("마지막 번호(" + str(start + 1) + "~" + str(len(all_info)) + ") : "))
            for i in range(start-1, end):
                print(all_info[i])

        elif (search_select == '3'): # 장수 검색 - 무력으로 검색
            ability_select = int(input("능력을 선택하시오(1. 통솔, 2. 무력, 3. 지력) : "))
            start = int(input("시작 능력(1~100) : "))
            end = int(input("마지막 능력(" + str(start + 1) + "~100) : "))
            for i in range(len(all_info)):
                if (int(all_info[i][ability_select]) >= start and int(all_info[i][ability_select]) <= end):
                    print(all_info[i])
                    
        else:
            continue
                
    elif (select == '2'):   # 장수 등용
        general_list = []
        for i in range(random.randint(1, 10)):
            random_num = random.randint(1, 676)
            general_list.append(all_info[random_num])
            
            print(i+1, all_info[random_num])
            time.sleep(0.3)

        choice = input("무장 하나를 선택하시오 : ")

        if (choice >= '1' and choice <= str(len(general_list))):
            my_choice.append(general_list[int(choice)-1])
            print(general_list[int(choice)-1][0], "를 선택하였습니다.")
            print("등용한 무장은 현재 ", len(my_choice), "명 입니다.")
            for i in my_choice:
                print(i[0])
        else:
            continue
        
    elif (select == '3'):   # 장수 해임
        for i in range(len(my_choice)):
            print(i+1, my_choice[i])

        choice = int(input("해임 할 무장 하나를 선택하시오 : "))

        if (choice >=1 and choice <= len(my_choice)):
            del my_choice[choice-1]
        else:
            print("무장을 선택하지 않았습니다.")
            
    elif (select == '4'):   # 현재 상태
        print("전체 장수 : ", len(all_info))
        print("등용 장수 : ", len(my_choice))
        
        for i in my_choice:
            print(i)
            
    elif (select == '5'):   # 전쟁
        enemy_list = []
        for i in range(random.randint(1, len(my_choice)+2)):
            random_num = random.randint(1, len(all_info))
            enemy_list.append(all_info[random_num])
            
            print(i+1, enemy_list[random_num])
            time.sleep(0.3)

        show_info()
        
    elif (select == '6'):  # 종료
        break
    else :
        print("잘못된 입력입니다.")
    
read_file.close()


