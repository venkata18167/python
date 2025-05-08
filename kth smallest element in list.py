def kth_smallest_element(lst, k):
    lst.sort()
    return lst[k - 1]

my_list = [7, 10, 4, 3, 20, 15]
k = 3
result = kth_smallest_element(my_list, k)
print(f"The {k}th smallest element in the list is: {result}")
