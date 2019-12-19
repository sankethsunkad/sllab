lst = []
n = int(input("Enter the number of elements in the list"))
for i in range(0, n):
    ele = int(input("Enter the element"))
    lst.append(ele)
print(lst)
ele=int(input("Enter the element to append"))
lst.append(ele)
print(lst.pop())
x=int(input())
if x not in lst:
    print("Not in the list")
else:
    print("element found in the list")