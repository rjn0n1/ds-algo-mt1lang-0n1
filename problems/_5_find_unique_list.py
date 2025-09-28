
'''
Problem statement
You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].

Now, in the given array/list, 'M' numbers are present twice and one number is present only once.

You need to find and return that number which is unique in the array/list.

 Note:
Unique element is always present in the array/list according to the given condition.
'''


def findUnique(arr, n) :
    #write your code here 
    #1 2 2 3 3 6 6 
    #1 1 3 3 6 6 7 7 10
    '''
    1. sort
    2. when match with next, go to next with i+2
    3. make sure i+1 < n befoe using in index.
    4. if do not match return arr[i]
    '''
    arr.sort()
    i = 0
    while i+1<n and arr[i] == arr[i+1]:
        i += 2
    return arr[i]

print (findUnique([1,2,1,3,3,2,4],7))


'''
Time Complexity:
O(nlog(n)):: since sorting involved.
while loop => n//2 times

Space:
no extra space needed, other than in sorting.
So O(1): independent of input size.

'''