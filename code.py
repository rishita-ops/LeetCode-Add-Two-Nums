"""
Add Two Numbers :
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
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