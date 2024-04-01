from abc import ABC, abstractmethod
# class Sword:
#     """검 클래스"""
#     def __init__(self, damage):
#         self.damage = damage

#     def slash(self, other_character):
#         """검 사용 메소드"""
#         other_character.get_damage(self.damage)


# class GameCharacter:
#     """게임 캐릭터 클래스"""
#     def __init__(self, name, hp, sword: Sword):
#         self.name = name
#         self.hp = hp
#         self.sword = sword

#     def attack(self, other_character):
#         """다른 유저를 공격하는 메소드"""
#         if self.hp > 0:
#             self.sword.slash(other_character)
#         else:
#             print(self.name + "님은 사망해서 공격할 수 없습니다.")

#     def change_sword(self, new_sword):
#         """검을 바꾸는 메소드"""
#         self.sword = new_sword

#     def get_damage(self, damage):
#         """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
#         if self.hp <= damage:
#             self.hp = 0
#             print(self.name + "님은 사망했습니다.")
#         else:
#             self.hp -= damage

#     def __str__(self):
#         """남은 체력을 문자열로 리턴하는 메소드"""
#         return self.name + "님은 hp: {}이(가) 남았습니다.".format(self.hp)
    
# bad_sword = Sword(1)
# good_sword = Sword(100)

# game_character_1 = GameCharacter("Worrior", 100, bad_sword)
# game_character_2 = GameCharacter("Magician", 1000, good_sword)

# game_character_1.attack(game_character_2)
# game_character_1.attack(game_character_2)
# game_character_1.attack(game_character_2)

# game_character_2.attack(game_character_1)

# print(game_character_1)
# print(game_character_2)

# 사용하는 GameCharacter 는 상위 클래스이고 Sword 는 하위 클래스이다.
# GameCharacter 클래스는 attack 메소드를 사용할 때 Sword 클래스의 slash 메소드를 사용하고 있다.
# 이건 Sword 클래스의 smash 메소드가 완벽하게 동작하다는 전제가 깔린 코드이다.
# 만약 Sword 클래스에 smash 메소드가 없다면? 그러면 GameCharacter 클래스의 attack 메소드는 작동하지 않는다.
# 이런 코드는 의존 관계 역전 원칙에 위배된다.
# 이런 경우 추상화에 의존해야 한다

class IWeapon(ABC):
    """무기 인터페이스"""
    @abstractmethod
    def use_on(self, other_character):
        """다른 캐릭터를 공격하는 메소드"""
        pass

class Sword(IWeapon):
    """검 클래스"""
    def __init__(self, damage):
        self.damage = damage

    def use_on(self, other_character):
        """검 사용 메소드"""
        other_character.get_damage(self.damage)

class Gun(IWeapon):
    """총 클래스"""
    def __init__(self, damage):
        self.damage = damage

    def use_on(self, other_character):
        """총 사용 메소드"""
        other_character.get_damage(self.damage)

class GameCharacter:
    """게임 캐릭터 클래스"""
    def __init__(self, name, hp, weapon: IWeapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.weapon.use_on(other_character)
        else:
            print(self.name + "님은 사망해서 공격할 수 없습니다.")

    def change_sword(self, new_sword):
        """검을 바꾸는 메소드"""
        self.sword = new_sword

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 사망했습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        """남은 체력을 문자열로 리턴하는 메소드"""
        return self.name + "님은 hp: {}이(가) 남았습니다.".format(self.hp)
    
bad_sword = Sword(1)
good_sword = Sword(100)

gun = Gun(100)

game_character_1 = GameCharacter("Worrior", 100, bad_sword)
game_character_2 = GameCharacter("Magician", 1000, gun)

game_character_1.attack(game_character_2)
game_character_1.attack(game_character_2)
game_character_1.attack(game_character_2)

game_character_2.attack(game_character_1)

print(game_character_1)
print(game_character_2)