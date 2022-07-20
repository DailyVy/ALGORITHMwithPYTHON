# p.40 동명이인 찾기(1)

# 내가 짜보자고
def findSameName(nameList):
    sameNameSet = set() # 비어있는 집합 자료형 만들기
    for i in range(len(nameList)-1): # 마지막 이름을 기준으로는 비교하지 않아도 됨
        compareName = nameList[i]
        for j in range(i+1, len(nameList)):
            if compareName == nameList[j]:
                sameNameSet.add(compareName)
    return sameNameSet

# 책에서 짠거
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1): # 0부터 n-2까지 반복
        for j in range(i+1, n): # i+1부터 n-1까지 반복
            if a[i] == a[j]:
                result.add(a[i])
    return result

################ 연습문제 ######################
def yourPartner(aList): # 리턴문이 없음 바로 출력하도록 함
    n = len(aList)
    result = []
    for i in range(n-1): # 맨 마지막 사람은 이미 짝이 지어졌겠지 뭐
        first = aList[i]
        for j in range(i+1, n):
            partner = []
            partner.append(first)
            partner.append(aList[j])
            result.append(partner)
    # 결과를 출력합시다.
    for jjak in result:
        print(f'{jjak[0]} - {jjak[1]}')

### 연습문제 답 ###
def print_pairs(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(a[i], "-", a[j])

if __name__ == "__main__":
    name = ["Tom", "Jerry", "Mike", "Tom", "Mike", "Yuna"]
    print(findSameName(name))
    print(find_same_name(name))
    print()

    partner = ["Tom", "Jerry", "Mike"]
    partner2 = ["Tom", "Jerry", "Mike", "John"]

    yourPartner(partner)
    print()
    yourPartner(partner2)
    print()
    print_pairs(partner)
    print()
    print_pairs(partner2)