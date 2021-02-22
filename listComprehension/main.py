# x = []
# for i in range(11):
#     if i % 2 == 0 and i != 0:
#         x.append(i)
# print(x)

print([x for x in range(11) if x % 2 == 0 and x != 0])

print([x for x in range(11) if x % 2 != 0 and x != 0])
