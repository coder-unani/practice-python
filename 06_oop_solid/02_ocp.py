# class AppleKeyboard:
#     """애플 키보드 클래스"""

#     def __init__(self):
#         """키보드 인풋과 터치바 인풋"""
#         self.keyboard_input = ""

#     def set_keyboard_input(self, input):
#         """키보드 인풋 저장 메소드"""
#         self.keyboard_input = input

#     def send_keyboard_input(self):
#         """키보드 인풋 전송 메소드"""
#         return self.keyboard_input

# class SamsungKeyboard:
#     def __init__(self):
#         """키보드 인풋"""
#         self.user_input = ""

#     def save_user_input(self, input):
#         """키보드 인풋 저장 메소드"""
#         self.user_input = input
    
#     def get_user_input(self):
#         """키보드 인풋 전송 메소드"""
#         return self.user_input

# class KeyboardManager:
#     def __init__(self):
#         """키보드 관리 클래스"""
#         self.keyboard = None

#     def connect_to_keyboard(self, keyboard):
#         """키보드 교체 메소드"""
#         self.keyboard = keyboard

#     def get_keyboard_input(self):
#         """유저가 키보드로 입력한 내용을 받아오는 메소드"""
#         # 새로운 키보드가 추가될 때마다 코드를 수정해야 함
#         # 이는 OCP(개방 폐쇄 원칙)를 위반하는 코드
#         if isinstance(self.keyboard, AppleKeyboard):
#             return self.keyboard.send_keyboard_input()
#         elif isinstance(self.keyboard, SamsungKeyboard):
#             return self.keyboard.get_user_input()

# # Apple Keyboard 연결
# keyboard_manager = KeyboardManager()
# apple_keyboard = AppleKeyboard()
# keyboard_manager.connect_to_keyboard(apple_keyboard)

# apple_keyboard.set_keyboard_input("안녕하세요")

# print(keyboard_manager.get_keyboard_input())  # 안녕하세요

# # Samsung Keyboard 연결
# samsung_keyboard = SamsungKeyboard()
# keyboard_manager.connect_to_keyboard(samsung_keyboard)

# samsung_keyboard.save_user_input("안녕하세요")

# print(samsung_keyboard.get_user_input())  # 안녕하세요

from abc import ABC, abstractmethod

class Keyboard(ABC):
    """키보드 클래스"""

    @abstractmethod
    def save_input(self):
        """키보드 입력 메소드"""
        pass

    def send_input(self):
        """키보드 입력 전송 메소드"""
        pass

class AppleKeyboard(Keyboard):
    """애플 키보드 클래스"""

    def __init__(self):
        """키보드 인풋과 터치바 인풋"""
        self.keyboard_input = ""

    def save_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.keyboard_input = input

    def send_input(self):
        """키보드 인풋 전송 메소드"""
        return self.keyboard_input


class SamsungKeyboard(Keyboard):
    def __init__(self):
        """키보드 인풋"""
        self.user_input = ""

    def save_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.user_input = input

    def send_input(self):
        """키보드 인풋 전송 메소드"""
        return self.user_input
 
class KeyboardManager:
    def __init__(self):
        """키보드 관리 클래스"""
        self.keyboard = None

    def connect_to_keyboard(self, keyboard):
        """키보드 교체 메소드"""
        self.keyboard = keyboard

    def get_keyboard_input(self):
        """유저가 키보드로 입력한 내용을 받아오는 메소드"""
        return self.keyboard.send_input()

keyboard_manager = KeyboardManager()
apple_keyboard = AppleKeyboard()
samsung_keyboard = SamsungKeyboard()

keyboard_manager.connect_to_keyboard(apple_keyboard)
apple_keyboard.save_input("안녕하세요")
print(keyboard_manager.get_keyboard_input())  # 안녕하세요

keyboard_manager.connect_to_keyboard(samsung_keyboard)
samsung_keyboard.save_input("안녕하세요")
print(keyboard_manager.get_keyboard_input())  # 안녕하세요