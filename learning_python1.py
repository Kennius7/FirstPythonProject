
def exponent_function (base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result


print(exponent_function(9, 4))