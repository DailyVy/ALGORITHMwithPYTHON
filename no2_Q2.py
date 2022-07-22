# p.60 최대공약수 구하기

# 입력 : a, b
# 출력 : a와 b의 최대공약수

# 일반적인 최대공약수 구하기
def gcd(a, b):
    i = min(a, b) # 두 수 중에서 최솟값을 구하는 파이썬 함수
    # i = a if a <= b else b # 위와 같음

    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

# 유클리드 호제법을 이용한 알고리즘
"""
- a와 b의 최대공약수는 ‘b’와 ‘a를 b로 나눈 나머지’의 최대공약수와 같다.
    ⇒ 즉, gcd(a, b) = gcd(b, a%b)
- 어떤 수와 0의 최대공약수는 자기 자신 ⇒ 즉, gcd(n, 0) = n
"""
def gcd_eu(a, b):
    # print("gcd : ", a, b) # 함수 호출 입력(인자) 값과 함께 화면에 표시
    if b == 0: # 종료 조건
        return a
    return gcd_eu(b, a % b) # 좀 더 작은 값으로 자기 자신을 호출

##################### 연습문제 ####################
# 5-1. n번째 피보나치 수 구하기
# 피보나치 수열이 파이썬의 리스트처럼 0번부터 시작한다고 가정할 때 n번째 피보나치 수를 구하시오

def fibo_num(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibo_num(n-1) + fibo_num(n-2)

### 답지 ###
# 입력 : n값(0부터 시작)
# 출력 : n번 피보나치 수 = n-2번 피보나치 수 + n-1번 피보나치 수
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-2) + fibo(n-1)

if __name__ == "__main__":
    # print(gcd(12, 8))
    # print(gcd_eu(1, 5))
    # print(gcd_eu(3, 6))
    # print(gcd_eu(6, 3))
    # print(gcd_eu(60, 24))
    # print(gcd_eu(81, 27))

    print(fibo_num(0)) # 0
    print(fibo_num(1)) # 1
    print(fibo_num(2)) # 1
    print(fibo_num(3)) # 2
    print(fibo_num(4)) # 3
    print(fibo_num(5)) # 5
    print(fibo_num(6)) # 8
    print(fibo_num(7)) # 13
