n, output = int(input()), ""

def createPalindrome(num):
    oldNum = num.copy()
    length = len(num)
    center = int((len(num))/2)
    # center = center-1 if length%2 else center

    createNum = lambda x:int("".join(x))

    if length%2 == 0:
        if createNum(num[:center]) <= createNum(num[length:center-1:-1]):
            num[center-1] = str( createNum(num[center-1])+1 )
        num[length:center-1:-1] = num[:center]
    else:
        if createNum(num[:center]) <= createNum(num[length:center:-1]):
            num[center] = str( createNum(num[center])+1 )
        num[length:center:-1] = num[:center]

    return num


for i in range(n):
    _input = list(input())
    output = output + "\n" + "".join(createPalindrome(_input))

print(output)