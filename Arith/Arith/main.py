num_inputs = int(input())

def create_operation(num1,num2, operation):
    if operation in ["+","-"]:
        l1,l2, result = len(num1),len(num2)+1, str(int(num1)+int(num2)) if operation == "+" else str(int(num1)-int(num2))
        tl = l1 if l1 > l2 else l2
        dash_len = len(result) if len(result) > l2 else l2
        str_output = " "*(tl-l1) + num1 + "\n" + " "*(tl-l2) + operation + num2 + "\n" + " "*(tl-dash_len) + "-"*dash_len + "\n" + " "*(tl - len(result)) + result
        return str_output + "\n"
    elif operation in ["*"]:
        result = str(int(num1)*int(num2))
        tl,l1,l2 = len(result) if len(result) > len(num2)+1 else len(num2)+1 ,len(num1), len(num2)
        str_output = " "*(tl - l1) + num1 + "\n" + " "*(tl-l2-1) + operation + num2 + "\n"
        if len(num2)!=1:
            temp_result = len(str(int(num1) * int(num2[-1])))
            str_output = str_output + " " * (tl - (temp_result if temp_result>l2+1 else l2+1)) + "-" * (temp_result if temp_result > l2 + 1 else l2 + 1) + "\n"
            for i in range(-1,-len(num2)-1,-1):
                temp_result = str(int(num1)*int(num2[i]))
                str_output = str_output + " "*(tl - len(temp_result) + 1 + i) + temp_result + "\n"

        str_output = str_output + " " * (tl - len(result)) + "-" * len(result) + "\n"
        return str_output + " " * (tl - len(result)) + result + "\n"

str_output = ""
for i in range(num_inputs):

    str_operation = input()

    if "+" in str_operation:
        [num1,num2], operation = str_operation.split("+"),"+"
    elif "-" in str_operation:
        [num1, num2], operation = str_operation.split("-"),"-"
    elif "*" in str_operation:
        [num1, num2], operation = str_operation.split("*"), "*"

    str_output = str_output + create_operation(num1,num2,operation) + "\n"

print(str_output)