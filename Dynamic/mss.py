arr = [7, 8, 12, -5, 22, -7, -6, -100, 8, -3, -2, 7, 72 ]



def maxSubarray(arr):

    ans = []

    #Base case
    ans.append((arr[0], 0, 0))
    running_sum = arr[0]

    for i in range (1, len(arr)):
        if running_sum < 0:
            if arr[i] > 0:
                positive_found = True
                running_sum = arr[i] 
                ans.append((arr[i], i, i))
            else:
                if ans[i-1][0] > arr[i]:
                    ans.append(ans[i-1])
                else:
                    ans.append((arr[i], i, i))
        else:
            running_sum += arr[i]
            if running_sum > ans[i-1][0]:
                ans.append((running_sum, ans[i-1][1], i))
            else:
                ans.append(ans[i-1])


    maxSum = float('-inf')
    for value in ans:
        if value[0] > maxSum:
            output = value

    return output

print(maxSubarray(arr))




