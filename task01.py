#dictionary = {"a": 1, "b": 2, "c": 3}

# st = set([1, 2, 3, 4, 5])
# print(st)
# print(len(st))
# print(type(st))

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
fb = frozenset(b)
fb.add(10)
print(type(fb))
#c = a.intersection(b)
#c = a.union(b)
#c = a.difference(b)
#c = b.difference(a)
#c = a.symmetric_difference(b)
#print(a)
#a.update(b)
#a.add(7)
#a.remove(7)
#a.clear()
#print(a)
