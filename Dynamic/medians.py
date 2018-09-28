import sys

arr = [-1, 32, 7, 8, -3, 4, 2]


def findMedians(arr):
    ans = [[] for _ in arr]


    for i in range (len(arr) - 1, -1, -1):
        for j in range(i, len(arr), 2):
            #Base case
            if j == i:
                ans[i].append([None, arr[i], None])

            elif j-i == 2:
                tmp = [arr[i],arr[i+1],arr[j]]
                tmp.sort()
                ans[i].append(tmp)

            else:
                lnth = ((j-i)//2) - 1
                tmp = ans[i+2][lnth]
                tmp.append(arr[i])
                tmp.append(arr[i+1])
                tmp.sort()
                ans[i].append([tmp[1], tmp[2], tmp[3]])

        for length in range(0, len(ans[i])):
            if length == 0:
                print('Medians starting at position {0}:'.format(i), end=' ')
                print(ans[i][0][1], end=' ')
            else:
                print(ans[i][length][1], end=' ')
        print()
        
        #Free up memory to achieve O(n) space
        if i < len(arr) - 2:
            del ans[i+2]



findMedians(arr)



            











