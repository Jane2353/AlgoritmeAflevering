import random
import time

# The time starts.
start = time.time()
# The list has 50.000 numbers to choose from, and we want to see x numbers.
my_list = random.sample(range(50000), 40000)

# The list is being sorted
my_list.sort()

# The time ends
slut = time.time()

# The list and time is shown after being sorted
print(my_list)
print (slut - start)

