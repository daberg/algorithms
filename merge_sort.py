def merge_sort(a):
    _merge_sort(a, 0, len(a) - 1)


def _merge_sort(a, start, end):

    if start < end:

        mid = (start + end) // 2

        _merge_sort(a, start, mid)
        _merge_sort(a, mid + 1, end)
        _merge(a, start, mid, end)


def _merge(a, start, mid, end):

    b = [0] * len(a)

    k = start
    i = start
    j = mid + 1

    while i <= mid and j <= end:

        if a[i] < a[j]:
            b[k] = a[i]
            i = i + 1
            k = k + 1

        else:
            b[k] = a[j]
            j = j + 1
            k = k + 1

    while i <= mid:
        b[k] = a[i]
        i = i + 1
        k = k + 1

    while j <= end:
        b[k] = a[j]
        j = j + 1
        k = k + 1

    for i in range(start, k):
        a[i] = b[i]


if __name__ == "__main__":
    list = [7, 1, 44, 8, 10]
    merge_sort(list)
    print(list)
    list = [1, 1, 4, 8, 10]
    merge_sort(list)
    print(list)
