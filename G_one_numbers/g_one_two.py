import functools, time

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
d100 =  {0: 37, 1: 37, 2: 37, 3: 35, 4: 34, 5: 33, 6: 32, 7: 32, 8: 32, 9: 31, 10: 30,
      11: 28, 12: 26, 13: 26, 14: 26, 15: 25, 16: 24, 17: 23, 18: 22, 19: 23, 20: 24,
      21: 24, 22: 24, 23: 23, 24: 22, 25: 23, 26: 24, 27: 25, 28: 26, 29: 26, 30: 26,
      31: 27, 32: 28, 33: 28, 34: 28, 35: 27, 36: 26, 37: 25, 38: 24, 39: 22, 40: 20,
      41: 19, 42: 18, 43: 19, 44: 20, 45: 20, 46: 20, 47: 20, 48: 20, 49: 22, 50: 24,
      51: 24, 52: 24, 53: 23, 54: 22}

d1000 = {0: 340, 1: 333, 2: 324, 3: 313, 4: 304, 5: 296, 6: 288, 7: 280, 8: 271, 9: 261, 10: 253,
         11: 247, 12: 243, 13: 241, 14: 238, 15: 234, 16: 232, 17: 232, 18: 234, 19: 238, 20: 241,
         21: 243, 22: 246, 23: 250, 24: 255, 25: 261, 26: 265, 27: 267, 28: 267, 29: 265, 30: 261,
         31: 255, 32: 247, 33: 237, 34: 228, 35: 220, 36: 213, 37: 207, 38: 202, 39: 198, 40: 198,
         41: 202, 42: 207, 43: 213, 44: 217, 45: 219}


counter = lambda beg: len([i for i in primes if (i >= beg and i <= beg + 9)])
counter_range  = lambda beg,end: len([i for i in primes if (i>=beg and i<=end)])

numDict = dict([(i,counter(i)) for i in range(72)])

sumOfDigits = lambda number : sum(map(int, str(number)))
##################################################################
def find_actual(lower, upper):
    a = [i for i in range(lower,upper+1) if sumOfDigits(i) in primes]
    return len(a)

def find_same(beg, end):
    if beg==end:
        return 1 if sumOfDigits(beg) in primes else 0
    elif end-beg< 10:
        return find_actual(beg, end)

    beg_index, end_index = int(beg/10), int(end/10)
    count = counter_range(sumOfDigits(beg),sumOfDigits((beg_index+1)*10-1))
    count += functools.reduce(lambda a,b:a+b, [counter(sumOfDigits(i * 10)) for i in range((beg_index+1), end_index)]) if (end_index-beg_index)>1 else 0
    count += counter_range(sumOfDigits(end_index*10), sumOfDigits(end)) if (end_index-beg_index) else 0
    return count

def find100(n1, n2):
    tn = 0
    if (n2-n1)<100:
        tn += find_same(n1,n2)
    else:
        start, end = (int(n1/100)+1),(int(n2/100))
        for i in range(start, end):
            # print(d.get(sumOfDigits(i)))
            tn = tn + d100.get(sumOfDigits(i))
        tn += find_same(n1,start*100-1)
        tn += find_same(end*100,n2)
    return tn

def find1000(n1,n2):
    tn = 0
    if n2-n1 < 1000:
        tn += find100(n1,n2)
    else:
        start, end = (int(n1 / 1000) + 1), (int(n2 / 1000))
        for i in range(start, end):
            tn = tn + d1000.get(sumOfDigits(i))
        tn += find100(n1, start * 1000 - 1)
        tn += find100(end * 1000, n2)
    return tn


##################################################################
if __name__ == '__main__':
    n = int(input())
    # n = 1
    output = ""

    for i in range(n):
        # lower, upper = 1, 100000000
        lower, upper = (eval(i) for i in input().split())
        # t = time.time()
        output = output + "\n" + str(find1000(lower,upper))
        # t_end = time.time() - t
        # print("Evaluation Time : ", t_end)

    print(output)

    # beg, (beg_index+1)*10-1, end_index*10, end
    # (12, 19, 1440, 1443)