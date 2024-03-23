# file_read.py 파일이 있는 디렉토리에서 실행하여야 한다.
# 다른 경로에서 실행하면 파일을 찾을 수 없다는 에러가 발생한다.
with open("data/chicken.txt", "r") as file:
    for line in file:
        # strip() 함수는 문자열의 앞뒤 공백을 제거한다.
        print(line.strip())

#split() 함수는 문자열을 특정 문자로 나누어 리스트로 만들어 준다.
my_split = "1. 2. 3. 4. 5. 6"
print(my_split.split(". "))

print("1 2 \n\n 3      4  5 \n 6".split())

with open("data/new_file.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("안녕하세요. 파이썬!\n")

with open("data/new_file.txt", "a") as file:
    file.write("Append a new line!\n")

############################################################
'''
밑에 나와 있는 chicken.txt 파일을 보세요. 
제가 운영하는 치킨집 '코딩에빠진닭(이하 코빠닭)'의 12월 매출이 정리되어 있습니다.
1일: 453400
2일: 388600
3일: 485300
4일: 477900
5일: 432100
6일: 665300
7일: 592500
8일: 465200
9일: 413200
10일: 523000
11일: 488600
12일: 431500
13일: 682300
14일: 633700
15일: 482300
16일: 391400
17일: 512500
18일: 488900
19일: 434500
20일: 645200
21일: 599200
22일: 472400
23일: 469100
24일: 381400
25일: 425800
26일: 512900
27일: 723000
28일: 613600
29일: 416700
30일: 385600
31일: 472300
:의 왼쪽에는 해당 월의 며칠인지, 그리고 오른쪽에는 그 날의 매출이 적혀 있습니다. 
data 폴더의 chicken.txt 파일을 읽어 들이고, strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 출력하세요. 
평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다. 
참고로 현재 제공된 파일에는 31일이 있지만, 어떤 달은 31일이 아닐 수도 있습니다. 
이 점을 고려해서 확장성 있는 코드를 작성해 주시길 바랍니다.
'''
total = []
with open("data/chicken.txt") as file:
    for line in file:
        split = line.split("일: ")
        total.append(int(split[1]))

total_sum = sum(total) / len(total)
print (total_sum)

############################################################
'''
영어 강사 Coy는 학생들의 단어 암기를 위해 단어장 프로그램을 만들려고 합니다. 
이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고, 
vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리하는데요. 
사용자가 새로운 단어와 뜻을 입력할 때마다 vocabulary.txt에 작성되는 것입니다. 
사용자는 반복적으로 단어와 뜻을 입력하는데, 단어나 뜻으로 q를 입력하는 순간 프로그램은 즉시 종료됩니다. 
사용자가 q를 입력하고 나면 파일은 더 이상 바뀌지 않아야 합니다.
'''
EXIT_STRING = "q"

with open("data/vocabulary.txt", "a") as file:
    is_exit = False
    word_en = ""
    word_ko = ""
    while not is_exit:
        word_en = input("영어 단어를 입력하세요: ")
        if word_en == EXIT_STRING:
            is_exit = True
            break;
        word_ko = input("한국어 뜻을 입력하세요: ")
        if word_ko == EXIT_STRING:
            is_exit = True
            break;
        
        if not is_exit:
            file.write(f"{word_en}: {word_ko}\n")

############################################################
'''
앞선 실습에서 vocabulary.txt라는 파일을 만들었죠? 이 파일에는 우리가 암기하고 싶은 단어들이 정리되어 있는데요. 
이번에는 이 파일의 단어들을 가지고 학생들에게 문제를 내는 프로그램을 만들려고 합니다.
프로그램은 터미널에 한국어 뜻을 알려 줄 것이고, 사용자는 그에 맞는 영어 단어를 입력해야 합니다. 
사용자가 입력한 영어 단어가 정답이면 맞았습니다!라고 출력하고, 틀리면 아쉽습니다. 
정답은 OOO입니다.가 출력되어야 합니다.
문제를 내는 순서는 vocabulary.txt에 정리된 순서입니다.
'''
with open("data/vocabulary.txt", "r") as file:
    for line in file:
        list = line.split(": ")
        word_en = list[0].strip()
        word_ko = list[1].strip()
        answer = input(f"{word_en} :").strip()
        if answer == word_ko:
            print("정답입니다.")
        else:
            print(f"아쉽습니다. 정답은 {word_ko}입니다.")