import math
def finding_value(length, x):
    result = 1
    function = (1 + 4 * x ** 2 - 2 * x) ** 0.5
    alfa = 0.5
    lst = []
    coeficient = alfa
    lst.append(coeficient)
    result += coeficient * (4 * x ** 2 - 2 * x)
    for element in range(1, length):
        coeficient1 = lst[-1] * (alfa - element) / (element + 1)
        print(coeficient1)
        lst.append(coeficient1)
        value = coeficient1 * (4 * x ** 2 - 2 * x) ** (element + 1)
        result += value
    return result

print(finding_value(50, 1))
print(math.sqrt(3))
