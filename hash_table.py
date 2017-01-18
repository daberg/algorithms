class ChainNode:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class ChainingTableEntry:

    def __init__(self):
        self.head = None

    def __iter__(self):

        curr = self.head

        while curr:
            yield (curr.key, curr.data)
            curr = curr.next

    # TODO: make the list sorted to improve complexity in the average case
    def add(self, key, data):

        if self.head is None:
            self.head = ChainNode(key, data)
            return key

        curr = self.head

        while curr.key != key and curr.next is not None:
            curr = curr.next

        if curr.key == key:
            curr.data = data
            return key

        curr.next = ChainNode(key, data)

    def remove(self, key):
        
        if self.head is None:
            return None

        prev = None
        curr = self.head

        while curr is not None:

            if curr.key == key:

                if prev is not None:
                    prev.next = curr.next
                    return curr.data

            prev = curr
            curr = curr.next

        return None

    def print_entry(self):

        for couple in self:
            print("[" + str(couple[0]) + ":" + str(couple[1]) + ']', end='')

        print()

    def is_empty(self):
        return (self.head is None)


class ChainingHashTable:

    def __init__(self):

        self.index_size = 10
        self.table_size = 2**self.index_size
        self.max_index = self.table_size - 1

        self.entries = []
        for i in range(0, self.table_size):
            self.entries.append(ChainingTableEntry())

    def naive_hash(self, key):
        return key % self.table_size

    # Hashing function based upon multiplication of the key with a constant.
    # The fractionary part of the said product is multiplied to the table size
    # to get a suitable index.
    # The actual implementation makes use of integer representation in order to
    # achieve better performance.
    def hash(self, key):

        assert(key >= 0)

        # The constant suggested by Donald Knuth multiplied by 2^32 to work
        # with a 32-bit integer representation.
        # Note that, of course, multiplying by a power of two in binary
        # representation is just like multiplying by a power of ten in decimal.
        knuth = 2654435769    # floor( ((√5−1)÷2) x (2^32) )

        product = key * knuth

        # Take index_size number of bits from the last 32 bits of the product.
        # Those bits constitute the integer representation of the aproximated
        # fractionary part of the product between Knuth constant and the key.
        # Note that the hash is obtained just by using standard arithmetic
        # operations.
        return (product >> (32 - self.index_size)) & (self.max_index)

    def add(self, key, data):

        key_hash = self.hash(key)

        self.entries[key_hash].add(key, data)

    def remove(self, key):

        key_hash = self.hash(key)

        self.entries[key_hash].remove(key)

    def print_table(self):

        i = 0

        for entry in self.entries:

            if not entry.is_empty():
                print(str(i) + '-->', end='')
                entry.print_entry()

            i = i + 1


htable = ChainingHashTable()
htable.add(10, "asd")
htable.add(2918, "lulz")
htable.add(2918, "test")
htable.add(110, 239)
htable.add(10, "xd")
htable.add(9, 5012)
htable.add(36, "lmao")
htable.add(2918, "test2")
htable.remove(10)
htable.remove(0)
htable.remove(119)
htable.print_table()
