'''
Instructions:
Implement a double hashing algorithm. Make the table size 16. Set the first hash function as: 
𝐻1 = 𝑘𝑒𝑦 𝑚𝑜𝑑 16; and the second hash function as: 𝐻2 = 2 (𝑘𝑒𝑦 𝑚𝑜𝑑 4) + 1. Recall: In double hashing, 
the slot is determined by (𝐻1 + 𝑖 𝐻2) 𝑚𝑜𝑑 16, in which 𝐻1 is the first hash function and 𝐻2 is 
the second hash function. Here 𝑖 multiplies 𝐻2, and initially 𝑖 is set to 0; then if there is a 
collision we set 𝑖 to 1; then if there is still a collision we set 𝑖 to 2; and so on.

Run your algorithm on example keys that you insert into the hash table. Try to illustrate the collisions
and skips to new slots.

We ask you to print out the program state at each loop iteration (in this case, each insertion of a 
new key, and each collision that occurs). The program state in this case should be the key inserted, 
the array of numbers and the probe number “i”

'''
class DoubleHashing:
    def __init__(self):
        self.table_size = 16
        self.array = [None] * self.table_size

    def h1(self, key):
        return key % 16

    def h2(self, key):
        return 2 * (key % 4) + 1

    def insert(self, key):
        index = self.h1(key)
        if not self.array[index]:
            self.array[index] = key
            print(f"Inserting key {key} at index {index}.\nArray: {self.array}. \n\n")
            return
        
        i = 1
        while i < self.table_size:
            next_index = (index + i * self.h2(key)) % 16
            if not self.array[next_index]:
                self.array[next_index] = key
                print(f"Inserting key {key} at index {next_index}.")
                print(f"There were collisions!!! Total number of collisions: {i}\nArray: {self.array}.\n\n")
                return
            i += 1

hash_table = DoubleHashing()
keys = [10, 26, 18, 34, 22, 14, 42, 50, 27, 13, 9, 21, 6, 19, 48, 31]
print(f"\nKeys: {keys}\n\n")
for key in keys:
    hash_table.insert(key)