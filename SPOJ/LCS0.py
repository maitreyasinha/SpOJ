#To find the Largest Common Substring
import numpy as np
import string
import time

def ar_sum(a):
    result = 0
    count = 0
    for i in range(0,len(a)):
        if a[i]==1:
            count += 1
        else:
            result = max(result,count)
            count = 0
    return max(result,count)

def dynamic_find_largest_common_subs(a,b):
    a = [i for i in a if i in b]
    b = [i for i in b if i in a]
    stack = np.zeros((len(a),len(b)))
    for j in range(len(a)):
        stack[j] = np.array([int(i==a[j]) for i in b])
    return stack


# s1 = "dynamictutorialProgramming"
# s2 = "tutorialhorizon"

# s1 = "bcaaaade"
# s2 = "deaaaabc"

# s1 = "abababab"
# s2 = "bcbb"
#
# s1 = string.ascii_letters*500
# s2 = string.ascii_letters*500

s1 = input()
s2 = input()
# t = time.time()
stack = dynamic_find_largest_common_subs(s1,s2)
print(max([ar_sum(stack.diagonal(offset=i)) for i in range(-stack.shape[0],stack.shape[1])]))
# print(time.time()-t)

# print("="*20)
#
# t = time.time()
# stack = dynamic_find_largest_common_subs_prev(s1,s2)
# print(max([ar_sum(stack.diagonal(offset=i)) for i in range(-stack.shape[0],stack.shape[1])]))
# print(time.time()-t)

#alsdfkjfjkdsal
#fdjsk a l ajfkdsla

#dynamictutorialProgramming
#tutorialhorizon


# bcaaaade
# deaaaabc