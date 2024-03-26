'''
__init__ 파일이란?
패키지 안에는 __init__.py라는 파일이 있습니다. 
__init__.py 파일 (지금부터는 그냥 init 파일이라고 하겠습니다) 은 '이 폴더는 파이썬 패키지다'라고 말해 주는 파일입니다.
파이썬 3.3 이전 버전에서는 init 파일이 필수였습니다. 
디렉토리 안에 init 파일이 없으면 디렉토리가 패키지로 인식되지 않아서 패키지를 임포트할 수 없었습니다.
파이썬 3.3 이후 버전부터는 init 파일이 필수가 아니게 됐지만 
파이썬 하위 버전과의 호환성과 패키지의 명확성을 위해 항상 패키지 안에 init 파일을 만들어 주는 것을 권장 드립니다.
init은 'initialize'라는 단어를 줄인 건데요. 
initialize는 초기화를 뜻합니다. 
우리가 처음으로 패키지나 패키지 안에 있는 어떤 것을 임포트하면 가장 먼저 패키지의 init 파일에 있는 코드가 실행됩니다.
'''
# __all__ = ['area', 'volume']

# PI = 3.14
from mymath.shapes import area, volume
# 상대경로로 임포트
# from . import area, volume 
# from .area import *
# from .volume import *

PI = 3.14