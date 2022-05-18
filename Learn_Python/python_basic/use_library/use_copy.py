import copy

src = [1, [2, 3], (4, 5, 6), "789"]
dst1 = src
dst2 = src[:]
dst3 = list(src)

print(dst1 is src)
print(dst1[0] is src[0])
print(dst1[1] is src[1])
print(dst1[2] is src[2])
print(dst1[3] is src[3])
print("==========================")
print(dst2 is src)
print(dst2[0] is src[0])
print(dst2[1] is src[1])
print(dst2[2] is src[2])
print(dst2[3] is src[3])
print("==========================")
print(dst3 is src)
print(dst3[0] is src[0])
print(dst3[1] is src[1])
print(dst3[2] is src[2])
print(dst3[3] is src[3])

a = [1, 2, ["x", "y"]]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a.append(3)
a[2].append("z")
a.append(["x", "y"])
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)

L = [1, 2]
M = L
L += L
print(L, M)

L = [1, 2]
M = L
L = L + L
print(L, M)

s = "123"
t = s
s += s
print(s, t)

s = "123"
t = s
s = s + s
print(s, t)

a = ""
b = ""
print("a == b:", a == b)
print("a is b:", a is b)

a = []
b = []
print("a == b:", a == b)
print("a is b:", a is b)

a = "123"
b = "123"
print("a == b:", a == b)
print("a is b:", a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print("a == b:", a == b)
print("a is b:", a is b)
