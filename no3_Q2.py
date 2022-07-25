# p.84 선택 정렬

### 쉽게 설명한 선택 정렬 알고리즘
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트
# 주어진 리스트에서 최솟값의 위치를 돌려주는 함수

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = [] # 새 리스트를 만들어 정렬된 값을 저장
    while a: # 주어진 리스트에 값이 남아 있는 동안 계속
        min_idx = find_min_idx(a) # 리스트에 남아 있는 값 중 최솟값의 위치
        value = a.pop(min_idx) # 찾은 최솟값을 빼내어 value에 저장
        result.append(value)
    return result

### 일반적인 선택 정렬 알고리즘
# 입력 : 리스트 a
# 출력 : 없음(입력으로 주어진 a가 정렬됨)

# 내가 먼저 일단 짜볼래
# 0:len(a)-1 해서 최솟값 찾아서 0번째 자리와 교환
# -> 1:len(a)-1 최솟값 찾아서 1번째 자리와 교환
# -> 2:len(a)-1 최솟값 찾아서 2번째 자리와 교환
# .. 이렇게 하면 되지 않을까?
def general_sel_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = findMinIdx(i, a) # 최솟값의 index
        a[i], a[min_idx] = a[min_idx], a[i]

def findMinIdx(start, aList):
    """
    :param start: start부터 찾기
    :param aList: 입력 리스트
    :return: 최솟값 인덱스
    """
    min_idx = start
    for i in range(start, len(aList)):
        if aList[i] < aList[min_idx]:
            min_idx = i
    return min_idx

# 책에서 짠 거
def sel_sort2(a):
    n = len(a)
    for i in range(0, n-1): # 0부터 n-2까지 반복
        # i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i] # 이게 for j 문 안에 있으면 안됨

################ 연습 문제 ###################
# 오름차순 정렬을 내림차순으로 정렬

# A. 책의 코드를 응용하는 방법
def selSortOption(a, b=True):
    n = len(a)
    if b:
        for i in range(0, n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if a[j] < a[min_idx]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
    else:
        for i in range(0, n - 1):
            max_idx = i
            for j in range(i + 1, n):
                if a[j] > a[max_idx]:
                    max_idx = j
            a[i], a[max_idx] = a[max_idx], a[i]

# B. 내가 짠거 응용
def generalSelSortOption(a, ascending=True):
    n = len(a)
    for i in range(n):
        if ascending:
            min_idx = findMinIdx(i, a) # 최솟값의 index
            a[i], a[min_idx] = a[min_idx], a[i]
        else:
            max_idx = findMaxIdx(i, a) # 최댓값의 index
            a[i], a[max_idx] = a[max_idx], a[i]

def findMaxIdx(start, aList):
    """
    :param start: start부터 찾기
    :param aList: 입력 리스트
    :return: 최댓값 인덱스
    """
    max_idx = start
    for i in range(start, len(aList)):
        if aList[i] > aList[max_idx]:
            max_idx = i
    return max_idx

if __name__ == "__main__":
    # d = [2, 4, 5, 1, 3]
    # general_sel_sort(d)
    # print(d)

    # e = [99, 45, 13, 24, 66, 78, 55, 32, 13]
    # general_sel_sort(e)
    # print(e)

    # f = [2, 4, 5, 1, 3]
    # print(f)
    # sel_sort2(f)
    # print(f)

    # g = [99, 45, 13, 24, 66, 78, 55, 32, 13]
    # selSortOption(g, False)
    # print(g)

    h = [99, 45, 13, 24, 66, 78, 55, 32, 13]
    generalSelSortOption(h, False)
    print(h)
