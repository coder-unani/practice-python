############################################################
'''
numbers라는 리스트가 주어졌습니다.
for문과 range 함수를 사용하여, numbers의 인덱스와 원소를 출력해 보세요.

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
'''
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
for i in range(len(numbers)):
    print(i, numbers[i])

############################################################
'''
"2의 n제곱"을 출력하는 프로그램을 만들려고 합니다.
코드를 실행하면 아래와 같이 2^0 = 1부터 2^10 = 1024까지 출력되어야 합니다.
'''
for i in range(11):
    print(f"2^{i} = {2 ** i}")

############################################################
'''
구구단 프로그램을 while문이 아닌 for문을 사용해서 만들어 보세요.
'''
for i in range(1, 9+1):
    for j in range(1, 9+1):
        print(f"{i} * {j} = {i * j}")

############################################################
'''
'피타고라스 정리'라고 들어 보셨나요? 직각삼각형에서, 빗변의 제곱이 두 직각변의 제곱의 합과 같다는 정리입니다.
거기서 나온 '피타고라스 삼조'라는 개념이 있는데요. 피타고라스 삼조란, 

피타고라스 정리
a^2 + b^2 = c^2

를 만족하는 세 자연수 쌍 (a,b,c) 입니다.
예를 들어, 
3^2 + 4^2 = 5^2 이기 때문에 (3,4,5) 는 피타고라스 삼조입니다.
a < b < c 라고 가정할 때, a + b + c = 400 을 만족하는 피타고라스 삼조(a,b,c)는 단 하나인데요. 
이 경우, a * b * c 는 얼마인가요?
'''
for a in range(1, 400):
    for b in range(1, 400):
        c = 400 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)

############################################################
'''
리스트 내 요소들의 순서를 거꾸로 뒤집으려고 합니다.
예를 들면 다음과 같습니다.

[1, 4, 7]이 있으면 1과 7의 위치를 바꾸어서 [7, 4, 1]로 만듭니다.
[1, 4, 7, 11]이 있으면 1과 11의 위치를 바꾸고, 4와 7의 위치를 바꾸어서 [11, 7, 4, 1]로 만듭니다.

아래와 같이 numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 보세요!

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 여기에 코드를 작성하세요

print("뒤집어진 리스트: {}".format(numbers))
'''
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("뒤집어진 리스트: " + str(numbers))