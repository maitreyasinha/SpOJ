import time
sumOfDigits = lambda number : sum(map(int, str(number)))

def isPrime(i):
    for divisor in range(2,int(i**0.5)+1):
        if i%divisor == 0:
            return False
    return True

primes = [2] + [ i for i in range(3,72,2) if isPrime(i)]

# def sumOfDigits(i):
#     if i/10==0:
#         return 0
#     else:
#         return i%10 + int(sumOfDigits(i/10))

a = 10**9-1

def compare(a):
    print("Sum of digits using function")
    t = time.time()
    x1 = sumOfDigits(a)
    t_end = time.time() - t
    print(a)
    print((t_end)*1000)

    print("Sum of digits using lambda")
    t = time.time()
    x2 = sdigit(a)
    t_end2 = time.time() - t
    print(x1)
    print((t_end2)*1000)

    print("Improvement: ", t_end/t_end2)

# compare(a)

def analyzeSum(num1,num2):
    counter, prev_counter = 0,0
    for i in range(num1, num2+1):
        if i%10==0:
            print("=======  ",counter-prev_counter)
            prev_counter = counter
        if sumOfDigits(i) in primes:
            counter+=1
        print(i, sumOfDigits(i))

# analyzeSum(1,30)

def testSum(num):
    print((num/10 + 1)*10)

    next = (num/10 + 1)*10
    beg, end = sumOfDigits(num), sumOfDigits(next)
    filterObj = filter(lambda x:x>=beg and x<=end,primes)
    for i in filterObj:
        print(i)
    return num

# testSum(4)


def analyze_counters():
    # counter1 = lambda beg, end: len([i for i in primes if (i >= beg and i <= end)])
    counter1 = lambda beg, end: len([i for i in primes if (i >= beg and i <= end)])
    counter2 = lambda beg: len([i for i in primes if (i >= beg and i <= beg+9)])
    # counter2 = lambda beg: len(list(filter(lambda x:x>=beg and x<=beg+9, primes)))

    t = time.time()
    counter1(9,18)
    t_end = time.time()-t
    print("Using Counter1 : ", t_end*1000)

    t = time.time()
    counter2(9)
    t_end = time.time() - t
    print("Using Counter2 : ", t_end*1000)

# analyze_counters()

counter_range  = lambda beg,end: len([i for i in primes if (i>=beg and i<=end)])
counter = lambda beg: len([i for i in primes if (i >= beg and i <= beg + 9)])

import functools

def main(beg, end):
    beg_index, end_index = int(beg/10) + 1, int(end/10)

    count = counter_range(sumOfDigits(beg),sumOfDigits(beg_index*10-1))

    t = time.time()
    for i in range(beg_index, end_index):
        start = sumOfDigits(i * 10)
        count += counter_range(start,start+9)
    t_end = time.time() - t
    print("Time using loops : ", t_end)

    #Use only one of below
    t = time.time()
    count += sum([counter(sumOfDigits(i * 10)) for i in range(beg_index, end_index)])
    t_end = time.time() - t
    print("Time using first : ", t_end)

    t = time.time()
    count += functools.reduce(lambda a,b:a+b, [counter(sumOfDigits(i * 10)) for i in range(beg_index, end_index)])
    t_end = time.time() - t
    print("Time using second : ", t_end)

    count += counter_range(sumOfDigits(end_index*10), sumOfDigits(end))
    print(count)

main(1,29)

