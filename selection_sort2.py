import time
import random

# Traverse through all array elements
def selection_sort(list):
    n = len(list)

    for i in range(n):

        # Find the minimum element in remaining
        # unsorted array
        min = i
        for j in range(i+1, n):
            if list[min] > list[j]:
                min = j

        # Swap the found minimum element with
        # the first element
        list[i], list[min] = list[min], list[i]
    return list




A = random.sample(range(50000), 40000)
print(A)
start = time.time()
print(selection_sort(A))
slut = time.time()
print(slut-start)
