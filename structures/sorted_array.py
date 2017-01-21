# Sorted dynamic array implementation.
# Cannot hold duplicate elements.

"""
Examples

0 1 2 3  4  5  6
3 6 7 10 11 12 14

0 1 2 3  4  5
3 6 7 10 11 12
"""


class SortedArray:

    def __init__(self):

        self.list = []

    def insert(self, new):

        count = len(self.list)

        if count == 0:
            self.list.append(new)
            return 0

        else:
            return self._rec_insert(new, 0, count-1)

    def _rec_insert(self, new, start, end):

        if start > end:

            self.list.insert(start, new)
            return start

        mid = (start + end) // 2

        mid_val = self.list[mid]

        if mid_val == new:
            return None

        elif mid_val < new:
            return self._rec_insert(new, mid + 1, end)

        elif mid_val > new:
            return self._rec_insert(new, start, mid - 1)

    def python_list(self):

        return self.list

    def search(self, element):

        return self._rec_search(element, 0, len(self.list)-1)

    def _rec_search(self, element, start, end):

        if start > end:
            return None

        mid = (end + start) // 2

        if self.list[mid] == element:
            return mid

        elif self.list[mid] < element:
            return self._rec_search(element, mid + 1, end)

        elif self.list[mid] > element:
            return self._rec_search(element, start, mid - 1)


if __name__ == "__main__":
    array = SortedArray()
    print(array.insert(4))
    print(array.insert(10))
    print(array.insert(2))
    print(array.insert(1))
    print(array.insert(6))
    print(array.insert(149))
    print(array.insert(4))
    print(array.python_list())
