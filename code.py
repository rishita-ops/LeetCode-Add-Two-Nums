nl1 = int(input("Enter the number of elements in the first list: "))
l1 = []
for i in range(nl1):
    l1.append(int(input(f"Enter element {i+1}: ")))

nl2 = int(input("Enter the number of elements in the second list: "))
l2 = []
for i in range(nl2):
    l2.append(int(input(f"Enter element {i+1}: ")))

sl1=0
for i in range(nl1):
    sl1 += l1[i] * (10 ** i)

sl2=0
for i in range(nl2):
    sl2 += l2[i] * (10 ** i)

result = sl1 + sl2

output = list(map(int, str(result)))
output.reverse()
print(output)
