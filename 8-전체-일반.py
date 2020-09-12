import random
import time

read_file = open("전체무장.txt", "r")

all_info = []
my_choice = []
my_gold = 10000
recruit_fee = 3000
my_hp = 100

while True:
    read_info = read_file.readline()
    if read_info != '':
        all_info.append(read_info.split())
    else:
        break
                
while True:
    select = input("명령을 선택하시오(1.검색, 2.등용, 3.해임, 4.정보, 5.전쟁, 6. 종료) : ")

    if (select == '1'):
        search_select = input("검색 방법을 선택하시오(1. 이름, 2. 번호, 3. 능력) : ")
        
        if (search_select == '1'):
            name = input("무장의 이름을 입력하시오 : ")
            for i in range(len(all_info)):
                if (all_info[i][0] == name):
                    print(all_info[i])

        elif (search_select == '2'):
            start = int(input("시작 번호(1~676) : "))
            end = int(input("마지막 번호(" + str(start + 1) + "~676) : "))

            for i in range(start-1, end):
                print(all_info[i])

        elif (search_select == '3'):
            ability_select = int(input("능력을 선택하시오(1. 통솔, 2. 무력, 3. 지력) : "))

            start = int(input("시작 능력(1~100) : "))
            end = int(input("마지막 능력(" + str(start + 1) + "~100) : "))

            for i in range(len(all_info)):
                if (int(all_info[i][ability_select]) >= start and int(all_info[i][ability_select]) <= end):
                    print(all_info[i])
        else:
            break

    elif (select == '2'):   # 장수 등용
        my_gold = my_gold - 1000
        print("소지금이 1000 차감 되어 현재 ", my_gold, "보유중입니다")
        
        general_list = []
        for i in range(random.randint(1, 10)):
            random_num = random.randint(1, 676)
            general_list.append(all_info[random_num])
            
            print(i+1, all_info[random_num])
            time.sleep(0.3)

        choice = input("무장 하나를 선택하시오 : ")
        if choice != '':
            choice = int(choice)
        else:
            continue
            
        if (my_gold < recruit_fee):
            print("소지한 금이 부족합니다.")
            continue
        
        if (choice >=1 and choice <= len(general_list)):
            my_choice.append(general_list[choice-1])
            my_gold = my_gold - recruit_fee

            print()
            print(general_list[choice-1][0], "를 선택하였습니다.")
            print("소지금은 현재 ", my_gold, "입니다")

            print("등용한 무장은 현재 ", len(my_choice), "입니다")
            for i in my_choice:
                print(i[0])
            
        else:
            print("무장을 선택하지 않았습니다.")

    elif (select == '3'):  # 장수 해임
        for i in range(len(my_choice)):
            print(i+1, my_choice[i])

        choice = int(input("해임 할 무장 하나를 선택하시오 : "))

        if (choice >=1 and choice <= len(general_list)):
            del my_choice[choice-1]
        else:
            print("무장을 선택하지 않았습니다.")
            
    elif (select == '4'): # 현재 상태
        for i in my_choice:
            print(i)

        print("소지금 : ", my_gold)
        print("HP : ", my_hp)

    elif (select == '5'):

        if len(my_choice) == 0:
            print("등용한 장수가 없어 전쟁은 불가합니다.")
            continue
        
        my_total = 0
        enemy_total = 0
        
        for i in range(len(my_choice)):
            print(i + 1, my_choice[i])
            my_total = my_total + int(my_choice[i][1]) * 1.2 + int(my_choice[i][2]) *1.5 + int(my_choice[i][3])
            time.sleep(0.3)
            
        print("총 합 : ", round(my_total, 1))
        print("소지금 : ", my_gold)
        print("HP : ", my_hp)
        time.sleep(0.3)
        
        input("엔터키를 눌러 주세요...")
        print()
        print("적군 출현....")
        enemy = []
        enemy_num = random.randint(len(my_choice), int(len(my_choice) * 2) )
        
        for i in range(enemy_num):
            random_num = random.randint(1, 676)
            enemy.append(all_info[random_num])
            print(all_info[random_num])
            enemy_total = enemy_total + int(enemy[i][1]) * 1.2 + int(enemy[i][2]) * 1.5 + int(enemy[i][3])
            time.sleep(0.3)
            
        print("총 합 : ", round(enemy_total, 1))

        diff = abs(my_total - enemy_total)
        
        if (my_total > enemy_total):
            get_gold = 0
            
            if (diff >= 300):
                get_gold = random.randint(int(diff * 10), int(diff * 50))
                print("대승!!!!  -> 획득금 : ", get_gold)
                my_hp = my_hp + 30
                
            else:
                get_gold = random.randint(int(diff * 10), int(diff * 20))
                print("승리! -> 획득금 : ", get_gold)
                my_hp = my_hp + 10
                
            my_gold = my_gold + get_gold
                
        elif (my_total < enemy_total):
            if (diff >= 300):
                print("대패!!!!")
                killed = random.randint(0, len(my_choice)-1)
                print(my_choice[killed], "전사하였습니다.")
                del my_choice[killed]

                my_hp = my_hp - 30
                
            else:
                my_hp = my_hp - 10
                print("패배!")
        else:
            print("무승부!!")

        if (my_hp > 100):
            my_hp = 100
        elif (my_hp < 0):
            print("더이상 진행 불가...!!")
            break
        
    elif (select == '6'):
        break
    
    else :
        print("잘못된 입력입니다.")

    print()
    
read_file.close()
