import time
import random
import tracemalloc
import matplotlib.pyplot as pl

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end =" ")
    print()

def Bubble_sort(l):
    for i in range(1,len(l)):
        for j in range(0,len(l)-i):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

def Selection_sort(l):
    for i in range(0,len(l)):
        min = i
        for j in range(i+1,len(l)):
            if l[min]>l[j]:
                min = j
        l[min],l[i] = l[i],l[min]
    return l

def Insertion_sort(l):
    for i in range(1,len(l)): # outer loop for unsorted sub-list
        temp = l[i]
        for j in range(i-1,-1,-1): # Inner loop for sorted sub-list
            if l[j] > temp:
                l[j+1],l[j] = l[j],l[j+1]
    return l

def Merge_sort_Recursion(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        Merge_sort_Recursion(L)
        Merge_sort_Recursion(R)

        i,j,k = 0,0,0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def merge_iterative(A, temp, frm, mid, to): 
    k = frm
    i = frm
    j = mid + 1
    while i <= mid and j <= to:
        if A[i] < A[j]:
            temp[k] = A[i]
            i = i + 1
        else:
            temp[k] = A[j]
            j = j + 1
        k = k + 1
 
    while i < len(A) and i <= mid:
        temp[k] = A[i]
        k = k + 1
        i = i + 1
 
    for i in range(frm, to + 1):
        A[i] = temp[i]
 
def Merge_sort_iterative(A):
    low = 0
    high = len(A) - 1
    temp = A.copy()
    m = 1
    while m <= high - low:
        for i in range(low, high, 2*m):
            frm = i
            mid = i + m - 1
            to = min(i + 2*m - 1, high)
            merge_iterative(A, temp, frm, mid, to)
        m = 2*m

def partition_recursion(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot: skaow
    for j in range(low, high):
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def Quick_sort_Recursion(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition_recursion(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        Quick_sort_Recursion(arr, low, pi-1)
        Quick_sort_Recursion(arr, pi+1, high)

def partition_iterative(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
    for j in range(l , h):
        if arr[j] <= x:
            # increment
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

def Quick_sort_iterative(arr,l,h):
    # Creating a stack
    size = h - l + 1
    stack = [0] * (size)
    # initialization
    top = -1
    # push initial values
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    # pop from stack
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        # Set pivot element at its correct position
        p = partition_iterative(arr, l, h)
        # elements on the left
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        # elements on the right
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


"""
here you have to put the time in sec, which you will get after running this code,
like this [2.0123, 3.221, 4.554, 8.222]
"""
# inputs = [10,100,1000,10000,100000]
# Bubble_s = []
# Selection_s = []
# Insertion_s = []
# Merge_s_recursive = []
# Merge_s_iterative = []
# Quick_s_rec = []
# Quick_s_itr = []
# pl.plot(inputs,Bubble_s,marker="+")
# pl.plot(inputs,Selection_s,marker="o")
# pl.plot(inputs,Insertion_s,marker="*")
# pl.plot(inputs,Merge_s_recursive,marker="x")
# pl.plot(inputs,Merge_s_iterative,marker="s")
# pl.plot(inputs,Quick_s_rec,marker="P")
# pl.plot(inputs,Quick_s_itr,marker="^")
# pl.legend(["Bubble Sort","Selection Sort","Insertion Sort","Merge Sort Rec", "Merge Sort Itr","Quick Sort Rec", "Quick Sort Itr"],loc = "upper left")
# pl.xlabel("No. of inputs")
# pl.ylabel("Time taken by each input(in seconds.)")
# pl.title("Performance Analysis of Sorting Algorithms")
# pl.show()

if __name__ == "__main__":
    # inputs = [10,100,1000,10000,100000]
    # here you can input the nos. like 10, 100, 1000
    # to check for each algorithm's real time complexity
    # and put that time in a repective list above to plot the graph

    # **Note: Please avoid printing large array like 10000, 100000, etc
    n = int(input("Enter no. of input : "))
    tracemalloc.start()
    Array = random.sample(range(1, 3*n), n)
    start = time.time()
    Merge_sort_Recursion(Array)
    printList(Array) # don't use this function for large array size
    time.sleep(1)
    end = time.time() 
    print(f"Time required is: {end-start} sec.")
    print(f"Memory used by sorting Algorithm: {tracemalloc.get_traced_memory()[0]} bytes")
    print(f"Peak memory used by Whole Program: {tracemalloc.get_traced_memory()[1]} bytes")
    tracemalloc.stop()
