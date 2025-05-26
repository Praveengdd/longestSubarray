#code to find out the longest subarray in an array with given sum

#read array and the target from the user
arr = list(map(int, input("Enter the array elements seperated by space: ").split()))
target = int(input("Enter the target: "))

#brute force approach with only two for loops
mlen = 0

arr.sort()

i = 0
j = 0
summ = arr[i]
while i < len(arr):
    while j <= i and summ > target:
        summ -= arr[j]
        j += 1
        
    if summ == target:
        mlen = max(mlen, i - j + 1)
        
    i += 1
    if i < len(arr):
        summ += arr[i]
        
        
            
print("Maximum length subarray's length is", mlen)