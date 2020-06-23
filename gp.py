a = int(input('Enter the first term: '))
r = int(input('Enter the common ratio: '))
n = int(input('Enter the no. of terms you want to calulate the sum to: '))
def gp(a, r, n):
    ls = [a]
    for i in range(n-1):
        a *= r
        ls.append(a)
    return ls,sum(ls)
m, n = gp(a, r, n)
print(f'The series is given by:\n{m}...\nThe sum of the GP is:\n{n}')
