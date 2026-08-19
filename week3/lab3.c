def selection_sort(arr):
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[mini]>arr[j]:
                mini=j
        arr[mini], arr[i] = arr[i], arr[mini]
    return arr

n=int(input("enter the no of elements"))
arr=[]

for i in range(n):
    arr.append(int(input("enter the element:")))

print(selection_sort(arr))
