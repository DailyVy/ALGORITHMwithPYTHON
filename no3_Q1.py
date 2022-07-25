# p.80 순차 탐색
# 첫 번째 자료부터 하나씩 비교하면서 같은 값이 나오면 그 위치를 결과로 돌려주고,
# 리스트 끝가지 찾아도 같은 값이 나오지 않으면 -1을 돌려준다.

# 내가 짠 거 ==> 잘못짬
# 중복된 값의 인덱스를 찾았네ㅠㅜ 그냥 그 값이 있는지 찾는거였는데...
# def orderFind(aList, val):
#     # 일단 val이 aList에 존재하는가
#     if val in aList: # 만약 존재한다면?
#         first = aList.index(val) # val의 위치(중복된다면 처음 위치)
#         for i in range(first+1, len(aList)): # 처음위치 + 1 부터 끝까지 탐색해보자고
#             if aList[i] == val: # 만약 중복된다면?
#                 return i
#     return -1

# 책에서 짠 거
# 입력 : 리스트 a, 찾는 값 x
# 출력 : 찾으면 그 값의 위치, 찾지 못하면 -1
def search_list(a, x):
    n = len(a)
    for i in range(0, n): # f
        if x == a[i]:
            return i
    return -1

################# 연습문제 #################
# 7-1. 모든 위치를 리스트로 돌려주는 탐색 알고리즘
# 입력 : 리스트 aList, 찾는 값 x
# 출력 : 인덱스가 포함된 리스트, 없으면 빈리스트
def search_all(aList, x):
    result = []
    for i in range(len(aList)):
        if aList[i] == x:
            result.append(i)
    return result

# 7-3. 학생 번호에 해당하는 이름을 순차 탐색으로 찾아 돌려주는 함수
def search_stu_no(stu_name, stu_no, number):
    """
    :param stu_name: 학생 이름 리스트
    :param stu_no: 학생 번호 리스트
    :param number: 학생 번호
    :return: number에 해당하는 학생 이름
    """
    # if number not in stu_no: return "?" # 해당하는 학생 번호가 없으면 물음표(?)를 돌려줌
    # 이는 맨 밑에 그냥 return "?"로만 해줘도 된다.

    for i in range(len(stu_no)):
        if stu_no[i] == number:
            return stu_name[i]

    return "?"

if __name__ == "__main__":
    v = [17, 92, 18, 33, 58, 5, 33]

    # print(orderFind(v, 18))
    # print(orderFind(v, 33))
    # print(orderFind(v, 900))
    # print()
    print(search_list(v, 18))
    print(search_list(v, 33))
    print(search_list(v, 900))

    print()

    print(search_all(v, 18))
    print(search_all(v, 33))
    print(search_all(v, 900))

    print()

    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]

    print(search_stu_no(stu_name, stu_no, 39))
    print(search_stu_no(stu_name, stu_no, 14))
    print(search_stu_no(stu_name, stu_no, 1))