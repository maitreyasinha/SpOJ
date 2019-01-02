n, output = int(input()), ""


def compare(num1, num2):
    for i in range(len(num2)):
        if num1[-1-i] > num2[i]:
            return False
        elif num1[-1-i] < num2[i]:
            return True
        else:
            continue
    return True


def increment(num1):
    if len(num1) == 0:
        return ["1"]
    elif num1[-1] == "9":
        return increment(num1[:-1])+["0"]
    else:
        return num1[:-1] + [str(int(num1[-1])+1)]


def convert(num):
    if num == ["9"]:
        return ["1", "1"]
    center = int(len(num)/2)
    left = num[:center]
    if len(num)%2 == 0:
        left = increment(left) if compare(left, num[center::]) else left
        return left + left[-1-len(left)+len(num[center:])::-1]
    else:
        left = increment(num[:center+1]) if compare(left, num[center+1::]) else num[:center+1]
        return left + left[-2-len(left) + center + 1::-1]


for i in range(n):
    _inp = input()
    output = output + "\n" + "".join(convert(_inp))


print(output)
