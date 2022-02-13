class HashTable:
    def __init__(self):
        self.hash_table = [[] for _ in range(10)]

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hash_table)
        bucket = self.hash_table[hash_key]
        key_exists = False
        for i, key_value in enumerate(bucket):
            k, v = key_value
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = hash(key) % len(self.hash_table)
        bucket = self.hash_table[hash_key]
        for key_value in bucket:
            k, v = key_value
            if k == key:
                return v

    def delete(self, key):
        hash_key = hash(key) % len(self.hash_table)
        bucket = self.hash_table[hash_key]
        key_exists = False
        for i, key_value in enumerate(bucket):
            k, v = key_value
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))

    def print_table(self):
        print(self.hash_table)

    def get_table(self):
        return self.hash_table


if __name__ == '__main__':
    hash_table = HashTable()
    print("You have created an empty hash table!")
    hash_table.print_table()

    print("\nYou have added some elements to your table!")
    hash_table.insert(0, "John")
    hash_table.insert(1, "Tom")
    hash_table.insert(2, "Elon")
    hash_table.insert(10, "Mark")
    hash_table.print_table()

    print("\nLet's get some values by the key!")
    print(hash_table.search(0))
    print(hash_table.search(1))
    print(hash_table.search(2))
    print(hash_table.search(10))

    print("\nLet's delete elements with keys 2 and 10")
    hash_table.delete(2)
    hash_table.delete(10)
    hash_table.print_table()


