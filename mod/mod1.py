print('mod/mod1.py 시작')

print('모듈 이름: ', __name__)
PI = 3.14 # 변수

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

print('mod/mod1.py 끝')

if __name__ == '__main__':
    print(PI)
