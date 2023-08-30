import random

def randomize_in_place(A):
    n = len(A)
    for i in range(n):
        # Get random index between i and n
        random_index = random.randint(i, n-1)

        # Print the program state state before swapping
        print('Before Swap:')
        print('   {A}')
        print('   i = {i+1}')
        print('   Random({i+1}, {n+1}) = {random_index + 1}')
        print("")

        # Swap the number at index i and the number at the random index
        A[i], A[random_index] = A[random_index], A[i]

        # Print the program state after swapping
        print('After Swap:')
        print('   {A}')
        print('   i = {i + 1}')
        print('-' * 35) 
    return A

sample_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_array = randomize_in_place(sample_array)
print('Final Array:')
print('   {random_array}')


