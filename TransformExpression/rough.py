import string
global test

test=[]
gen = (i for i in list(["a","b","c","d","e"]))
def tester(charGen):
    heap = []
    for i in charGen:
        print(i,i in ["a", "e", "c"],type(i),type(["a", "e", "c"][2]))
        print()
        if i in ["a", "e", "c"]:
            print("i is %s"%i)
            heap.append(i)
            print("heap",heap)
        else:
            print(next(charGen))
            tester(charGen)


tester(gen)
