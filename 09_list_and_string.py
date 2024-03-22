
alphabet_string = "ABCDEFGHIJ"
print(alphabet_string[0]) # A
print(alphabet_string[1]) # B
print(alphabet_string[4]) # E
print(alphabet_string[-1]) # J

alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

print(alphabet_list[0]) # A
print(alphabet_list[1]) # B
print(alphabet_list[4]) # E
print(alphabet_list[-1]) # J
print(alphabet_list[0:5]) # ['A', 'B', 'C', 'D', 'E']
print(alphabet_list[4:]) # ['E', 'F', 'G', 'H', 'I', 'J']
print(alphabet_list[:4]) # ['A', 'B', 'C', 'D']

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3) # [1, 2, 3, 4, 5, 6, 7, 8]

my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # 5

my_string = "Hello World!"
print(len(my_string)) # 12

my_list = [1, 2, 3, 4, 5]
my_list[0] = 6
print(my_list) # [6, 2, 3, 4, 5]

my_string = "Hello World!"
my_string[0] = "h" # TypeError: 'str' object does not support item assignment

############################################################
'''
함수 sum_digit은 파라미터로 정수형 num을 받고, num의 각 자릿수를 더한 값을 리턴합니다.
예를 들어서 12의 각 자릿수는 1, 2이니까 sum_digit(12)는 3, 즉 1 + 2의 결괏값을 리턴합니다.
마찬가지로 486의 각 자릿수는 4, 8, 6이니까 sum_digit(486)은 18(4 + 8 + 6)을 리턴하는 거죠.
여러분이 해야 할 일은 두 가지입니다.

1. sum_digit 함수를 작성한다.
2. sum_digit(1)부터 sum_digit(1000)까지의 합을 구해서 출력한다.
'''
# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)
    
    for digit in str_num:
        total += int(digit)

    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
digit_total = 0
for i in range(1, 1001):
    digit_total += sum_digit(i)

############################################################
'''
주민등록번호 YYMMDD-abcdefg는 총 열세 자리인데요.

앞의 여섯 자리 YYMMDD는 생년월일을 의미합니다.

YY → 연
MM → 월
DD → 일
뒤의 일곱 자리 abcdefg는 살짝 복잡합니다.

a → 성별
bc → 출생등록지에 해당하는 지방자치단체의 고유번호
defg → 임의의 번호
보시다시피 많은 부분은 특정 규칙대로 정해져 있는데요. 
여러분에 대한 몇 가지 정보만 알면, 마지막 네 개 숫자 defg를 제외한 앞의 아홉 자리는 쉽게 알 수 있다는 거죠.
그래서 저희는 주민등록번호의 마지막 네 자리 defg만 가려 주는 보안 프로그램을 만들려고 합니다.

mask_security_number라는 함수를 정의하려고 하는데요. 
이 함수는 파라미터로 문자열 security_number를 받고, security_number의 마지막 네 글자를 '*'로 대체한 새 문자열을 리턴합니다.
참고로 파라미터 security_number에는 작대기 기호(-)가 포함될 수도 있고, 포함되지 않을 수도 있는데요.  
작대기 포함 여부와 상관 없이, 마지막 네 글자가 '*'로 대체되어야 합니다!
'''
def mask_security_number(security_number):
    return security_number[:-4] + '****'


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

############################################################
'''
"토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 '팰린드롬(palindrome)'이라고 부릅니다.
팰린드롬 여부를 확인하는 함수 is_palindrome을 작성하려고 하는데요. 
is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴하고 팰린드롬이 아니면 False를 리턴합니다.
예를 들어서 "racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 합니다. 
그리고 "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야 하는 거죠.

'''
def is_palindrome(word):
    # 여기에 코드를 작성하세요
    forward = list(word)
    backward = list(reversed(forward))
    
    return forward == backward

# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

############################################################
'''
리스트와 문자열은 굉장히 비슷합니다. 리스트가 어떤 자료형들의 나열이라면, 문자열은 문자들의 나열이라고 할 수 있겠죠. 지금부터 파이썬에서 리스트와 문자열이 어떻게 같고 어떻게 다른지 알아봅시다.

인덱싱 (Indexing)
두 자료형은 공통적으로 인덱싱이 가능합니다.


# 알파벳 리스트의 인덱싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0])
print(alphabets_list[1])
print(alphabets_list[4])
print(alphabets_list[-1])

# 알파벳 문자열의 인덱싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0])
print(alphabets_string[1])
print(alphabets_string[4])
print(alphabets_string[-1])

A
B
E
J
A
B
E
J
for 반복문
두 자료형은 공통적으로 인덱싱이 가능합니다. 따라서 for 반복문에도 활용할 수 있습니다.


# 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:
    print(alphabet)

# 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:
    print(alphabet)

C
O
D
E
I
T

C
O
D
E
I
T
슬라이싱 (Slicing)
두 자료형은 공통적으로 슬라이싱이 가능합니다.


# 알파벳 리스트의 슬라이싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

# 알파벳 문자열의 슬라이싱
alphabets_string = 'ABCDEFGHIJ'
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])

['A', 'B', 'C', 'D', 'E']
['E', 'F', 'G', 'H', 'I', 'J']
['A', 'B', 'C', 'D']
ABCDE
EFGHIJ
ABCD
덧셈 연산
두 자료형에게 모두 덧셈은 "연결"하는 연산입니다.


# 리스트의 덧셈 연산
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# 문자열의 덧셈 연산
string1 = '1234'
string2 = '5678'
string3 = string1 + string2
print(string3)

[1, 2, 3, 4, 5, 6, 7, 8]
12345678
len 함수
두 자료형은 모두 길이를 재는 len 함수를 쓸 수 있습니다.


# 리스트의 길이 재기
print(len(['H', 'E', 'L', 'L', 'O']))

# 문자열의 길이 재기
print(len("Hello, world!"))

5
13
Mutable (수정 가능) vs. Immutable (수정 불가능)
하지만 차이점이 있습니다. 리스트는 데이터를 바꿀 수 있지만, 문자열은 데이터를 바꿀 수 없다는 것입니다. 리스트와 같이 수정 가능한 자료형을 'mutable'한 자료형이라고 부르고, 문자열과 같이 수정 불가능한 자료형을 'immutable'한 자료형이라고 부릅니다. 숫자, 불린, 문자열은 모두 immutable한 자료형입니다.


# 리스트 데이터 바꾸기
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

[5, 2, 3, 4]
리스트 numbers의 인덱스 0에 5를 새롭게 지정해주었습니다. [5, 2, 3, 4]가 출력되었습니다. 이처럼 리스트는 데이터의 생성, 삭제, 수정이 가능합니다.


# 문자열 데이터 바꾸기
name = "codeit"
name[0] = "C"
print(name)

Traceback (most recent call last):
  File "untitled.py", line 3, in <module>
    name[0] = "C"
TypeError: 'str' object does not support item assignment
문자열 name의 인덱스 0 에 "C"를 새롭게 지정해주었더니 오류가 나왔습니다. TypeError: 'str' object does not support item assignment는 문자열은 변형이 불가능하다는 메시지입니다. 이처럼 문자열은 리스트와 달리 데이터의 생성, 삭제, 수정이 불가능합니다.
'''
