def getnUglyNumbers(n):
    max_power = int(n/4)
    if n%4 == 0:
        return (2**max_power)*(3**max_power)*(5**max_power)
    elif n%4 == 1:
        return (2 ** (max_power+1)) * (3 ** max_power) * (5 ** max_power)
    elif n%4 == 2:
        return (2 ** max_power) * (3 ** (max_power + 1)) * (5 ** max_power)
    elif n%4 == 3:
        return (2 ** max_power) * (3 ** max_power) * (5 ** (max_power + 1))

for i in range(10):
    print("max n %s >> "%i,getnUglyNumbers(i))