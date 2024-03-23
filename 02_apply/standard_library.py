import math # 수학 관련된 모든걸 모아놓은 라이브러리
import random # 랜덤한 값을 만들어 내고 싶을 때 사용하는 라이브러리
import os # 운영체제를 조작하기 위한 라이브러리
import datetime # 날짜와 시간을 다루기 위한 라이브러리


print(math.log10(100))
print(math.cos(0))
print(math.pi)

print(random.random())
print(random.randint(1, 10)) # 1~10 사이의 랜덤한 정수를 출력
print(random.uniform(0, 1)) # 0~1 사이의 랜덤한 소수를 출력

print(os.getlogin())
print(os.getcwd())

pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))

today = datetime.datetime.now() # 현재 시간을 출력
print(today)
print(type(today))

# 두 날짜의 차이를 구할 수 있다.
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))

# 날짜와 시간을 더하거나 빼는 것도 가능하다.
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta)

# 날짜와 시간을 출력하는 방법
today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

# 포맷을 지정해서 출력하는 방법
today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))

'''
포맷 코드	설명	예시
%a	요일 (짧은 버전)	Mon
%A	요일 (풀 버전)	Monday
%w	요일 (숫자 버전, 0~6, 0이 일요일)	5
%d	일 (01~31)	23
%b	월 (짧은 버전)	Nov
%B	월 (풀 버전)	November
%m	월 (숫자 버전, 01~12)	10
%y	연도 (짧은 버전)	16
%Y	연도 (풀 버전)	2016
%H	시간 (00~23)	14
%I	시간 (00~12)	10
%p	AM/PM	AM
%M	분 (00~59)	34
%S	초 (00~59)	12
%f	마이크로초 (000000~999999)	413215
%Z	표준시간대	PST
%j	1년 중 며칠째인지 (001~366)	162
%U	1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	35
%W	1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35
'''