# list
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

# indexing
print(numbers[3])
print(numbers[-1])
print(numbers[-2])

# list slicing
print(numbers[0:3])
print(numbers[2:3])
print(numbers[2:])
print(numbers[:3])

# append & del & insert
numbers[0] = 7
print(numbers)

numbers = []
numbers.append(5)
numbers.append(8)
print(str(len(numbers)))

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
del numbers[3]
print(numbers)

numbers.insert(4, 37)
print(numbers)

# sort & sorted
numbers = [19, 13, 2, 5, 3, 11, 7, 17]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # [2, 3, 5, 7, 11, 13, 17, 19]

reverse_sorted_numbers = sorted(numbers, reverse=True)
print(reverse_sorted_numbers) # [19, 17, 13, 11, 7, 5, 3, 2]

print(numbers.sort()) # None
print(numbers) # [2, 3, 5, 7, 11, 13, 17, 19]
numbers.sort(reverse=True)
print(numbers) # [19, 17, 13, 11, 7, 5, 3, 2]
numbers.reverse();
print(numbers);

# value check or value find indexing
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)

members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))

# remove
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)

############################################################
'''
화씨 온도(°F)를 섭씨 온도(°C)로 바꾸어주는 프로그램을 만들려고 합니다.

섭씨와 화씨의 관계식은 다음과 같습니다:
°C = (°F - 32) * 5 / 9

화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius를 써 보세요. 이 함수는 파라미터로 화씨 온도 fahrenheit를 받고, 변환된 섭씨 온도를 리턴합니다.

실습 결과

화씨 온도 리스트: [40, 15, 32, 64, -4, 11]
섭씨 온도 리스트: [4.4, -9.4, 0.0, 17.8, -20.0, -11.7]
'''

# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드
i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1

print("섭씨 온도 리스트: {}".format(temperature_list))

############################################################
'''
제가 구매하고 싶은 물건들의 가격을 리스트에 정리해 놨습니다.


prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
가격의 단위는 모두 원화(￦)인데요. 이 물건들의 가격을 미국 달러($)로 하면 얼마일지, 그리고 일본 엔화(￥)로 하면 얼마일지 확인해 보려고 합니다.
참고로 환율은 1달러에 1,000원, 그리고 1,000엔에 8달러라고 가정합니다.
'''
# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    # 여기에 코드를 작성하세요
    return krw / 1000

# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    # 여기에 코드를 작성하세요
    return usd / 8 * 1000


# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 
# prices를 원화(￦)에서 달러($)로 변환하기
# 여기에 코드를 작성하세요
i = 0;
while i < len(prices):
    prices[i] = krw_to_usd(prices[i])
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))


# prices를 달러($)에서 엔화(￥)으로 변환하기
# 여기에 코드를 작성하세요
i = 0
while i < len(prices):
    prices[i] = usd_to_jpy(prices[i])
    i += 1
# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))  # 섭씨 온도 출력

############################################################

# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
# 코드를 입력하세요
print(numbers)

# numbers에서 홀수 제거
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i += 1
# 코드를 입력하세요
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
# 코드를 입력하세요
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
# 코드를 입력하세요
print(numbers)

