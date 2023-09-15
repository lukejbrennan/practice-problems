class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        # A simple hash function that takes the length of the key and returns a hash value
        return len(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return

# Example usage
hash_table = HashTable(10)
hash_table.insert("name", "John")
hash_table.insert("age", 30)
hash_table.insert("city", "New York")

print(hash_table.search("name"))  # Output: John
print(hash_table.search("age"))   # Output: 30
print(hash_table.search("city"))  # Output: New York

hash_table.delete("age")
print(hash_table.search("age"))   # Output: None
