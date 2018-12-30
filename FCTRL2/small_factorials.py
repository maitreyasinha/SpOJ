n = int(input())
output = ""

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

for i in range(n):
    _input = int(input())
    output = output + "\n" + str(factorial(_input))
print(output)
