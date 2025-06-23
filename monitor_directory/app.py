#import mod1 
#ctrl + space 하면 참조가능한 모듈이 나오므로 참고
#from mod1 import PI,add,sub
#from mod1 import *
#import mod1 as mo # mo.add(10,2) 이런식으로 별칭을 붙일 수도 있음
import mod.mod1 as mo

print('모듈 이름: ', __name__)


# print(mod1.PI)
# print(mod1.add(10, 200))
# print(mod1.sub(10, 3))

print(mo.PI)
print(mo.add(100,20))
print(mo.sub(10,1)) 




