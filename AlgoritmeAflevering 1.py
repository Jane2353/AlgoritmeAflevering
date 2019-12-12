
def bubble_sort(A):
    swapped = True
    n = len(A)
    while swapped == True:
        swapped = False
        for i in range (1, n):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True
    return A

A = [3, 8, 4, 1, 2, 7, 5, 6]
print (bubble_sort(A))

print(talliste)
print(insertion_sort(talliste))

start = time.time()
my_list = random.sample(range(3000000), 3000000)
slut = time.time()

print (slut - start)
print (my_list)
