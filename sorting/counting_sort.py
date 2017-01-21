def counting_sort(a, k):

    aux = [0] * (k + 1)    # +1 because it also accepts 0
    out = [None] * len(a)

    for val in a:
        aux[val] = aux[val] + 1

    for i in range(1, k + 1):
        aux[i] = aux[i] + aux[i - 1]

    for j in range(len(a)):
        out[aux[a[j]] - 1] = a[j]
        aux[a[j]] = aux[a[j]] - 1

    for i in range(len(a)):
        a[i] = out[i]


if __name__ == "__main__":
    list = [7, 1, 44, 8, 10]
    counting_sort(list, 44)
    print(list)
    list = [1, 1, 4, 8, 10]
    counting_sort(list, 44)
    print(list)
