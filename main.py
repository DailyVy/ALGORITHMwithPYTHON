import math

"""
절댓값 알고리즘 1(부호 판단)
입력 : 실수 a
출력 : a의 절댓값
"""

def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a

"""
절댓값 알고리즘 2(제곱-제곱근)
입력 : 실수 a
출력 : a의 절댓값
"""

def abs_square(a):
    b = a * a
    return math.sqrt(b) # math.sqrt는 float형을 되돌려줌

print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(5))
print(abs_square(-3))