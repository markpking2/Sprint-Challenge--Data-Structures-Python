import time
from binary_search_tree import BinarySearchTree

# runtime of reading files/storing names: O(n)
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

starter_duplicates = []  # Return the list of duplicates in this data structure

start_time = time.time()

# starter code runtime: O(n ^ 2)
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            starter_duplicates.append(name_1)

end_time = time.time()
print(f"{len(starter_duplicates)} duplicates:\n\n{', '.join(starter_duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# optimized list solution compared to original: O(n^2) but the outer loop continues if a name is found,
# instead of always looping n times in inner loop as it did in the starter solution

start_time = time.time()
limited_duplicates = [name for name in names_1 if name in names_2]

end_time = time.time()
print(f"{len(limited_duplicates)} duplicates:\n\n{', '.join(limited_duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# runtime using binary search tree: O(n log(n))

start_time = time.time()
names_1_bst = BinarySearchTree(names_1[0])
for name in names_1:
    names_1_bst.insert(name)

duplicates = [name for name in names_2 if names_1_bst.contains(name)]

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# runtime using hash table: O(n)

start_time = time.time()

stretch_duplicates = []
dictionary = {}


for name in names_1:
    dictionary[name] = name

stretch_duplicates = [name for name in names_2 if name in dictionary]
end_time = time.time()

print(f"{len(stretch_duplicates)} duplicates:\n\n{', '.join(stretch_duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
