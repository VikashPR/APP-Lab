a = (11, 2, 3, 14)
b = (13, 5, 22, 10)
c = (12, 2, 3, 10)
print("Element wise-sum sum of given tuples : ")
res = tuple(map(sum, zip(a,b,c)))
print(res)