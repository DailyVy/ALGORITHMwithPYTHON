# a = [1, 2, 3]
#
# b = [i+1 for i in a]
# print(b)
# print(max(a))

d = [6, 8, 3, 9, 5, 2, 4, 7, 10]
n = len(d)
pivot = n // 2 # 4, 원소 값은 5
g1 = d[:pivot]
g2 = d[pivot+1:]
print(g1, g2)

# g2.append(g1.pop(3))
d.insert(3, g1.pop(3))
print(g1, g2, d)


