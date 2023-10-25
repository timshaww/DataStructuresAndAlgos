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