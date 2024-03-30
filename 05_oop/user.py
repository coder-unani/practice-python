class User:

    count = 0 # 클래스 변수

    def __init__(self, name, email, password): # 생성자. __ 로 시작하는 메소드는 special method, 특수 메소드
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다.".format(self.name))
    
    def login(self, email, password):
        if (self.email == email and self.password == password):
            print("로그인 성공")
            self.say_hello()
        else:
            print("로그인 실패")
    
    def __str__(self):
        return "사용자: {}, 이메일: {}".format(self.name, self.email)
    
    @classmethod # 데코레이터로 클래스 메소드 지정
    def print_number_of_users(cls):
        print(f"총 유저 수는: {cls.count}입니다.")

    @staticmethod # 데코레이터로 정적 메소드 지정
    def valid_email(email):
        return '@' in email
    

user1 = User("이윤환", "coder.unani@gmail.com", "12345")
user1.say_hello() # say_hello(() 인스턴스를 호출하면 자동으로 첫번째 인자로 인스턴스가 전달된다.
user1.login("coder.unani@gmail.com", "12345")

user2 = User("이윤환2", "coder.unani2@gmail.com", "12345")

print(user1)
print(user2)

print(User.count)

user1.print_number_of_users()
User.print_number_of_users()

print(User.valid_email("coder.unani"))
print(User.valid_email("coder.unani@gmail.com"))

###########################################################################################################
'''
인스타그램에 취직한 Jane은 User 클래스에 "팔로우" 기능을 추가하라는 지시를 받았습니다.

팔로우 기능은 크게 2개의 동작을 해야 합니다.

"내가 팔로우하는 사람" 목록에 그 사람을 추가하는 동작
상대방의 "나를 팔로우하는 사람" 목록에 나를 추가하는 동작
팔로우 기능은 follow 메소드로 구현하려고 하는데요.    
팔로우 기능을 만드는 김에 아래 기능을 하는 메소드들도 추가해 봅시다.

유저가 팔로우하는 사람 수를 알려주는 num_following 메소드
유저를 팔로우하는 사람 수를 알려주는 num_followers 메소드
User 클래스에 이 메소드들을 모두 추가하고 나서 코드를 실행하면 아래와 같은 실행 결과가 나와야 합니다.
'''
# class User:

#     # 인스턴스 변수 설정
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#         self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
#         self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

#     # 팔로우
#     def follow(self, another_user):
#         # 여기에 코드를 작성하세요
#         self.following_list.append(another_user)
#         another_user.followers_list.append(self.name)

#     # 내가 몇 명을 팔로우하는지 리턴
#     def num_following(self):
#         # 여기에 코드를 작성하세요
#         return len(self.following_list)

#     # 나를 몇 명이 팔로우하는지 리턴
#     def num_followers(self):
#         # 여기에 코드를 작성하세요
#         return len(self.followers_list)
    
# # 유저들 생성
# user1 = User("Young", "young@codeit.kr", "123456")
# user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
# user3 = User("Taeho", "taeho@codeit.kr", "123abc")
# user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# # 유저마다 서로 관심 있는 유저를 팔로우
# user1.follow(user2)
# user1.follow(user3)
# user2.follow(user1)
# user2.follow(user3)
# user2.follow(user4)
# user4.follow(user1)

# # 유저 이름, 자신의 팔로워 수, 자신이 팔로우하는 사람 수를 출력합니다
# print(user1.name, user1.num_followers(), user1.num_following())
# print(user2.name, user2.num_followers(), user2.num_following())
# print(user3.name, user3.num_followers(), user3.num_following())
# print(user4.name, user4.num_followers(), user4.num_following())

###########################################################################################################
'''
인스턴스를 생성할 때 필요한 정보들이 항상 우리가 원하는 형태로 존재할까요? 
우리는 다양한 형태의 정보에서 필요한 부분을 뽑아내서 인스턴스를 생성할 수 있어야 합니다. 
예를 들어 유저 인스턴스 생성에 필요한 정보가 문자열일 수도 있고 리스트일 수도 있습니다. 
어떻게 각각의 형태에 대응할 수 있을까요? 아래와 같은 User 클래스가 있다고 해보죠.

User 클래스
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
그리고 아래와 같이 서로 다른 형태의 정보를 갖고 유저 인스턴스를 만들어야 한다면?

info_string = "강영훈,younghoon@codeit.kr,123456"
info_list = ["이윤수", "yoonsoo@codeit.kr", "abcdef"]
문자열은 쉼표(,)를 기준으로 분리하면 되겠고, 리스트는 각 인덱스의 요소를 가져오면 되겠죠?

아래 코드를 볼까요?

다양한 형태의 정보로 유저 인스턴스 만들기
# 유저 인스턴스 만들기 (1): 문자열로 인스턴스 만들기
parameter_list = info_string.split(",") # split 메소드를 사용해서 쉼표(,)를 기준으로 문자열을 리스트로 분리한다

# 각 변수에 분리된 문자열 각각 저장
younghoon_name = parameter_list[0]
younghoon_email = parameter_list[1]
younghoon_password = parameter_list[2]

younghoon = User(younghoon_name, younghoon_email, younghoon_password)

# 유저 인스턴스 만들기 (2): 리스트로 인스턴스 만들기
yoonsoo_name = info_list[0]
yoonsoo_email = info_list[1]
yoonsoo_password = info_list[2]

yoonsoo = User(yoonsoo_name, yoonsoo_email, yoonsoo_password)

# 인스턴스가 제대로 생성되었는지 확인
print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)

# 결과)
강영훈 younghoon@codeit.kr 123456
이윤수 yoonsoo@codeit.kr abcdef
'''
# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
        
#     @classmethod
#     def from_string(cls, string_params):
#         # 여기에 코드를 작성하세요
#         string_to_list = string_params.split(",")
#         return cls(string_to_list[0], string_to_list[1], string_to_list[2])

#     @classmethod
#     def from_list(cls, list_params):
#         # 여기에 코드를 작성하세요
#         return cls(list_params[0], list_params[1], list_params[2])
    
# # 유저 생성 및 초기값 설정
# younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
# yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

# print(younghoon.name, younghoon.email, younghoon.password)
# print(yoonsoo.name, yoonsoo.email, yoonsoo.password)