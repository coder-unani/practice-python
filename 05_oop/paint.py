# 추상클래스를 상속받기 위해서는 아래와 같이 ABC 클래스를 import 해야 한다.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    
class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        result = "\n"
        for i in range(self.height):
            result += "* " * self.width + "\n"
        print(result)

    def __str__(self):
        return f"밑변 {self.width}, 높이 {self.height}인 직사각형"

class Circle(Shape):
    """원 클래스"""
    def __init__(self, diameter):
        self.diameter = diameter
    
    def draw(self):
        radius = self.diameter / 2 - .5
        r = (radius + .25) ** 2 + 1
        result = "\n"
        for i in range(self.diameter):
            y = (i - radius) ** 2
            for j in range(self.diameter):
                x = (j - radius) ** 2
                if x + y <= r:
                    result += "* "
                else:
                    result += "  "
            result += "\n"
        print(result)
    
    def __str__(self):
        return f"지름 {self.diameter}인 원"

class EquilatetralTriangle(Shape):
    """정삼각형 클래스"""
    def __init__(self, side):
        self.side = side

    def draw(self):
        result = "\n"
        for i in range(self.side + 1):
            result += " " * (self.side - i) + "* " * i + "\n"
        print(result)

    def __str__(self):
        return f"한 변이 {self.side}인 정삼각형"

class RightTriangle(Shape):
    """직각삼각형 클래스"""
    def __init__(self, stool):
        self.stool = stool

    def draw(self):
        result = "\n"
        for i in range(self.stool):
            result += "* " * (i + 1) + "\n"
        print(result)

    def __str__(self):
        return f"변이 {self.stool}인 직각이등변삼각형"
    
class Paint:
    """그림판 클래스"""
    def __init__(self):
        self.shapes = []
    
    def add(self, shape: Shape):
        """
        파라미터 shape 도형을 추가한다
        파라미터 shape는 Shape 클래스를 상속받은 클래스의 인스턴스여야 한다
        """
        self.shapes.append(shape)

    def draw(self, index):
        """파라미터 인덱스에 해당하는 도형을 그린다"""
        if 0 <= index < len(self.shapes):
            self.shapes[index].draw()
        else:
            print("인덱스를 확인해주세요")
    
    def draw_all(self):
        """그림판에 있는 모든 도형을 그린다"""
        if not self.shapes:
            print("그릴 도형이 없습니다")
        
        for shape in self.shapes:
            shape.draw()
    
    def __str__(self):
        """"""
        result = "\n그림판 안에 있는 도형들:\n"
        for i in range(len(self.shapes)):
            result += f"    {i}: {self.shapes[i]}\n"
        return result
    

rectangle1 = Rectangle(7, 8)
rectangle2 = Rectangle(4, 6)
circle = Circle(9)
triangle = EquilatetralTriangle(7)
triangle2 = RightTriangle(7)

paint = Paint()

paint.add(rectangle1)
paint.add(rectangle2)
paint.add(circle)
paint.add(triangle)
paint.add(triangle2)

print(paint)
paint.draw(0)
paint.draw(2)

paint.draw_all()

'''
# 이런식으로 getter 메소드를 추상 메소드로 지정하면 변수도 강제 할 수 있다
class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def draw(self):
        """콘솔에 도형을 그린다"""
        pass

    @property
    @abstractmethod
    def x(self):
        """도형의 x 좌표 getter 메소드"""
        pass

    @property
    @abstractmethod
    def y(self):
        """도형의 y 좌표 getter 메소드"""
        pass

'''