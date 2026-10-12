import random

secret = random.randint(1,100)

for i in range(7):
    guess = int(input("猜一个1~100的数字："))

    if guess == secret:
        print("恭喜，猜对了")
        break
    elif guess < secret:
        print("太小了")
    else:
        print("太大了")
else:
    print(f"机会用完了，答案是{secret}")
