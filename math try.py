

sum = 0
counter = 0
#lists for saving ascending numbers
list_a=[0]
list_af=[]
#lists for saving descending numbers
list_d=[0]
list_df=[0]
#list wich will contain index of median number
list_of_index=[]
#list of median number or numbers
list_of_median=[]

# function quicksort was taken from https://realpython.com/sorting-algorithms-python/
from random import randint
def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

#open file with numbers
with open ("C:\/Users\соня\Downloads\/10m.txt\/10m.txt", "r") as file:
    # create list with numbers and measure its length
    file = file.read().split('\n')[:-1]
    len_of_file = len(file)
    # depends on amount of numbers in a list, it choose differ strategy to calculate median
    if len_of_file%2==0:
        list_of_index.append(len_of_file//2)
        list_of_index.append(len_of_file//2-1)
    else:
        list_of_index.append((len_of_file-1)//2)
    # moving through lists to find the longest ASC and DESC chain of number and in the same time changing type of data in list
    for i in range (len(file)):
        file[i] = int(file[i])
        num = int(file[i])
        sum+=num
        if num>list_a[-1]:
            list_a.append(num)
        else:
            if len(list_a)>len(list_af):
                list_af = list_a[:]
            list_a = [num]
        if num<list_d[-1]:
            list_d.append(num)
        else:
            if len(list_d)>len(list_df):
                list_df = list_d[:]
            list_d = [num]
        counter+=1
    # sort our list
    new_files = quicksort(file)
# finalize DESC AND ASC lists
if len(list_a) > len(list_af):
    list_af = list_a[:]
if len(list_d) > len(list_df):
    list_df = list_d[:]
print("ASC: ", list_af)
print("DSC: ", list_df)
print("mean: ", sum/counter)
print("max: ", new_files[-1])
print("min: ", new_files[0])
# find numbers for median and make calculation if it's needed
for elem in list_of_index:
    list_of_median.append(new_files[elem])
if len(list_of_median)>1:
    list_of_median = (list_of_median[0]+list_of_median[1])/2
print("median: ", list_of_median)
