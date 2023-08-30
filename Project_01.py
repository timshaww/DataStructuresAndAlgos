import random

def randomize_in_place(A):
    n = len(A)
    for i in range(n):
        # Get random index between i and n
        random_index = random.randint(i, n-1)

        # Print the program state state before swapping
        print('Before Swap:')
        print(f'   {A}')
        print(f'   i = {i+1}')
        print(f'   Random({i+1}, {n}) = {random_index + 1}')
        print("")

        # Swap the number at index i and the number at the random index
        A[i], A[random_index] = A[random_index], A[i]

        # Print the program state after swapping
        print('After Swap:')
        print(f'   {A}')
        print(f'   i = {i + 1}')
        print('-' * 35) 
    return A

sample_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_array = randomize_in_place(sample_array)
print('Final Array:')
print(f'   {random_array}')

''' 
I want to make print look like this:

Before Swap:
   Index = 1
   Random(1, 10) = 5
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ^-----------^
                

After Swap:
   [5, 2, 3, 4, 1, 6, 7, 8, 9, 10]
    ^-----------^

    Index = 2

'''