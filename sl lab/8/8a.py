dict={'h' : 'hydrogen', 'n' : 'nitrogen'}
print(dict)
sym=input("Enter the symbol of the element")
name=input("Enter the name of the element")
if sym not in dict:
    dict[sym]=name
else:
    print("Element already in the list")
print(len(dict))
ele=input("Enter the symbol of the element to search")
if ele in dict:
    print("Element present in the list",dict[ele])
else:
    print("Element not present in the list")