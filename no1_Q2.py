# p.33 최댓값 찾기

# 내가 짠 거
def findMaxList(aList):
    tempMax = aList[0]

    for i in range(len(aList)):
        if tempMax < aList[i]:
            tempMax = aList[i]

    return tempMax

# 책에서 짠거
def find_max(a):
    n = len(a)
    max_v = a[0]

    for i in range(1, n): # 1부터 n-1까지 반복
        if a[i] > max_v:
            max_v = a[i] # 최댓값 변경

    return max_v

# 내가 짠 max Index
def findMaxIndex(aList):
    n = len(aList)
    # max_v = aList[0]
    max_i = 0
    max_v = aList[max_i]
    for i in range(1, n):
        if aList[i] > max_v:
            max_v = aList[i]
            max_i = i
    return max_i

# 책에서 짠 max Index
def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx


############# 연습문제 ################
def findMin(aList):
    n = len(aList)
    min_val = aList[0]
    for i in range(1, n):
        if min_val > aList[i]:
            min_val = aList[i]
    return min_val

def findMinIdx(aList):
    n = len(aList)
    min_idx = 0
    for i in range(1, n):
        if aList[i] < aList[min_idx]:
            min_idx = i
    return min_idx

if __name__ == "__main__":
    v = [17, 92, 18, 33, 58, 7, 33, 42]

    print(findMaxList(v))
    print()
    print(find_max(v))
    print()
    print(findMaxIndex(v)) # 1이 나와야함
    print()
    print(find_max_idx(v))
    print()
    print(findMin(v)) # 7이 나와야함
    print()
    print(findMinIdx(v)) # 5