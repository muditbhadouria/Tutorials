my_list1 = ["banana", "apple"]
# print(my_list1)

my_list2 = list()
# print(my_list2)

my_list2.append("banana")
my_list2.append("cherry")
my_list2.append("apple")

# Access items in list
# print(my_list2[1])
# print(my_list2[-1])

# Iterate over a list
# for item in my_list2:
#     print(item)

# Check if item is present in a list
if "banana" in my_list2:
    print("present")
else:
    print("absent")

# Append, insert, pop, remove
my_list2.append("lemon")
# print(my_list2)
my_list2.insert(1, "orange")
# print(my_list2)
# my_list2.pop()
# print(my_list2)
# my_list2.remove("orange")
# print(my_list2)

# Clear a list
# my_list2.clear()
# print(my_list2)

# Sort a list (Sorts in place)
# my_list2.sort()
# print(my_list2)

# Sort a list and create a new list
sorted_list = sorted(my_list2)
print(sorted_list)

sorted_list.reverse()
print(sorted_list)

zeroes = [0] * 5
new_zeroes = zeroes.copy()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
zeroes.extend(nums)
# print(zeroes)
all_nums = new_zeroes + nums
# print(all_nums)
sliced = all_nums[::-2]
# print(sliced)

sqaured = [i*i for i in nums]
print(sqaured)
