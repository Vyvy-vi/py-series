from aps import generate_ap
from gps import generate_gp
from fib import generate_fib
from kthpow import generate_kth_pow


def ui():
    ls = inp_ls()
    if fibonacci(ls):
        print_series(ls, 0)
    elif ap(ls):
        print_series(ls, 1)
    elif gp(ls):
        print_series(ls, 2)
    elif nth_power_check(2, ls):
        print_series(ls, 3)
    elif nth_power_check(3, ls):
        print_series(ls, 4)
    elif nth_power_check(4, ls):
        print_series(ls, 5)
    elif nth_power_check(5, ls):
        print_series(ls, 6)
    else:
        print(
            "The entered sequence might not be a series,\n\
OR maybe you should consider going to wolfram :wink:"
        )


def inp_ls():
    inp = input(print("Enter the terms of the series (comma-separated): "))
    return list(map(int, inp.split(" ")))


def fibonacci(ls):
    for i in range(len(ls) - 2):
        j = i + 1
        k = i + 2
        if ls[k] != ls[i] + ls[j]:
            return False
        else:
            continue
    return True


def ap(ls):
    for i in range(len(ls) - 2):
        if ls[i + 1] - ls[i] != ls[i + 2] - ls[i + 1]:
            return False
    return True


def gp(ls):
    for i in range(len(ls) - 2):
        if ls[i + 1] / ls[i] != ls[i + 2] / ls[i + 1]:
            return False
    return True


def nth_power_check(n, ls):
    for i in range(len(ls) - 1):
        if (ls[i] ** (1 / n)) + 1 != ls[i + 1] ** (1 / n):
            return False
    return True


def print_series(ls, t):
    series_types = [
        "Fibbonaci",
        "AP",
        "GP",
        "Squares",
        "Cubes",
        "N to 4th power",
        "N to 5th power",
    ]
    series_type = series_types[t]

    print(f'The type of this series is: "{series_type}"')
    n = int(input("Enter no. of terms in series that you want to print: "))
    if t == 0:
        m, n = generate_fib(n)
    elif t == 1:
        m, n = generate_ap(ls[0], ls[1] - ls[0], n)
    elif t == 2:
        m, n = generate_gp(ls[0], ls[1] // ls[0], n)
    elif t < 7:
        m, n = generate_kth_pow(ls[0], t - 1, n)
    print(f'The series is given by:\n{m}...\nThe sum of the "{series_type}" is:\n{n}')


ui()
