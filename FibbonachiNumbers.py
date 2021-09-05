print("Fibbonachi Numbers".center(75, "="))


def fibonacci(n):
    if n < 1:
        return [n]

    SebelumN = fibonacci(n - 1)
    a1 = SebelumN[-2] if len(SebelumN) > 2 else 0
    a2 = SebelumN[-1] if len(SebelumN) > 2 else 1

    return SebelumN + [a1 + a2]


angka = int(input("Input Angka : "))

print(fibonacci(angka - 1))
