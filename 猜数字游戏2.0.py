import random
while True:
    print("1.简单模式")
    print("2.困难模式")
    print("3.地狱模式")
    level = int(input("请选择你的难度："))

    if level == 1:
        num_max = 100
        time_max = 15
    elif level == 2:
        num_max = 1000
        time_max = 10
    elif level == 3:
        num_max = 2000
        time_max = 7

    secret = random.randint(1, num_max)

    for i in range(time_max):
        if level == 1:
            guess = int(input("请在1~100中猜一个数字，15次机会："))
        elif level == 2:
            guess = int(input("请在1~1000中猜一个数字，10次机会："))
        elif level == 3:
            guess = int(input("请在1~2000中猜一个数字，7次机会："))

        if guess == secret:
            print("猜对了")
            break
        elif guess > secret:
            print("太大了")
        else:
            print("太小了")
    else:
        print(f"答案是{guess}")
