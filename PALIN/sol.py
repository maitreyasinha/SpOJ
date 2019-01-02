n, output = int(input()), ""

def compare(num1,num2):
    if len(num1)==0 or len(num2)==0:
        return True
    elif int(num1[-1]) > int(num2[0]):
        return False
    elif int(num1[-1]) < int(num2[0]):
        return True
    else:
        return compare(num1[:-1:],num2[1::])

def incrment(num1):
    if len(num1)==0:
        return ["1"]
    elif num1[-1]=="9":
        return incrment(num1[:-1])+["0"]
    else:
        return num1[:-1] + [str(int(num1[-1])+1)]

def convert(num):
    if num == ["9"]:
        return ["1","1"]
    if len(num)%2==0:
        center = int(len(num)/2)
        left = num[:center]
        if compare(left,num[center::]):
            left = incrment(left)
        return left + left[-1-len(left)+len(num[center:])::-1]
    else:
        center = int(len(num)/2)
        left = num[:center]
        if compare(left,num[center+1::]):
            left = incrment(num[:center+1])
        else:
            left = num[:center+1]
        num = left + left[-2-len(left) + center + 1 ::-1]
        return num


for i in range(n):
    _inp = list(input())
    output = output + "\n" + "".join(convert(list(_inp)))


print(output)