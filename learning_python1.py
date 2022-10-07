
def exponent_function (base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result


print(exponent_function(9, 4))

data_lists = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11],
    [12, 13, 14]
]
print(data_lists[1][1])

for row1 in data_lists:
    for col1 in row1:
        print(col1)
