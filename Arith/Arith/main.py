import re

num_inputs = 3 or int(input())


def create_operation(num1,num2, operation):
    if operation in ["+","-"]:
        l1,l2, result = len(num1),len(num2)+1, str(int(num1)+int(num2)) if operation == "+" else str(int(num1)-int(num2))
        tl = l1 if l1 > l2 else l2
        str_output = " "*(tl-l1) + num1 + "\n" + " "*(tl-l2) + operation + num2 + "\n" + "-"*tl + "\n" + " "*(tl - len(result)) + result
        return str_output
    elif operation in ["*"]:
        result = str(int(num1)*int(num2))
        tl,l1,l2 = len(result),len(num1), len(num2)
        str_output = " "*(tl - l1) + num1 + "\n" + " "*(tl-l2-1) + operation + num2 + "\n" + " "*(tl - (l1 if l1>l2+1 else l2+1))  + "-"*(l1 if l1>l2+1 else l2+1) + "\n"
        for i in range(-1,-len(num2)-1,-1):
            temp_result = str(int(num1)*int(num2[i]))
            str_output = str_output + " "*(tl - len(temp_result) + 1 + i) + temp_result + "\n"
        return str_output + "-"*tl + "\n" + result


for i in range(num_inputs):
    str_operation = input()

    if "+" in str_operation:
        [num1,num2], operation = str_operation.split("+"),"+"
    elif "-" in str_operation:
        [num1, num2], operation = str_operation.split("-"),"-"
    elif "*" in str_operation:
        [num1, num2], operation = str_operation.split("*"), "*"
    else:
        pass

    print(create_operation(num1,num2,operation))