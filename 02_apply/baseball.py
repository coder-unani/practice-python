# import random


# def generate_random_numbers(number_count, number_start, number_end):
#     numbers = []
#     while len(numbers) < number_count:
#         new_number = random.randint(number_start, number_end)
#         if new_number not in numbers:
#             numbers.append(new_number)
    
#     return numbers

# def count_matching_numbers(my_numbers, winning_numbers):
#     counts = [0, 0, 0]
#     for i in range(len(my_numbers)):
#         if  my_numbers[i] == winning_numbers[i]:
#             counts[0] += 1
#         elif my_numbers[i] in winning_numbers:
#             counts[1] += 1
#         else:
#             counts[2] += 1
    
#     return counts

# def record_my_numbers(number_count, number_start, number_end):
#     my_numbers = []
#     while len(my_numbers) < NUMBER_COUNT:
#         new_number = int(input(f"{len(my_numbers) + 1}번째 숫자를 입력하세요:"))
#         if new_number < NUMBER_START or new_number > NUMBER_END:
#             print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
#         elif new_number in my_numbers:
#             print("중복되는 숫자입니다. 다시 입력하세요.")
#         else:
#             my_numbers.append(new_number)
    
#     return my_numbers

# NUMBER_COUNT = 3
# NUMBER_START = 1
# NUMBER_END = 9

# winning_numbers = generate_random_numbers(NUMBER_COUNT, NUMBER_START, NUMBER_END)
# my_numbers = record_my_numbers(NUMBER_COUNT, NUMBER_START, NUMBER_END)


# print(my_numbers)


from random import randint


def generate_numbers():
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    numbers = []

    # 여기에 코드를 작성하세요
    while len(numbers) < 3:
        new_number = randint(1, 9)
        if new_number not in numbers:
            numbers.append(new_number)
    
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    # 여기에 코드를 작성하세요
    while len(new_guess) < 3:
        new_number = int(input(f"{len(new_guess) + 1}번째 숫자를 입력하세요:"))
        if new_number < 1 or new_number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_number)
    
    return new_guess


def get_score(guesses, solution):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    strike_count = 0
    ball_count = 0

    # 여기에 코드를 작성하세요
    for i in range(len(guesses)):
        if  guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1
    
    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 여기에 코드를 작성하세요
winning_numbers = generate_numbers()
strike_count = 0
ball_count = 0
while strike_count < 3:
    my_numbers = take_guess()
    strike_count, ball_count = get_score(my_numbers, winning_numbers)
    print(f"{strike_count}S {ball_count}B")
    tries += 1
    
print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))