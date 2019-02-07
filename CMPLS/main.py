output_string = ""
num_seq = int(input())


def recurse_diff(l1, new_elems_len, depthofrecursion):
    if depthofrecursion == 1:
        return [l1[0]]*(new_elems_len+1)
    depthofrecursion -= 1
    diff_list = recurse_diff(list(map(lambda a, b: a-b, l1[1:], l1[:-1])), new_elems_len, depthofrecursion)
    for i in range(len(l1) - 1, len(diff_list)):
        l1.append(l1[i] + diff_list[i])
    return l1


for i in range(num_seq):
    [elems_len, new_elems_len] = [int(j) for j in input().split(" ")]
    elems_list = [int(elem) for elem in input().split(" ")]
    output_list = recurse_diff(elems_list,new_elems_len,elems_len)[elems_len:]
    output_string = output_string + " ".join((str(elem) for elem in output_list)) + "\n"


print(output_string)