def bubble_sort():
    arr=[0,1,5,4,9,91,78]
    n=len(arr)
    for i in range(1,n):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)



if __name__ == "__main__":
    bubble_sort()
