"""
for loop and while loop
x++ garna paidaina
x+=1 garne or
x=x+1
name.append() to add data 0 to no
name.insert(position,element)

break: go outside loop
contine: only one part chodcha


"""


# users=[["Ram","SIta","Laxman"],["A","B","C"],["e","f","g"]]
# print(users[0][1])
# for user in users:
#     for usr in user:
#         print(usr)



"""
no=int(input("Enter no of students:"))
x=0
name=[]
while x<no:
    name.insert(x,input("Enter your name:"))
    x=x+1
i=0
while i<no:
    print(name[i])
    i=i+1
"""

x=0
# while x<10:
#     if x==5:
#         break
#     print(x)
#     x=x+1
while x<10:
    x = x + 1
    if x==5:
        continue
    print(x)


