import string

n,output = int(input()),""


def convert(charGen):
    heap = []
 
    for c in charGen:
        if c in string.ascii_lowercase:
            heap.append(c)
        elif c in ['+', '-', '*', '/', '^']:
            nextchar = next(charGen)
            if nextchar=="(":
                heap = heap + convert(charGen)
            else:
                heap.append(nextchar)
            heap.append(c)
        elif c == "(":
            heap = heap + convert(charGen)
        elif c == ")":
            return heap
    return "".join(heap)


for i in range(n):
    _input = (i for i in input())
    output = output + "\n" + convert(_input)
print(output)
