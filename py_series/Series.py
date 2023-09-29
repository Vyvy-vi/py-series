from aps import generate_ap
from gps import generate_gp
def ui():
    ls = inp_ls()
    if fibonacci(ls):
        print_series(ls, 0)
    elif ap(ls):
        print_series(ls, 1)
    elif gp(ls):
        print_series(ls, 2)
    elif nth_power_sum_check(2, ls):
        print_series(ls, 3)
    elif nth_power_sum_check(3, ls):
        print_series(ls, 4)
    elif nth_power_sum_check(4, ls):
        print_series(ls, 5)
    elif nth_power_sum_check(5, ls):
        print_series(ls, 6)
    else:
        print('The entered sequence might not be a series,\n\
OR maybe you should consider going to wolfram :wink:')

def inp_ls():
    ls=[]
    print("You'll be prompted to enter the terms in the series.")
    print('Press Q or some alphabets to quit.')
    while True:
        inp= input('Enter term of series: ')
        if inp.isdigit():
            ls.append(int(inp))
        else:
            break
    return ls

def fibonacci(ls):
    #ls=[1,1,2,3,5,8,13,21]
    for i in range(len(ls)-2):
        j = i+1
        k=i+2
        if (ls[k]!=ls[i]+ls[j]):
            return False
        else:
            continue
    return True

def ap(ls):
    #ls=[1,2,3,4,5]
    for i in range(len(ls)-2):
        if ls[i+1]-ls[i]== ls[i+2]-ls[i+1]:
            continue
        else:
            return False
    return True

def gp(ls):
    #ls=[3,9,27,81,243,729]
    for i in range(len(ls)-2):
        if (ls[i+1]/ls[i]==ls[i+2]/ls[i+1]):
            continue
        else:
            return False
    return True

def nth_power_sum_check(n, ls):
    for i in range(len(ls) - 1):
        if (ls[i] ** (1/n)) + 1 != ls[i+1] ** (1/n):
            return False
    return True

def print_series(ls, t):
    type= ["Fibbonaci","AP","GP","Sum of square","Sum of Cubes","Sum of N to 4th power","Sum of N to 5th power"]
    type=type[t]
    print(f'The type of this series is: "{type}"')
    n = int(input('Enter no.of terms in series that you want to print: '))
    if t==0:
        m,n= None,None
    elif t==1:
        m,n= generate_ap(ls[0],ls[1]-ls[0],n)
    elif t==2:
        m,n= generate_gp(ls[0],ls[1]//ls[0],n)
    else:
        m,n= None,None
    print(f'The series is given by:\n{m}...\nThe sum of the "{type}" is:\n{n}')

ui()