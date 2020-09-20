import random
import time
import pandas as pd

def read_data(file_name):
    all_info = pd.read_table(file_name)

    print("전체 장수 : ", len(all_info))
    print(all_info.head(5))
    print(all_info.tail(5))
    #print(pd.concat([all_info.head(5), all_info.tail(5)]))

    return all_info


def search_generals(all_info):
    search_select = input("검색 방법을 선택하시오(1. 이름, 2. 번호, 3. 능력) : ")
    
    if (search_select == '1'):   # 장수 검색 - 이름으로 검색
        name = input("무장의 이름을 입력하시오 : ")

        #print(all_info[all_info.이름 == name].values.tolist()[0])
        
        print(all_info[all_info.이름 == name])
        
        '''
        for i in range(len(all_info)):
            if (all_info[i][0] == name):
                print(all_info[i])
        '''

    elif (search_select == '2'):  # 장수 검색 - 번호로 검색
        start = int(input("시작 번호(1~" + str(len(all_info)) + ") : "))
        end = int(input("마지막 번호(" + str(start + 1) + "~" + str(len(all_info)) + ") : "))

        print(all_info[start+1:end+1])
        
        '''
        for i in range(start-1, end):
            print(all_info[i])
        '''

    elif (search_select == '3'): # 장수 검색 - 무력으로 검색
        ability_select = int(input("능력을 선택하시오(1. 통솔, 2. 무력, 3. 지력) : "))
        start = int(input("시작 능력(1~100) : "))
        end = int(input("마지막 능력(" + str(start + 1) + "~100) : "))

        dic = {1 : "통솔", 2 : "무력", 3 : "지력"}

        category = dic[ability_select]

        print(all_info[ (all_info[category] >= start) & (all_info[category] <= end)])
        
        
        '''
        for i in range(len(all_info)):
            if (int(all_info[i][ability_select]) >= start and int(all_info[i][ability_select]) <= end):
                print(all_info[i])
        '''
        
    else:
        return

def recruit_generals(all_info, my_choice):    
    general_list = []
    for i in range(random.randint(1, 10)):
        random_num = random.randint(1, len(all_info))
        general_list.append(random_num)
        
        print(i+1, list(all_info.loc[random_num]))
        time.sleep(0.3)

    choice = input("무장 하나를 선택하시오 : ")

    if (choice >= '1' and choice <= str(len(general_list))):
        my_choice.append(general_list[int(choice)-1])
        print(all_info.loc[int(choice)-1, "이름"], "를 선택하였습니다.")
        print("등용한 무장은 현재 ", len(my_choice), "명 입니다.")
        
        for i in my_choice:
            print(list(all_info.loc[i]))
    
    return my_choice

def dismiss_generals(my_choice):
    for i in range(len(my_choice)):
        print(i+1, my_choice[i])

    choice = int(input("해임 할 무장 하나를 선택하시오 : "))

    if (choice >=1 and choice <= len(my_choice)):
        del my_choice[choice-1]
    else:
        print("무장을 선택하지 않았습니다.")

def show_info(all_info, my_choice):
    print("전체 장수 : ", len(all_info))
    print("등용 장수 : ", len(my_choice))
    
    for i in my_choice:
        print(i)
