import mymodule_pd as mm

url = "https://raw.githubusercontent.com/ovclid/python/master/all.txt"
all_info = mm.read_data(url)

my_choice = []


while True:
    print("---------------------------------------------------------------------")
    select = input("명령을 선택하시오(1.검색, 2.등용, 3.해임, 4.정보, 5.전쟁, 6. 종료) : ")

    if (select == '1'):     # 장수 검색
        mm.search_generals(all_info)
        
    elif (select == '2'):   # 장수 등용
        my_choice = mm.recruit_generals(all_info, my_choice)
        
    elif (select == '3'):   # 장수 해임
        mm.dismiss_generals(my_choice)
            
    elif (select == '4'):   # 현재 상태
        mm.show_info(all_info, my_choice)
            
    elif (select == '5'):   # 전쟁
        pass
    
    elif (select == '6'):  # 종료
        break
    
    else :
        print("잘못된 입력입니다.")

