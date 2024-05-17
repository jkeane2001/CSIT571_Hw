#Jack Keane
#Professor Zhang
#CST571_01 Computer Algorithms and Analysis
#PG4 Quick Sort: This program uses the last element as the pivot
#3 March 2023
def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr)-1

    if left < right:
        i = partition(arr, left, right)
        leftComp = quicksort(arr, left, i-1)
        rightComp = quicksort(arr, i+1, right)
        totalComp = leftComp + rightComp + (right - left)
        return totalComp
    else:
        return 0

def partition(arr, left, right):

    pivot = arr[right]

    i = left

    for j in range(left, right):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[right], arr[i] = arr[i], arr[right]
    return i



#array = [3, 2 , 1, 5, 4]
#comps = quicksort(array,0, len(array)-1)

#print(array)
#print(comps)

print("Number of comparisons from the file:")
with open('data.txt', 'r') as f:
    dataArray = [int(nums) for nums in f]

comps = quicksort(dataArray, 0, len(dataArray)-1)
print(comps)

# Number of comparisons seems to be about 160361