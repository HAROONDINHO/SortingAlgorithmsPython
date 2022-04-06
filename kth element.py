from sorts import partition

#this functions uses partitioning to find the kth smallest element in an unsorted array

def find_kth(arr, start, end, k):
    if start <= end:
        p = partition(arr, start, end)
        if k - 1 == p:
            return arr[p]
        elif k - 1 < p:
            return find_kth(arr, start, p - 1, k)
        if k - 1 > p:
            return find_kth(arr, p + 1, end, k)


ar=[2,5,1,7,6,10]
x=find_kth(ar,0,len(ar)-1,3)
print(x)