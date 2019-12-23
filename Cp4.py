l = list(range(1,1000001))
print(min(l))
print(max(l))
print(sum(l))

oddL = list(range(1,21,2))
for e in oddL:
    print(e)

devByThree = list(range(3,30,3))
for e in devByThree:
    print(e)

cubicL = list(v ** 3 for v in range(1,10))
for e in cubicL:
    print(e)

foods = (0, 1, 3, 5, 7)
for e in foods:
    print(e)
