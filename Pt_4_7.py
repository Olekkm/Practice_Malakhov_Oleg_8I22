from itertools import permutations


def unique(_arr):
    arr = _arr[::1]
    for i in arr:
        while arr.count(i) > 1:
            arr.remove(i)
    return arr


arr = list(permutations(input("Введите значения списка ").split()))
for i in arr:
    print(i)
print("Всего перестановок {}\nУникальных перестановок {}".format(len(arr), len(unique(arr))))
