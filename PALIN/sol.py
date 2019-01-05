


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
    c = 1
    if num1[-c] != "9":
        return num1[:-c]+str(int(num1[-c])+1)
    while num1[-c] == "9":
        num1 = num1[:-c]+"0"+(num1[-c+1:len(num1)] if c!=1 else "")
        c += 1
        if c==len(num1)+1:
            return "1" + num1

    return num1[:-c] + str(int(num1[-c])+1) + num1[-c+1:]


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

path = '/Users/maitreyasinha/Workspace/SpOJ/PALIN/stdin.in.txt'
import sys,io, time
std_in = "".join(open(path).readlines())
sys.stdin = io.StringIO(std_in)

start_time = time.time()

n, output = int(input()), []
for i in range(n):
    _inp = input()
    output.append( convert(_inp))

for i in output:
    print("".join(i))

print("\nElapsed_time :", time.time() - start_time)