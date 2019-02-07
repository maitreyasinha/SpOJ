num_input = int(input())
output_str = ""

def getNumZeros(inp):
    num_factors = int(inp/5)
    if num_factors == 0:
        return 0
    return num_factors + getNumZeros(num_factors)


for i in range(num_input):
    inp = input()
    output_str = output_str + str(getNumZeros(int(inp))) + "\n"

print(output_str)