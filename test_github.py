def greet(name):
    """向指定用户打招呼"""
    return f"Hello, {name}! 合并两个分支的修改"


def add(a, b):
    """两数相加"""
    return a + b


if __name__ == "__main__":
    print(greet("World"))
    print(f"1 + 2 = {add(1, 2)}")
