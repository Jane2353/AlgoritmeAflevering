# Python program to find the largest number in the list

# The list is empty in the beginning
list = []

# It asks how many many numbers you want in the list
number = int(input("Hvor mange tal vil du have i din liste? "))
# It will keep asking until you have the amount of numbers you want,
# then it will sort them to see which is the largest
for i in range(1, number + 1):
    tal = int(input("Indsæt tal: "))
    list.append(tal)

# It tells which is the largest number
# from the list by looking at the append list
print("Det højeste tal er:", max (list))
