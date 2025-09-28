'''
find the second larget element from a list of size n
'''
def secondLargestElement(arr,n):
    '''
    1. sort
    2. the 2nd last element
    '''
    arr.sort()
    return arr[n-2]

print(secondLargestElement([2,1,3,2,5,6,],6))

def secondLargestElement2(arr,n):
    '''
     [8,3,2,10,0,0,2,2,8,1]
    '''
    fmax = -2147483648
    smax = -2147483648

    i=0
    while i < n:
        if arr[i] > fmax:
            smax = fmax
            fmax = arr[i]
        elif arr[i] > smax:
            smax = arr[i]
        i +=1
    return smax

print(secondLargestElement2([2,1,3,2,5,6,],6))


'''
Time complexity
2: O(n) since one loop, 
1st: O(nlogn) , since sorting involved.

Space Complexity:
No extra space needed so O(1)
'''
