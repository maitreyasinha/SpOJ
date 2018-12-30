import string

# n = int(input())
# global output, heap
# heap = []

# for i in range(1):
#     _input = input()


# def convert(charectors):
#     print("heap is ","".join(heap))
#     # print("Into convert Method")
#     output = ""
#     for i in charectors:
#         # print("i is %s"%i)
#         if i in string.ascii_lowercase:
#             heap.append(i)
#         elif i in "+,-,*,/,^".split(","):
#             print("character is %s"%i)
#             convert(charectors)
#             print("Appending",i)
#             heap.append(i)
#             print(heap)
#         elif i == "(":
#             convert(charectors)
#         elif i == ")":
#             output = output + "".join(heap)
#             print("output",output)
#             return output
#
#     return heap

global output
output = ""

def convert2(chargen):
    heap = []

    for c in chargen:
        if c in string.ascii_lowercase:
            heap.append(c)
        elif c in "+,-,*,/,^".split(","):
            nextchar = next(chargen)
            if nextchar=="(":
                heap.append(convert2(chargen))
            else:
                heap.append(nextchar)
            heap.append(c)
        elif c=="(":
            heap.append(convert2(chargen))
        elif c == ")":
            return heap
    return heap

_input = "(b+(a+c))^(c+d)"
# _input = "(a+b)"
gen = (i for i in _input)
output = convert2(gen)
# print("".join(output))
print(output)