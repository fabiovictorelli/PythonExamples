
result = "fix"


def func(flag):
    global result
    if flag == True:
        result = "pre" + result
    if flag == False:
        result = "post" + result

    return result


def func2(flag):
    return ("prefix" if (flag == True) else "postfix")


def main():
    global result
    print("func True=", func(True))
    result = "fix"
    print("func False=", func(False))
    print("func2 True=", func2(True))
    print("func2 False=", func2(False))


if __name__ == "__main__":
    main()
