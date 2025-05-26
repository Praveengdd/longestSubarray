#code to find out the longest subarray in an array with given sum

#read array and the target from the user
arr = list(map(int, input("Enter the array elements seperated by space: ").split()))
target = int(input("Enter the target: "))

#brute force approach with only two for loops
mlen = 0

dic = {}
ps = 0
summ = 0

for i in range(len(arr)):
    ps += arr[i]
    
    if ps == target:
        mlen = max(mlen, i + 1)
        
    if ps - target in dic:
        mlen = max(mlen, i - dic[ps - target])
        
    if ps not in dic:
        dic[ps] = i
        
        
            
print("Maximum length subarray's length is", mlen)