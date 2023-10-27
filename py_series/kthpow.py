def generate_kth_pow(a, k, n):
    ls = [(a + i) ** k for i in range(n)]
    return ls, sum(ls)


if __name__ == "__main__":
    a = int(input("Enter the first term: "))
    k = int(input("Enter the k: "))
    n = int(input("Enter the no. of terms you want to calulate the sum to: "))
    m, n = generate_kth_pow(a, k, n)
    print(f"The series is given by:\n{m}...\nThe sum of the {k}th power is is:\n{n}")
