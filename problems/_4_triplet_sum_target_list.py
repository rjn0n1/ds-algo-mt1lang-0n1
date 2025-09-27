def findTriplet(arr, n, x) :
    #write your code logic 
    res=[]
    count = 0
    i=0
    while i <= n-3:
        j=i+1
        f = arr[i]
        while j<=n-2:
            s = arr[j]
            rem = x - f-s
            k=j+1
            while k<n:
                if arr[k] == rem:
                    count +=1
                    res.append([f,s,arr[k]])
                k +=1
            j +=1
        i +=1
    return res #count
print(findTriplet([1 ,2 ,3, 4, 5, 6, 7],7,12))



