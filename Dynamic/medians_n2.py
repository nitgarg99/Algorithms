
def findMedians(arr):
    #Ans[0] is last element in array. Ans[-1] is first element in arr
    #Each element is a list where index 0 is length 1 median, index 2 is 
    #length 3 median ...
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


arr = [-1, -2, -3, 4, 0, 5, 24, -9, 2]

findMedians(arr)



            











