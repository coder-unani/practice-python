class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        """세로와 가로"""
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산 메소드"""
        return self.width * self.height

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._height = value if value > 0 else 1


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1

rectangle_1 = Rectangle(4, 6)
rectangle_2 = Square(2)

rectangle_1.width = 3
rectangle_1.height = 7

print(rectangle_1.area())

rectangle_2.width = 3
rectangle_2.height = 7

print(rectangle_2.area())


# 부모 클래스는 가로만 설정하는데 자식 클래스는 가로와 세로를 동시에 설정한다.
# 이렇게 되면 부모 클래스의 기능을 사용하는 코드가 자식 클래스에 대입되었을 때 문제가 발생한다.
# 에러가 발생하지는 않지만 결과값이 의도와 다른 값이 출력된다 이는 리스코프 치환 원칙을 위반하는 것이다.
# 정사각형 클래스는 직사각형 클래스의 행동 규칙을 지키기 어렵다. 이런 경우는 상속을 하면 안된다.
        