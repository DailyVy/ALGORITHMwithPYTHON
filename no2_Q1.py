# p.50 팩토리얼 구하기

# for문으로 팩토리얼
# 입력 : n
# 출력 : 1부터 n까지 연속된 숫자를 곱한 값
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

# 재귀 호출로 팩토리얼 구하기
def factR(n):
    if n <= 1: # 종료 조건
        return 1
    return n * factR(n-1)

##################### 연습문제 ####################
# 4-1. 1부터 n까지의 합 구하기를 재귀 호출로 만들기
def sumR(n):
    if n == 1: # 종료 조건
        return 1
    return n + sumR(n-1)

# 이렇게 하면 n==0일때 에러가 난다!!! 근데 보통 1부터 0까지의 합을 구하라고는 하지 않잖아.....

### 답지 ###
"""
종료 조건 : n=0 ==> 결괏값 0
재귀 호출 조건 : n까지의 합 = n-1까지의 합 + n
"""
def sum_n(n):
    if n == 0:
        return 0
    return sum_n(n-1) + n

# 4-2. 최댓값 찾기를 재귀 호출로 만들기
def findMaxR(aList):
    max_v = aList[len(aList)-1]
    if len(aList) == 1: # 종료 조건 : List의 길이가 1이면 List[0]이 최댓값 ==> max_v = aList[0]
        return max_v
    com_v = findMaxR(aList[:len(aList)-1])
    if max_v < com_v:
        max_v = com_v
    return max_v

### 답지 ###
"""
종료 조건 : 자료 값이 한 개면 (n=1) 그 값이 최댓값
재귀 호출 조건 : n개 자료 중 최댓값 ==> n-1개 자료 중 최댓값과 n-1번 위치 값 중 더 큰값
"""
def find_max(a, n): # 리스트 a의 앞부분 n개 중 최댓값을 구하는 재귀 함수
    if n == 1:
        return a[0]
    max_n_1 = find_max(a, n-1) # n-1개 중 최댓값을 구함
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]

# 확실히 답지가 좀 더 직관적이긴 하다.... 흠...

if __name__ == "__main__":
    print(fact(5)) # 120
    print(fact(4)) # 24
    print(fact(1)) # 1
    print()
    print(factR(5))
    print(factR(4))
    print(factR(1))
    print()
    print("################연습 문제 4-1#################")
    print(sumR(10)) # 55가 나와야해
    print(sumR(100)) # 5050이 나와야해
    print(sumR(1))
    # print(sumR(0)) # 에러발생
    print("============답지=============")
    print(sum_n(10))
    print(sum_n(100))
    print(sum_n(1))
    print(sum_n(0))
    print("################연습 문제 4-2#################")
    v = [17, 92, 18, 33, 58, 7, 33, 42]
    print(findMaxR(v)) # 92 가 나와야해
    print(find_max(v, len(v))) # 92