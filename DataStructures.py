# This is the HashTable class using chaining
class HashTable:
    # time complexity -> O(1)
    def __init__(self, initial_capacity=40):
        # initialize hash table with empty list entries
        # assign each index with an empty list
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # time complexity -> O(N)
    # insert a new item into hash table
    def insert(self, key, item):
        # get bucket list where item will go
        bucket = hash(key) % len(self.table)  # index that item will be placed in
        bucket_list = self.table[bucket]
        key_value = [key, item]  # construct a list from the key and value

        # update if it already exists
        for kv in bucket_list:
            if kv[0] == key:  # if the key already exists
                kv[1] = item  # update the item
                return True
        # insert new item
        bucket_list.append(key_value)  # else append the key/value pair to the list
        return True

    # time complexity -> O(N)
    # search the hash table using key
    def search(self, key):
        # get bucket list where item would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key
        for key_value in bucket_list:
            if key_value[0] == key:  # if key exists
                return key_value[1]  # return the value
        return None  # else return None

    # time complexity -> O(N)
    # remove an item from hash table using key
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if found
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])
