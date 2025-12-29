class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i in range(0, len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    self.table[key_hash].pop(i)
                    return True
        return False

    def __str__(self):
        result = ""
        for i, item in enumerate(self.table):
            if item is not None:
                result += f"{i}: {str(item)}\n"
        return result


if __name__ == "__main__":
    try:
        H = HashTable(5)
        H.insert("apple", 10)
        H.insert("orange", 20)
        H.insert("banana", 30)

        assert H.get("apple") == 10
        assert H.get("orange") == 20
        assert H.get("banana") == 30

        assert H.delete("orange") is True
        assert H.get("orange") is None
        assert H.delete("grape") is False

    except AssertionError:
        print("Assertation failed!")
    else:
        print("All tests passed successfully!")
