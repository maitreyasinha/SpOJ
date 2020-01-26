import functools

n = int(input())
output = ""

def isPrime(i):
    for divisor in range(2,int(i**0.5)+1):
        if i%divisor == 0:
            return False
    return True

primes = [2] + [ i for i in range(3,72,2) if isPrime(i)]

sumOfDigits = lambda number : sum(map(int, str(number)))

counter_range  = lambda beg,end: len([i for i in primes if (i>=beg and i<=end)])
counter = lambda beg: len([i for i in primes if (i >= beg and i <= beg + 9)])

def find(beg, end):
    beg_index, end_index = int(beg/10) + 1, int(end/10)
    count = counter_range(sumOfDigits(beg),sumOfDigits(beg_index*10-1))
    count += functools.reduce(lambda a,b:a+b, [counter(sumOfDigits(i * 10)) for i in range(beg_index, end_index)])
    count += counter_range(sumOfDigits(end_index*10), sumOfDigits(end))
    return count

import time

for i in range(n):
    lower, upper = (eval(i) for i in input().split())

    t = time.time()
    output = output + "\n" + str(find(lower,upper))
    t_end = time.time() - t
    print("Evaluation Time : ", t_end)

print(output)