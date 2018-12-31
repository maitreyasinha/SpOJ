n, output = int(input()), ""

def add(li):
    if li==[]:
        return ["1"]
    elif li[-1]=="9":
        return add(li[:-1])+["0"]
    else:
        li[-1]= str(int(li[-1])+1)
        return li

def createPalindrome(num):
    length = len(num)
    center = int((len(num))/2)

    createNum = lambda x:int("".join(x))

    if length%2 == 0:
        left,right = num[:center], num[length:center-1:-1]
        print("left",left,"right",right)

        for char in range(center):
            increment_flag=True
            if left[-1-char] < right[char]:
                increment_flag = True
                break
            elif left[i]> right[i]:
                increment_flag = False
                break
            else:
                continue

        if increment_flag:
            print("left >> ",add(left), add(left)[-2::-1])
            return add(left) + add(left)[-2::-1]
        else:
            return left + left[::-1]
    else:
        if createNum(num[:center]) <= createNum(num[length:center:-1]):
            assignment = list(str(createNum(num[:center]) + 1))
        return assignment + assignment[::-1]

for i in range(n):
    _input = list(input())
    output = output + "\n" + "".join(createPalindrome(_input))

print(output)