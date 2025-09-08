import random

number = random.randint(1, 20)
guess = int(input("1부터 20 사이의 숫자를 맞춰보세요: "))

if guess == number:
    print("정답입니다!")
else:
    print(f"틀렸습니다. 정답은 {number}였습니다.")
