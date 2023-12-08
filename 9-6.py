score = input("Enter the score:")
grade = []

try:
    score = int(score)
    print(score)
    if score>=90:
        grade[0] = 'A+'
    else:
        print("당신의 점수는 " + score)
except ValueError:
    print("형식 오류")
except IndexError:
    print("첨자 범위 오류")
except TypeError:
    print("데이터 타입 오류")
    print(f'당신의 점수는 {score}')
print("프로그램 종료")

score = input("Enter the score")
for digit in score:
    if digit not in "0123456789":
        raise ValueError("숫자값을 입력하지 않음")
score = int(score)
print(score)

while True:
    score = input("Enter the score:")
    for digit in score:
        if digit not in "0123456789":
            raise ValueError("숫자값을 입력하지 않음")
    score = int(score)
    print(score)
    