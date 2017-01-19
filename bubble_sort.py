def bubble_sort(a):

    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]


def better_bubble_sort(a):

    for i in range(len(a), 0, -1):

        has_swapped = False

        for j in range(1, i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                has_swapped = True

        # If no swaps are performed the array is already sorted
        if not has_swapped:
            break


if __name__ == "__main__":
    list = [7, 1, 44, 8, 10]
    bubble_sort(list)
    print(list)
    list = [1, 1, 4, 8, 10]
    better_bubble_sort(list)
    print(list)
