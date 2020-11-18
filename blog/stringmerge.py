string1=input()
list1=list(string1)
for i in range(int(input())):
	string2=input()
    for j in string2:
        if j in list1:
            list1.remove(j)
if len(list1)==0:
    print("YES")
else:
    print("NO")