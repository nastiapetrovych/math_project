import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



def finding_value():
    """
    Returns the value in an exact point
    :param x: int
    :param length: int
    :return: float
    """
    print(f'Hi, the function is (1 - (2 * x) + 4 * (x ** 2))) ** 0.5')
    params = input('Enter the meaning of "x":')
    length_input = input('Enter the length of row:')
    x = int(params)
    length = int(length_input)
    my_func = (1 - (2 * x) + 4 * (x ** 2)) ** 0.5
    text_input = input("Enter 'yes' if you want to see the row:")
    alfa = 0.5
    result = 1
    lst = [alfa]
    value = alfa * (4 * (x ** 2) - 2 * x)
    extra_value = 4 * (x ** 2) - 2 * x
    result += value
    if length == 0:
        line = '1'
    elif length == 1:
        line = '1 + x'
    else:
        line = '1 + x + '
    for element in range(2, length + 1):
        item = (lst[-1] * (alfa - (element - 1)))
        if element != length:
            line += f'{item/math.factorial(element)} * x ** {element} + '
        else:
            line += f'{item/math.factorial(element)} * x ** {element}'
        value1 = item * extra_value ** element
        lst.append(item)
        result += value1
    if text_input == 'yes':
        print(line)
    result = eval(str(line))
    return result


def creation_of_table():
    first_point = finding_value()
    fig, ax = plt.subplots()
    second_point = finding_value()
    xpoints = np.array([first_point, second_point])
    first_point_1 = 2
    second_point_1 = 20
    x = first_point_1
    my_func1 = (1 - (2 * x) + 4 * (x ** 2)) ** 0.5
    x = second_point_1
    my_func2 = (1 - (2 * x) + 4 * (x ** 2)) ** 0.5
    ypoints = np.array([my_func1, my_func2])
    ax.set(title=f'The difference between my function and module math',\
           xlabel=f'the value of x', ylabel=f'the value of function')

    plt.plot(xpoints, ypoints)
    plt.show()

print(creation_of_table())