'''
input: 0 to n-1 integer with 1 duplicate
output: the duplicate one.
Example:
n =5: => [0,1,2,3,4,2]
output = > 2    
'''
def findDuplicate(arr):
    sumArr = sum(arr)
    n = len(arr)
    sumOfN = ((n-1)*(n-2))/2
    duplicate= sumArr-sumOfN
    return duplicate

def findDuplicate2(arr):
    '''
        steps:
        1. Sort such that the duplicate will come in sequece one after another
        2. start traversing the list, comparing num to its adjacent next one.
        3. if different then return
    '''
    arr.sort()
    i=0
    while i<len(arr)-1: #since 2nd lst will be compare to last.
        if arr[i] == arr[i+1]:
            return arr[i] # arr[i+1]
        
        i += 1
    


print(findDuplicate([0,1,2,3,4,6,5,6]))
print(findDuplicate2([0,1,2,3,4,6,5,6]))


'''
Time Complexity
#2# O(nlogn) since sorting involved
#1# O(1) every operation in unit time consuming, independent of input size.

Space complexity: O(1), since no extra space is required.

'''