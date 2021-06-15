# if __name__ == “__main__”은 왜 필요할까?

위의 코드는 해석 그대로  
`__name__이라는 변수의 값이 __main__이라면 아래의 코드를 실행한다.` 라는 뜻이다.
이를 이해하려면 먼저 파이썬의 코드 실행 방식과 `__name__`이라는 내장 변수를 알아야 한다.

C 언어와 java같은 경우에은 main문이 있지만,  
파이썬은 main문 대신에, 들여쓰기가 되지 않은 level0의 코드를 가장 먼저 실행시킨다.

**`__name__`**
파이썬은 다양한 정보를 담고있는 내장변수가 존재한다. 이 중에서 `__name__`이라는 내장변수를 알아보자.   
`__name__`은 현재 모듈의 이름을 담고있는 내장 변수이다.  
직접 실행된 모듈의 경우 `__main__` 이라는 값을 가지게 되며, 직접 실행되지 않은 import된 모듈은 모듈의 이름(파일명)을 가지게 된다. 

(jupyter notebook에서는 안됩니다. 이유는 아직 찾고 있습니다.)
VSC에서 
```
#module.py

def hello():
    print("Hello!")

print(__name__)
```
위의 python 파일을 저장하고

```
#main.py

import module

print(__name__)
print('----------')
module.hello()
```
위의 파일을 실행하면 `__name__`에 `module`이 함께 출력되어 나온다. 
![Screenshot from 2021-06-15 11-10-38](https://user-images.githubusercontent.com/74230043/121982803-323f5a80-cdcb-11eb-8ebb-84d5d3beedbe.png)  
module.py에 `if __name__ == "__main__"`을 추가하고 출력해보자.
```
# module2.py

def hello():
    print("Hello!")

if __name__=="__main__":
    print(__name__)
```
을 저장하고  

```
# main2.py
import module2

print(__name__)
print('----------')
module2.hello()
```
main2.py를 실행하면 `module`출력없이 아래와 같이 출력된다.  
![Screenshot from 2021-06-15 13-57-04](https://user-images.githubusercontent.com/74230043/121995295-abe24300-cde1-11eb-8ae9-024bf376c58c.png)  
