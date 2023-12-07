def add(a,b):
    return a + b
    
def minus(a, b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b) :
    return a / b #실수형나누기

#__name__ : 실행되는 모듈
#__main__ : 이 모듈
#그럴 때만 실행되도록 하는 조건문
#다른 모듈에서 이 모듈(위에 함수 4개) 쓰려고 할 때 이 아래는 실행되지 않도록
if __name__=="__main__":
    x=int(input("정수 입력:")) 
    y=int(input("정수 입력:"))

    print(f'{x} + {y} = {add(x,y)}') #{}안에 함수 작성
    print(f'{x} - {y} = {minus(x,y)}')
    print(f'{x} * {y} = {mul(x,y)}')
    print(f'{x} / {y} = {div(x,y)}')
