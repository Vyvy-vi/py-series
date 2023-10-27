def generate_fib(n):
    ls = [None] * n
    ls[0] = 1
    ls[1] = 1
    for i in range(2, n):
        ls[i] = ls[i - 1] + ls[i - 2]

    return ls, sum(ls)


if __name__ == "__main__":
    n = int(input("Enter the no. of terms you want to calulate the sum of fibonacci sequence to: "))
    m, n = generate_fib(n)
    print(f"The series is given by:\n{m}...\nThe sum of the sequence is:\n{n}")
