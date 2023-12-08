num = int(input("정수를 입력하시오:"))
divisors = [i for i in range(1, num+1) if num%i==0]

print(*divisors)

with open("textfiles/output2.txt", "w") as file:
    file.write(f"{num}: {' '.join(map(str, divisors))}")