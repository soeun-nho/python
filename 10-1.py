f = open("textfiles/dream1.txt", "r")

for line in f:
    line = line.rstrip()
    print(line, end="")
f.close()

try:
    f = open("textfiles/dream1.txt", "r")
except FileNotFoundError as e:
    print(e)
    print("파일을 찾을 수 없습니다.")
else:
    for line in f:
        line = line.rstrip()
        print(line, end="")
    f.close()