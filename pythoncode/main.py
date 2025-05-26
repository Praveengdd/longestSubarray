#code to find out the longest subarray in an array with given sum

#read array and the target from the user
arr = list(map(int, input("Enter the array elements seperated by space: ").split()))
target = int(input("Enter the target: "))

#brute force approach
mlen = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        summ = 0
        count = 0
        for k in range(i, j + 1):
            summ += arr[k]
            count += 1
        if summ == target:
            mlen = max(count, mlen)
            
print("Maximum length subarray's length is", mlen)