import random
def choose_difficulty():
    levels = {
        "easy" : ("简单",1, 50, 10),
        "diffcult": ("困难", 1, 100, 7),
        "hell_diffcult": ("地狱", 1, 500, 8),
    }
    print("选择你的难度：easy\t\tdiffcult\t\thell_diffcult")
    choice = input("请输入：").strip()
    return levels.get(choice,("困难", 1, 100, 7))
def play(low, high, max_tries):
    secret = random.randint(low, high)
    print(f"范围{low}~{high},一共{max_tries}次机会。")
    for tires in range(1, max_tries + 1):
        try:
            guess = int(input("来猜一猜："))
        except ValueError:
            print("请输入整数！")
            continue
        if guess == secret:
            print("恭喜你猜对了！")
            return True
        elif guess > secret:
            print("太大了！")
        else:
            print("太小了！")
    print(f"sorry,机会用完了，答案是{secret}")
    return False
def cycle():
    while True:
        name, low, high, max_tries = choose_difficulty()
        print(f"当前难度{name}")
        play(low, high, max_tries)

        again = input("还要再玩一把吗？（y/n）:").strip().lower()
        if again != "y":
            print("再见！")
            break
if __name__ == "__main__":
    cycle()