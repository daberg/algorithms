def selection_sort(a):

    for i in range(0, len(a)):

        min_val = a[i]
        min_index = i

        for j in range(i + 1, len(a)):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j

        tmp = a[i]
        a[i] = min_val
        a[min_index] = tmp


if __name__ == "__main__":

    list = [21, 62, 34, 6, 59]
    selection_sort(list)
    print(list)
