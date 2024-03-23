# 사전 (dictionary)
# key와 value의 쌍으로 이루어진 자료형
# key는 일반적으로 string 형태로 사용
# value는 모든 데이터 타입이 가능
# key와 value는 콜론(:)으로 구분하고, 각 쌍은 쉼표(,)로 구분
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(type(my_dictionary))
my_dictionary[9] = 81
print(my_dictionary)

my_family = {
    "엄마": "김자옥",
    "아빠": "이석진",
    "아들": "이태호",
    "딸": "이하린"
}

print(my_family.values())
print("이하린" in my_family.values())

for value in my_family.values():
    print(value)

for key in my_family.keys():
    print(key)

for key, value in my_family.items():
    print(key, value)

############################################################
'''
태호는 미국 다트머스 대학교 컴퓨터 과학과에 지원하려고 합니다. 
컴퓨터 과학 전공으로 미국 유학을 가고 싶기 때문에, 코딩 공부와 영어 공부를 모두 해야 하는 상황인데요. 
그 둘을 동시에 하기 위해서 파이썬으로 단어장 프로그램을 만들기로 합니다.

- 해야 할 일
단어장 만들기
새로운 단어들 추가

1. 단어장 만들기
잘 모르는 단어 네 개입니다.

sanitizer: 살균제
ambition: 야망
conscience: 양심
civilization: 문명

이 단어들을 저장하는 사전을 만들고, 만든 사전을 vocab라는 변수에 저장하세요. 
단어와 뜻이 key-value로 들어가야 합니다.

2. 새로운 단어들 추가
이미 만들어진 vocab 사전에 새로운 단어들을 추가하고 싶습니다. 아래 단어들을 추가해 주세요.

privilege: 특권
principle: 원칙
'''
# 1. 단어장 만들기
vocab = {
    # 여기에 코드를 작성하세요
    "sanitizer": "살균제",
    "ambition": "야망",
    "conscience": "양심",
    "civilization": "문명"
}
print(vocab)


# 2. 새로운 단어들 추가
vocab["privilege"] = "특권"
vocab["principle"] = "원칙"
# 여기에 코드를 작성하세요
print(vocab)

############################################################
'''
태호는 영어 단어 공부를 위해서 단어장 프로그램을 만들었습니다. 
하지만 이번에는 영-한으로 공부하는 것이 아니라, 한-영으로 공부를 해 보고 싶습니다.
사전의 key와 value를 뒤집어 주는 함수 reverse_dict를 작성해 주세요. 
reverse_dict는 파라미터로 사전 dict를 받고, key와 value가 뒤집힌 새로운 사전을 리턴합니다.
# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}
'''
# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    
    # dict의 key와 value를 뒤집어서 new_dict에 저장
    # 여기에 코드를 작성하세요
    for key, value in dict.items():
        new_dict[value] = key
    
    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

############################################################
'''
효신이는 매년 국회의원 선거 때마다, 성북구에서 집계 도우미 봉사를 하는데요. 
작년까지는 표를 손수 세다가, 올해부터는 IT 시대에 더 적합한 솔루션을 개발하려고 합니다.
파이썬 리스트 votes에는 성북구민들의 투표 결과가 저장되어 있습니다. 
리스트 votes의 정보를 토대로, 사전 vote_counter에 후보별 득표수를 정리하는 것이 목표입니다.
예를 들어서 votes가 ['허유나', '서혜선', '허유나']라고 가정하면, 
vote_counter는 {'허유나': 2, '서혜선': 1}이 되어야 하는 거죠.

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']
'''

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    # 여기에 코드를 작성하세요
    if name in vote_counter:
        vote_counter[name] += 1
    else:
        vote_counter[name] = 1

# 후보별 득표수 출력
print(vote_counter)
