def quick_sort(a):
    _hoare_quick_sort(a, 0, len(a) - 1)


def _hoare_quick_sort(a, start, end):

    if start < end:

        j = hoare_partition(a, start, end)
        _hoare_quick_sort(a, start, j)
        _hoare_quick_sort(a, j + 1, end)


def _lomuto_quick_sort(a, start, end):

    if start < end:

        j = lomuto_partition(a, start, end)
        _lomuto_quick_sort(a, start, j - 1)
        _lomuto_quick_sort(a, j + 1, end)


def hoare_partition(a, start, end):

    pivot = a[start]

    i = start - 1
    j = end + 1

    while True:

        # The absence of a do-while block in python makes this not very
        # eye-pleasing. One could at least get rid of the infamous break
        # statements by using condition flags.

        while True:
            i = i + 1
            if a[i] >= pivot:
                break

        while True:
            j = j - 1
            if a[j] <= pivot:
                break

        if i < j:
            a[i], a[j] = a[j], a[i]

        else:
            return j


# This is actually simpler to implement but it performs worse than Hoare's
# partitioning with respect to the number of swaps.
def lomuto_partition(a, start, end):

    pivot = a[end]

    i = start - 1

    for j in range(start, end):

        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]

    pivot_index = i + 1

    a[pivot_index], a[end] = a[end], a[pivot_index]

    return pivot_index


# This was called naive with respect to the fact that it checks an
# unnecessarily high number of conditions.
def naive_partition(a, start, end):

        i = start + 1
        j = end

        pivot = a[start]

        while i < j:

            while i <= j and a[i] <= pivot:
                i = i + 1

            while j >= i and a[j] > pivot:
                j = j - 1

            if i < j:
                a[i], a[j] = a[j], a[i]

        a[start], a[j] = a[j], a[start]

        # here j is the actual pivot, so this can be used like lomuto_partition
        return j


if __name__ == "__main__":
    list = [7, 1, 4]
    quick_sort(list)
    print(list)
    list = [7, 1, 44, 8, 10]
    quick_sort(list)
    print(list)
