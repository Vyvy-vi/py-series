def generate_ap(a, d, n):
    ls = [a]
    for _ in range(n - 1):
        a += d
        ls.append(a)
    return ls, sum(ls)


if __name__ == "__main__":
    a = int(input("Enter the first term: "))
    d = int(input("Enter the common difference: "))
    n = int(input("Enter the no. of terms you want to calulate the sum to: "))
    m, n = generate_ap(a, d, n)
    print(f"The series is given by:\n{m}...\nThe sum of the AP is:\n{n}")
