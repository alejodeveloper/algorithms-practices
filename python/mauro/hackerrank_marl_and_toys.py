read = input().split()
n_of_items = int(read[0])
budget = int(read[1])
prices = input().split()
toys = []
for x in prices:
    toys.append(int(x))
toys.sort()
c = 0
p = 0
while c < n_of_items and p < budget:
    p += toys[c]
    c += 1
if p > budget:
    c -= 1
print(c)