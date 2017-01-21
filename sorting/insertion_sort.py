def insertion_sort(a):

    for i in range(1, len(a)):

        val = a[i]

        j = i - 1

        while j >= 0 and a[j] > val:
            a[j + 1] = a[j]
            j = j - 1

        a[j + 1] = val


if __name__ == "__main__":

    list = [7, 1, 44, 8, 10]
    insertion_sort(list)
    print(list)
