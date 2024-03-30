'''
DeliveryMan 클래스
이제 직원(Employee) 클래스를 상속해서 배달원을 나타내는 DeliveryMan 클래스를 만들어 봅시다. 
상속 후에 아래 내용들이 무엇일지 생각하며 코드를 작성해 보세요.

부모 클래스로부터 그대로 물려받을 내용
부모 클래스로부터 물려받은 후 바꿀 내용
아예 새로 추가할 내용
템플릿에 있는 DeliveryMan 클래스가 Employee 클래스를 상속받도록 코드를 수정하면 됩니다.
'''
class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03
    
    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self.wage *= self.raise_percentage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class DeliveryMan(Employee):
    """배달원 클래스"""

    def __init__(self, name, wage, on_standby):
        super().__init__(name, wage)
        self.on_standby = on_standby

    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 메시지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원 복귀를 처리한다"""
        self.on_standby = True

    def __str__(self):
        return DeliveryMan.company_name + " 배달원: " + self.name
    

taeho = DeliveryMan("성태호", 7000, True)

taeho.raise_pay()
print(taeho.wage)

taeho.deliver("경기도 남양주시 덕소로 206 최고 건물 401호")
taeho.deliver("경기도 남양주시 덕소로 206 최고 건물 402호")

taeho.back()
taeho.deliver("경기도 남양주시 덕소로 206 최고 건물 402호") 

print(taeho)

print(DeliveryMan.mro())