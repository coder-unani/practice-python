############################################################
'''
어떤 수가 짝수인지 홀수인지 판단하는 is_evenly_divisible() 함수를 작성하세요. 이 함수는 number(숫자)를 파라미터로 받습니다. 짝수인 경우, 즉 number가 2로 나누어떨어질 경우에는 True를 리턴합니다. 홀수인 경우, 즉 number가 2로 나누어떨어지지 않을 경우에는 False를 리턴합니다.
함수 안에는 print() 함수가 아닌, return문을 사용해야 합니다. 참고로 불린 개념을 잘 사용하면, 함수를 단 한 줄로 작성할 수 있습니다.
'''
def is_evenly_divisible(number):
    return number % 2 == 0

# 테스트 코드
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))

############################################################
'''
거스름돈을 계산하는 코드를 작성하려고 합니다. 예를 들어 33,000원짜리 물건을 사기 위해 100,000원을 냈다면 67,000원을 거슬러줘야 합니다.
각 지폐가 충분히 있다면 일반적으로 다음과 같이 거슬러 줍니다.

50,000원 지폐: 1장
10,000원 지폐: 1장
5,000원 지폐: 1장
1,000원 지폐: 2장
그 과정을 살펴보면 아래와 같습니다.

먼저 50,000원권 1장을 거슬러주면 67,000 - 50,000 = 17,000원이 남습니다.
남은 17,000원에 한해 10,000원권 1장을 거슬러주면 17,000 - 10,000 = 7,000원이 남습니다.
남은 7,000원에 한해 5,000원권 1장을 거슬러주면 2,000원이 남습니다.
남은 2,000원에 한해 1,000원권 2장을 거슬러주면 거스름돈을 다 돌려주게 됩니다.
이와 같은 방식으로 특정 가격의 물건을 사고, 금액을 지불했을 때 '가장 적은 수'의 지폐를 거슬러 주는 calculate_change() 함수를 작성하려고 합니다. 이 함수는 지불한 금액을 나타내는 payment와 물건의 가격을 나타내는 cost를 파라미터로 받습니다. 코드잇 실행기의 caculate_change() 함수를 완성해 주세요.
'''
def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000  # 50,000원 지폐
    ten_count = (change % 50000) // 10000  # 10,000원 지폐
    five_count = (change % 10000) // 5000  # 5,000원 지폐
    one_count = (change % 5000) // 1000  # 1,000원 지폐

    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))

# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)