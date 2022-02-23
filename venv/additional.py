import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def finding_value(x, length):
    """
    Returns the value in an exact point
    :param x: float
    :param length: int
    :return: float
    """
    my_func = (1 + 4 * (x ** 2) - 2 * x) ** 0.5
    alfa = 0.5
    lst = [alfa]
    x_arc = 4 * (x ** 2) - 2 * x
    if length == 0:
        line = '1'
    elif length == 1:
        line = f'1 + {alfa * x_arc}'
    else:
        line = f'1 + {alfa * x_arc} + '
    for element in range(2, length + 1):
        item = (lst[-1] * (alfa - (element + 1)))
        if element != length:
            line += f'({item} / {math.factorial(element)}) * ({x_arc} ** {element}) + '
        else:
            line += f'({item} / {math.factorial(element)}) *  ({x_arc} ** {element})'
        lst.append(item)
    result = eval(str(line))
    return [line, result, length, my_func]


def creation_of_table(x, length):
    lst1 = np.arange(-0.3, 0.8, step=0.01)
    fig, ax = plt.subplots()
    ax.set(title=f'The difference between my function and module math',\
           xlabel=f'the value of x', ylabel=f'the value of function')
    first_lst = []
    second_lst = []
    for y in lst1:
        result = finding_value(y, length)
        first_lst.append(result[-1])
        second_lst.append(result[1])
    plt.plot(lst1, first_lst,'r-', lst1, second_lst, 'b-')
    plt.xlim(-0.6, 1)
    plt.ylim(-1, 1.5)
    plt.savefig("mygraph.png")


def user_input():
    print(f'Hi, the function is (1 - (2 * x) + 4 * (x ** 2))) ** 0.5')
    params = input('Enter the meaning of "x":')
    length_input = input('Enter the length of row:')
    x = float(params)
    length = int(length_input)
    text_input = input("Enter 'yes' if you want to see the row:")
    line = finding_value(x, length)
    if text_input == 'yes':
        text = line[0]
        text1 = line[-1]
        print(text)
        print(text1)
    else:
        text1 = line[1]
        print(text1)
    creation_of_table(x, length)
    return 'Well done'

print(user_input())