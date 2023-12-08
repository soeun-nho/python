score = input("점수 입력: ")
try:
    score = int(score)
    print("점수는 " + score)
except ValueError:
    print("입력 형식 잘못됨")
except TypeError:
    print("정수형 + 문자형 연산 불가능")
except:
    print("기타 사유로 에러")

for i in range(0,20):
    try:
        print(f'{i}는 {10//i}')
    except ZeroDivisionError as e:
        print(e)

try:
    for i in range(20):
        print(10//i)
except:
    print("에러 발견 후 exception..프로그램 종료")
    