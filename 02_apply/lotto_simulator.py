import random

RANDOM_INT_START = 1
RANDOM_INT_END = 45

def generate_numbers(grnerate_count):
    result = []
    for i in range(grnerate_count):
        result.append(random.randint(RANDOM_INT_START, RANDOM_INT_END))
    
    return result

def draw_winning_numbers():
    # 여기에 코드를 작성하세요
    winning_numbers = generate_numbers(6)
    winning_numbers.sort()
    winning_numbers.append(generate_numbers(1)[0])
    
    return winning_numbers

# 테스트 코드
# print(draw_winning_numbers())


def count_matching_numbers(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    matched_numbers = []
    for i in range(len(numbers)):
        if numbers[i] in winning_numbers:
            matched_numbers.append(numbers[i])
            
    return len(matched_numbers)


# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))

#################################################
'''
main.py 파일의 check() 함수를 작성하세요. 참고로 당첨 액수는 아래 규칙에 따라 결정됩니다.
내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치: 10억 원
내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치: 5천만 원
내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치: 100만 원
내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치: 5만 원
내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치: 5천 원
check() 함수는 참가자의 당첨 금액을 리턴합니다. 
파라미터로 참가자가 뽑은 번호가 담긴 리스트 numbers와 주최측에서 뽑은 번호가 담긴 리스트 winning_numbers를 받는데요. 
numbers는 당연히 번호 6개를 담고 있고, winning_numbers는 보너스 번호까지 해서 7개를 담고 있겠죠?
'''
def count_matching_numbers(numbers, winning_numbers):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    matched_numbers = []
    for i in range(len(numbers)):
        if numbers[i] in winning_numbers:
            matched_numbers.append(numbers[i])
            
    return len(matched_numbers)

def check(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    bonus_number = [winning_numbers[-1]]
    winning_numbers = winning_numbers[:-1]
    winning_count = count_matching_numbers(numbers, winning_numbers)
    bonus_count = count_matching_numbers(numbers, bonus_number)
    
    winning_money = 0
    if (winning_count == 6):
        winning_money = 1000000000
    elif (winning_count == 5 and bonus_count == 1):
        winning_money = 50000000
    elif (winning_count == 5):
        winning_money = 1000000
    elif (winning_count == 4):
        winning_money = 50000
    elif (winning_count == 3):
        winning_money = 5000
    else:
        winning_money = 0
    
    return winning_money


# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))