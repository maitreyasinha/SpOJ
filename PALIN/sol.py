
def compare(num1, num2):
    """
    :param num1:
    :param num2:
    :return: True if num1 is less than or equal to num2 else False.
    """

    num2 = num2[::-1]
    comparison_list = [(i, j) for i, j in zip(num1, num2) if i != j]
    if not comparison_list:
        return True
    else :
        val = comparison_list[-1]
        if val[0] < val[1]:
            return True
        else :
            return False


def increment(num1):
    num1 = list(num1)
    c = 1
    if num1[-c] != "9":
        return num1[:-c]+[str(int(num1[-c])+1)]
    while num1[-c] == "9":
        num1[-c] = '0'
        c += 1
        if c==len(num1)+1:
            return ["1"] + num1

    num_list = num1[:-c] + [str(int(num1[-c]) + 1)] + num1[-c + 1:]

    return ''.join(num_list)


def convert(num):
    if num == "9":
        return list("11")
    center = int(len(num)/2)
    left = num[:center]
    if len(num)%2 == 0:
        left = increment(left) if compare(left, num[center::]) else left
        return list(left + left[-1-len(left)+len(num[center:])::-1])
    else:
        left = increment(num[:center+1]) if compare(left, num[center+1::]) else num[:center+1]
        return list(left + left[-2-len(left) + center + 1::-1])


n, output = int(input()), []

for i in range(n):
    _inp = input()
    output.append( convert(_inp))

for i in output:
    print("".join(i))