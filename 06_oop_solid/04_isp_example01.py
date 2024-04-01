'''
요즘은 프린터의 기능이 많아져서 인쇄 기능뿐만 아니라 스캔 기능이 있는 것들도 많은데요. 
이런 프린터를 추상화한 IPrinter 인터페이스를 만들어 봅시다. 
다음 코드를 보시죠.

from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print_file(self, file:str) -> bool:
        """문서 출력 메소드"""
        pass

    @abstractmethod
    def scan(self, content:str) -> bool:
        """문서 스캔 메소드"""
        pass
        
그런데 프린터 중에는 인쇄 기능만 있고 스캔 기능은 없는 것들도 있습니다. 
그런데 이런 프린터들이 단지 프린터라는 이유만으로 IPrinter 인터페이스를 상속받게 되면 
정작 스캔 기능이 없는데도 scan() 메소드를 오버라이딩해야 합니다. 
예를 들어 LGPrinter는 스캔 기능이 없다고 가정해 볼게요. 
그런데 지금 템플릿을 보면 LGPrinter 클래스는 불필요하게 scan() 메소드를 오버라이딩하고 있습니다. 
이것이 바로 필요없는 메소드의 구현을 강제하는 코드 즉, 인터페이스 분리 원칙을 위반한 코드입니다.

코드를 인터페이스 분리 원칙에 부합하는 코드로 리팩토링해 보세요!

from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print_file(self, file:str) -> bool:
        """문서 출력 메소드"""
        pass

    @abstractmethod
    def scan(self, content:str) -> bool:
        """문서 스캔 메소드"""
        pass
    
    
class SamsungPrinter(IPrinter):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력 중입니다!".format(file))
            return True
        return False

    def scan(self, content):
        """문서 스캔 메소드"""
        if self.is_connected:
            print("{}을/를 이미지 파일로 저장합니다.".format(content))
            return True
        return False 
    
    
class LGPrinter(IPrinter):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력합니다.".format(file))
            return True
        return False

    def scan(self, content):
        """LG 프린터는 스캔 기능이 없기 때문에 False 리턴"""
        print("이 프린터는 문서를 스캔하는 기능이 없습니다.")
        return False 
    

samsung_printer = SamsungPrinter(True, True, True)
lg_printer = LGPrinter(True, True, True)

samsung_printer.print_file("4월 보고서.docx")
lg_printer.print_file("4월 보고서.docx")

samsung_printer.scan("스캔 테스트 문서")
lg_printer.scan("스캔 테스트 문서")    

print(SamsungPrinter.mro())
print(LGPrinter.mro())  
'''

from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print_file(self, file:str) -> bool:
        """문서 출력 메소드"""
        pass


class IScanner(ABC):
    @abstractmethod
    def scan(self, content:str) -> bool:
        """문서 스캔 메소드"""
        pass
    
    
class SamsungPrinter(IPrinter, IScanner):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력 중입니다!".format(file))
            return True
        return False

    def scan(self, content):
        """문서 스캔 메소드"""
        if self.is_connected:
            print("{}을/를 이미지 파일로 저장합니다.".format(content))
            return True
        return False 
    
    
class LGPrinter(IPrinter):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력합니다.".format(file))
            return True
        return False
    

samsung_printer = SamsungPrinter(True, True, True)
lg_printer = LGPrinter(True, True, True)

samsung_printer.print_file("4월 보고서.docx")
lg_printer.print_file("4월 보고서.docx")

samsung_printer.scan("스캔 테스트 문서")
# lg_printer.scan("스캔 테스트 문서")    

print(SamsungPrinter.mro())
print(LGPrinter.mro())