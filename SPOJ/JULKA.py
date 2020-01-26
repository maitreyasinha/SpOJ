s = ""
getNum = lambda num:num.as_integer_ratio()[0]

for i in range(1):
    total = float(input())
    exc = float(input())
    nt = (getNum(total) - getNum(exc)) / 2
    kl = nt + exc

    s = s + getNum(kl).__str__() + "\n" + nt.__str__() + "\n"
print(s)
