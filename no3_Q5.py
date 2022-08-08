# p.109 퀵정렬

### 쉽게 설명한 퀵 정렬 알고리즘
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

def quick_sort(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음
    if n <= 1:
        return a

    # 기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot = a[-1] # 편의상 리스트의 마지막 값을 기준 값으로 정함
    g1 = []
    g2 = []

    for i in range(0, n-1): # 마지막 값은 기준 값이므로 제외
        if a[i] < pivot: # 기준 값과 비교
            g1.append(a[i]) # 작으면 g1에 추가
        else:
            g2.append(a[i]) # 크면 g2에 추가

    # 각 그룹에 대해 재귀 호출로 퀵 정렬을 한 후
    # 기준 값과 합쳐 하나의 리스트로 결괏값 반환
    return quick_sort(g1) + [pivot] + quick_sort(g2)

### 일반적인 퀵 정렬 알고리즘
# 새로운 리스트로 병합하지말고 입력 리스트 안의 자료를 직접 바꾸자
# 입력 : 리스트 a
# 출력 : 없음(입력으로 주어진 a가 정렬됨)

# 내가 짜보자.. => 실패

# 책에서 짠거
# 리스트 a에서 어디부터(start) 어디까지(end)가 정렬 대상인지
# 범위를 지정하여 정렬하는 재귀 호출 함수
def quick_sort_sub(a, start, end):
    # 종료 조건 : 정렬 대상이 한 개 이하이면 정렬할 필요가 없음
    if end - start <= 0:
        return
    # 기준 값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤
    # [기준 값보다 작은 값들, 기준 값, 기준 값보다 큰 값들]
    pivot = a[end] # 편의상 리스트의 마지막 값을 기준 값으로 정함
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    # 재귀 호출 부분
    quick_sort_sub(a, start, i - 1) # 기준 값보다 작은 그룹을 재귀 호출로 다시 정렬
    quick_sort_sub(a, i + 1, end) # 기준 값보다 큰 그룹을 재귀 호출로 다시 정렬

# 리스트 전체(0 ~ len(a)-1)를 대상으로 재귀 호출 함수 호출
def quickSort(a):
    quick_sort_sub(a, 0, len(a) - 1)


if __name__ == "__main__":
    d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    # print(quick_sort(d))
    quickSort(d)
    print(d)