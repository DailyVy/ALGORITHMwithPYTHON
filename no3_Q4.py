# p.99 병합 정렬

### 쉽게 설명한 병합 정렬 알고리즘
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

# 일단 내가 얼레벌레 짜본다... ==> 실패
def mergeSort(aList):
    result = []
    n = len(aList)

    # 일단 두 조로 나누자~
    firstGroup = aList[:(n//2)] # n이 홀수일수도 있으니까
    secondGroup = aList[(n//2):]

    # print(firstGroup)
    # print(secondGroup)

    # 그리고 이 두 조를 정렬시키자.... 이건 무슨 정렬이 필요하징 내부 함수 쓰겠슴다
    # firstGroup.sort()
    # secondGroup.sort()

    #... 모르겠다

    return result

# 책에서 짠거
def merge_sort(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
    if n <= 1:
        return a

    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2 # 중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(a[:mid]) # 재귀 호출로 첫 번째 그룹을 정렬
    g2 = merge_sort(a[mid:]) # 재귀 호출로 두 번째 그룹을 정렬

    # 두 그룹을 하나로 병합
    result = []
    while g1 and g2: # 두 그룹에 자료가 모두 남아 있는 동안 반복
        if g1[0] < g2[0]: # 두 그룹의 맨 앞 자료 값을 비교
            # g1 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    # 아직 남아 있는 자료들을 결과에 추가
    # g1과 g2 중 이미 빈 것은 while을 pass함
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

### 일반적인 병합 정렬 알고리즘
# 새로운 리스트로 병합하지말고 입력 리스트 안의 자료를 직접 바꾸자
# 입력 : 리스트 a
# 출력 : 없음(입력으로 주어진 a가 정렬됨)

# 책
def genMergeSort(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
    if n <= 1:
        return

    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2  # 중간을 기준으로 두 그룹으로 나눔
    g1 = a[:mid]
    g2 = a[mid:]
    genMergeSort(g1)  # 재귀 호출로 첫 번째 그룹을 정렬
    genMergeSort(g2)  # 재귀 호출로 두 번째 그룹을 정렬

    # 두 그룹을 하나로 병합
    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    # 아직 남아 있는 자료들을 결과에 추가
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1



if __name__ == "__main__":
    d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

    # print(merge_sort(d))
    genMergeSort(d)
    print(d)