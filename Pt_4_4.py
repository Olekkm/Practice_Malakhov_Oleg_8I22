def unique(l, sum, K, local, A):
    if sum == K:
        print("{", end="")
        for i in range(len(local)):
            if i != 0:
                print(" ", end="")
            print(local[i], end="")
            if (i != len(local) - 1):
                print(", ", end="")
        print("}")
        return

    for i in range(l, len(A), 1):

        if (sum + A[i] > K):
            continue

        if (i > l and
                A[i] == A[i - 1]):
            continue

        local.append(A[i])

        # Recursive call
        unique(i + 1, sum + A[i],
               K, local, A)

        local.remove(local[len(local) - 1])


def Combination(A, K):
    A.sort()
    local = []
    unique(0, 0, K, local, A)


try:
    A = list(map(int, input("Введите список чисел ").split()))
    K = int(input("Введите искомое число "))
    Combination(A, K)
except ValueError:
    print("Ошибка ввода")
