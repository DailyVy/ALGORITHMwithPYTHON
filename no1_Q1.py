# p.22 1부터 n까지 연속한 정수의 합을 구하는 알고리즘을 만들어 보시오.

# 알고리즘 1
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

# 알고리즘 2 : 가우스
# n(n+1)/2

def sum_gauss(n):
    return n*(n+1) // 2 # 정수 나눗셈


################# 연습문제 #################
def square_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i**2
    return s

def square_sum2(n):
    return n*(n+1)*(2*n+1)//6

if __name__ == "__main__":
    print(sum_n(10))
    print(sum_n(100))
    print()
    print(sum_gauss(10))
    print(sum_gauss(100))
    print()

    print(square_sum(10))
    print(square_sum2(10))