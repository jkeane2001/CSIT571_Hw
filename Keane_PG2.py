#Jack Keane
#Professor Zhang
#CST571_01 Computer Algortithms and Analysis
#PG3 Quick Sort Algorithm
#3 February 2023
count = 0

def mergeSort(array):

    if len(array) > 1:

        global count

        left = array[:len(array) // 2]
        right = array[len(array) // 2:]
        #count = 0
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                count += (len(left) - 1)
                j+=1
            k+=1

        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1


    return count

#arr = [6, 4, 10, 3, 15, 1]
#print(arr)
#print(mergeSort(arr))

#arr2= [15, 10, 6, 4, 3, 1]
#print(arr2)
#print(mergeSort(arr2))

print("The number of inversions from the file: ")
with open('Input.txt', 'r') as f:
    print(mergeSort([int(num) for num in f]))

#The number of inversions in the output is about: 4998442960