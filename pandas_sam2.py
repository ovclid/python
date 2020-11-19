import pandas as pd 
import random
import time

url = "https://raw.githubusercontent.com/ovclid/python/master/data.txt"
df = pd.read_table(url)

df["총계"] = df["통솔"] + df["무력"] + df["지력"]
df['나라'] = df.apply(lambda x : random.choice(["위", "촉", "오"]), axis = 1)

nation_dic = {1 : "위", 2:"촉", 3:"오"}
nation = nation_dic[int(input("나라를 선택하시오(1. 위, 2. 촉, 3. 오) : "))]

##my_choice_df = pd.DataFrame(None, columns = df.columns)
my_choice_df = df.head(0).copy()
#my_choice_df.drop(my_choice_df.index, inplace=True)

while True:
    print("---------------------------------------------------------------------")
    select = input("명령 선택(1.검색, 2.등용, 3.해임, 4.정보, 5.전쟁, 6. 종료) : ")

    if (select == '1'):     # 장수 검색
        search_select = input("검색 방법 선택(1. 이름, 2. 번호, 3. 능력, 4. 나라) : ")
    
        if (search_select == '1'):   # 장수 검색 - 이름으로 검색
            name = input("무장의 이름을 입력하시오 : ")
            print(df[df.이름 == name])

        elif (search_select == '2'):  # 장수 검색 - 번호로 검색
            start = int(input("시작(0~" + str(len(df)-1) + "):"))
            end = int(input("마지막(" + str(start+1) + "~" + str(len(df)-1) + "):"))
            print(df.loc[start-1:end])

        elif (search_select == '3'): # 장수 검색 - 무력으로 검색
            ability_select = int(input("능력 선택(1. 통솔, 2. 무력, 3. 지력) : "))
            start = int(input("시작 능력(1~100) : "))
            end = int(input("마지막 능력(" + str(start + 1) + "~100) : "))

            dic = {1 : "통솔", 2 : "무력", 3 : "지력"}
            category = dic[ability_select]
            print( df[(df[category] >= start) | (df[category] >= end)])
        
        elif (search_select == '4'): # 장수 검색 - 나라로 검색
            name = nation_dic[int(input("나라 선택(1. 위, 2. 촉, 3. 오) : "))]
            print(df[df["나라"]==name].sort_values("총계", ascending=False))

        else :
            continue

    elif (select == '2'):   # 장수 등용
        sample_df = df[df["나라"] == nation].sample(5)
        print(sample_df)

        choice = input("등용할 무장 하나를 선택하시오 : ")
        if (choice != ''):
            if (int(choice) in sample_df.index) :
                my_choice_df = my_choice_df.append(df.loc[int(choice)])
                print(my_choice_df)
            else:
                print("잘못된 선택입니다.")

    elif (select == '3'):   # 장수 해임
        print(my_choice_df)
        choice = input("해임할 무장 하나를 선택하시오 : ")

        if (choice != ''):
            if (int(choice) in my_choice_df.index):
                my_choice_df.drop(int(choice), inplace=True)
                print(my_choice_df)
            else:
                print("잘못된 선택입니다.")

    elif (select == '4'):   # 현재 상태
        print("-------등용 무장 -------")
        print(my_choice_df.describe())
        print(my_choice_df)

    elif (select == '5'):   # 전쟁
        enemy_sample_df = df[df["나라"] != nation].sample(len(my_choice_df))

        print("-----아군------")
        print(my_choice_df)

        time.sleep(1)
        print("-----적군------")
        print(enemy_sample_df)
        print()

        select_generals = []
        for i in range(len(my_choice_df)):
            select = int(input(f"{i+1} 번째 장수를 선택하시오 : "))
            if(select in my_choice_df.index):
                select_generals.append(select)
            else:
                print("잘못 입력하였음")
                continue

        win = 0
        lost = 0
        draw = 0

        for i in range(len(select_generals)):
            en_sum = enemy_sample_df.iloc[i]["무력"]
            my_sum = my_choice_df.loc[select_generals[i], "무력"]

            print(f"{my_choice_df.loc[select_generals[i], '이름']} {my_sum} VS. {enemy_sample_df.iloc[i]['이름']} {en_sum}")
            time.sleep(1)

            while(en_sum > 0 and my_sum > 0) :
                en_sum = en_sum - random.randint(1, 10)
                my_sum = my_sum - random.randint(1, 10)
                time.sleep(0.5)
                print(f"{my_choice_df.loc[select_generals[i], '이름']} {my_sum} VS. {enemy_sample_df.iloc[i]['이름']} {en_sum}")

            if (my_sum > en_sum):
                print("승리!!!!")
                win += 1
            elif (my_sum < en_sum):
                print("패배!!!!")
                lost += 1
            else:
                print("무승부")
                draw += 1
            
        print(f"\n 승리{win}, 패배{lost}, 무승부{draw}")
    
    elif (select == '6'):  # 종료
        break
    
    else :
        print("잘못된 입력입니다.")
