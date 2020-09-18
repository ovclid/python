from mymodule import *

all_info = read_data("전체무장.txt")
my_choice = []

while True:
    print("---------------------------------------------------------------------")
    select = input("명령을 선택하시오(1.검색, 2.등용, 3.해임, 4.정보, 5.전쟁, 6. 종료) : ")

    if (select == '1'):     # 장수 검색
        search_generals(all_info)
        
    elif (select == '2'):   # 장수 등용
        my_choice = recruit_generals(all_info, my_choice)
        
    elif (select == '3'):   # 장수 해임
        dismiss_generals(my_choice)
            
    elif (select == '4'):   # 현재 상태
        show_info(all_info, my_choice)
            
    elif (select == '5'):   # 전쟁
        pass
    
    elif (select == '6'):  # 종료
        break
    
    else :
        print("잘못된 입력입니다.")
