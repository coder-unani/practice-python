import random
# name = input("이름을 입력하세요: ")
# print(name)

# input으로 입력받은 값은 문자열로 저장된다.
# x = input("숫자를 입력하세요: ")
# print(int(x) + 5)

############################################################
'''
프로그램을 실행하면 기회가 *번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:가 출력됩니다. 총 네 번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회가 줄어듭니다.
정답을 맞히면 축하합니다. *번 만에 숫자를 맞히셨습니다.가 출력되고 프로그램은 종료됩니다.
사용자가 입력한 수가 정답보다 작은 경우 Up이 출력되고, 입력한 수가 정답보다 큰 경우 Down이 출력됩니다.
정답이 틀렸으면 1번부터 다시 진행합니다. 만약 네 번의 기회를 모두 사용했는데도 답을 맞히지 못했으면, 아쉽습니다. 정답은 *입니다.가 출력되고 프로그램은 종료됩니다.
'''
MAX_CHALLENGES = 4
HIGH_NUMBER = 20
LOW_NUMBER = 1
CHOICE_NUMBER = random.randint(LOW_NUMBER, HIGH_NUMBER)

my_number = 0
my_challenges = 0
while my_number != CHOICE_NUMBER:
    my_number = int(input(f"기회가 {MAX_CHALLENGES - my_challenges}번 남았습니다. {LOW_NUMBER}-{HIGH_NUMBER} 사이의 숫자를 맞혀 보세요: "))
    if my_number > 0:
        my_challenges += 1

    if my_number > HIGH_NUMBER or my_number < LOW_NUMBER:
        print(f"{LOW_NUMBER}~{HIGH_NUMBER} 사이의 숫자를 입력하세요.")
        continue
    
    print(f"입력한 숫자는 {my_number}입니다. / 정답은 {CHOICE_NUMBER}입니다.")

    if my_challenges < MAX_CHALLENGES:
        if my_number == CHOICE_NUMBER:
            print(f"축하합니다. {my_challenges}번만에 숫자를 맞히셨습니다.")
            break
        elif my_number < CHOICE_NUMBER:
            print("Up")
        else:
            print("Dwon")
    else:
        print(f"아쉽습니다. 정답은 {CHOICE_NUMBER}였습니다.")
        break
        
# or 
import random

# 상수 정의
ANSWER = random.randint(1, 20)
NUM_TRIES = 4

# 변수 정의
guess = -1
tries = 0

while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(NUM_TRIES - tries)))
    tries += 1    
    
    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")

if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))
