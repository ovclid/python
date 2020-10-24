def show_usage():
    print(
    '''
    1단계 - 과목별 점수를 입력받습니다.
    2단계 - 입력한 점수의 평균값을 구합니다.
    3단계 - 점수의 등급을 매깁니다.
    ''')


def get_score():
    scoreList = []
    
    subjectNum = int(input("과목수를 입력하세요 : "))

    for i in range(subjectNum):
        score = int(input(f"{i+1}번째 과목 점수를 입력하세요 : "))
        scoreList.append(score)

    print("과목별 점수 : ", scoreList)

    print("\n")

    return scoreList


def calculate_mean(scoreList):
    subjectSum = 0
    for i in range(len(scoreList)):
        subjectSum = subjectSum + scoreList[i]
        subjectAve = subjectSum/len(scoreList)

    return subjectAve
    
def print_grade(subjectAve):
    if subjectAve >= 90:
        print("평균 : A")

    elif 80 <= subjectAve and subjectAve <= 89:
        print("B")

    elif 70 <= subjectAve and subjectAve <= 89:
        print("C")

    else:
        print("D")

    

show_usage()
scoreList = get_score()
mean = calculate_mean(scoreList)
print_grade(mean)




