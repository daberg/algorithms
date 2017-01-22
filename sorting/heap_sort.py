def get_left(i):
    return (i << 1) + 1


def get_right(i):
    return (i << 1) + 2


def parent(i):
    return (i - 1) >> 1


def maxheapify(a, i, length):

    while i < length:

        left = get_left(i)
        right = left + 1

        max_index = i

        if left < length and a[left] > a[i]:
            max_index = left

        if right < length and a[right] > a[max_index]:
            max_index = right 

        if max_index == i:
            return

        a[i], a[max_index] = a[max_index], a[i]
        i = max_index


def rec_maxheapify(a, i, length):
    
    left = get_left(i)
    right = left + 1

    max_index = i

    if left < length and a[left] > a[i]:
        max_index = left

    if right < length and a[right] > a[max_index]:
        max_index = right 

    if max_index != i:
        a[i], a[max_index] = a[max_index], a[i]
        maxheapify(a, max_index, length)


def build_maxheap(a):

    # Loop from midpoint to the 0th element.
    for i in range(len(a) // 2 - 1, -1, -1):
        maxheapify(a, i, len(a))


def heap_sort(a):

    build_maxheap(a)

    heapsize = len(a)

    # Stop calling maxheapify when the cycle has reached the 0th element,
    # which, as the last remaining item, is the minimum and therefore is
    # already in the right position.
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapsize = heapsize - 1
        maxheapify(a, 0, heapsize)

if __name__ == "__main__":
    list = [7, 1, 44, 8, 10]
    heap_sort(list)
    print(list)
    list = [1, 1, 4, 8, 10]
    heap_sort(list)
    print(list)
