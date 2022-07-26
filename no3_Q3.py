# p.92 삽입 정렬

### 쉽게 설명한 선택 정렬 알고리즘
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

# 내가 한 번 짜보자
def insertSort(a):
    n = len(a)
    result = []

    result.append(a[0]) # 일단 맨 처음 값을 맨 첫번째에 집어넣는다.

    for i in range(1, n):
        for j in range(len(result)):
            if a[i] > max(result):
                result.append(a[i])
            elif a[i] < result[j]:
                result.insert(j, a[i])
                # print(result)
                break
            else:
                continue
    return result

# 책에서 짠 거
# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(r, v):
    # 이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인하여
    for i in range(0, len(r)):
        # v값보다 i번 위치에 잇는 자료 값이 크면
        # v가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨
        if v < r[i]:
            return i
    # 적절한 위치를 못 찾았을 때는
    # v가 r의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입
    return len(r)

def ins_sort(a):
    result = [] # 새 리스트를 만들어 정렬된 값을 저장
    while a: # 기존 리스트에 값이 남아있는 동안 반복
        value = a.pop(0) # 기존 리스트에서 한 개를 꺼냄 (맨 앞의 값)
        ins_idx = find_ins_idx(result, value) # 꺼낸 값이 들어갈 적당한 위치 찾기
        result.insert(ins_idx, value) # 찾을 위치에 값 삽입(이후 값은 한 칸씩 밀려남)
        print(result)
    return result

### 일반적인 선택 정렬 알고리즘
# 입력 : 리스트 a
# 출력 : 없음(입력으로 주어진 a가 정렬됨)

# 내가 먼저 짜보자
# 일단 a[0]은 고정이고 a[1]부터 비교할거야
# a[1]을 a[0]~a[n-1]까지 비교해서 적절한 위치를 찾을 거임
def genInsSort(a):
    for i in range(1, len(a)):
        for j in range(i):
            if a[i] < a[j]:
                ins_val = a.pop(i)
                a.insert(j, ins_val)
                break
    # return a # 제대로 짰는지 확인

# 책에서 짠거
def gen_ins_sort(a):
    n = len(a)
    for i in range(1, n): # 1부터 n-1까지
        key = a[i] # i번 위치에 있는 값을 key에 저장
        # j를 i 바로 왼쪽 위치에 저장
        j = i - 1
        # 리스트 j번 위치에 있는 값과 key를 비교해서 key가 삽입될 적절한 위치를 찾음
        while j >= 0 and a[j] > key: # key 보다 큰 애들을 옆으로 밀어버리나봄
            a[j + 1] = a[j] # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j -= 1
        a[j + 1] = key
    # return a # 제대로 짰는지 확인

################# 연습 문제 ###################
# 오름차순 정렬을 내림차순으로 정렬
def genInsSortAscend(a, ascending=True):
    n = len(a)
    for i in range(1, n): # 1부터 n-1 까지
        key = a[i]
        j = i - 1
        if ascending:
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key
        else:
            while j >= 0 and a[j] < key:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key

    return a


if __name__ == "__main__":
    d = [2, 4, 5, 1, 3]
    test = [5, 8, 3, 2, 4, 1, 9, 6, 11, 0]

    # print(insertSort(d))
    # print(insertSort(test))
    # print(ins_sort(d))
    # print(ins_sort(test))

    # print(genInsSort(test))
    # print(genInsSort(d))
    # print(gen_ins_sort(test))
    # print(gen_ins_sort(d))

    print(genInsSortAscend(test, False))