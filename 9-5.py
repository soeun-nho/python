for i in range(20):
    try:
        result=10//i
    except ZeroDivisionError as e:
        print(e)
    else: print(result)

score = input("Enter the score:")

try:
    score = int(score)
except ValueError as e:
    print(e)
    print("입력 자료형 오류 (ValueError)")
else:
    print(score)
finally:
    print("프로그램 종료")