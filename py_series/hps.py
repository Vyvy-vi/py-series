def generate_hp(a, d, n):
    ls = [a]
    for _ in range(n - 1):
        a += d
        ls.append(a)
    return [f"1 / {i}" for i in ls], sum([1 / i for i in ls])


if __name__ == "__main__":
    a = int(input("Enter the first term: "))
    d = int(input("Enter the common difference: "))
    n = int(input("Enter the no. of terms you want to calulate the sum to: "))
    m, n = generate_hp(a, d, n)
    print(f"The series is given by:\n{m}...\nThe sum of the HP is:\n{n}")
