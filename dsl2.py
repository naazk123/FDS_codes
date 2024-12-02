def listinput(lst):
    n=int(input("Enter the number of candidate:"))
    for i in range(n):
        a=input("Enter name of student:")
        lst.append(a)
    return lst

def intersection(lst1,lst2,lst3):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if(lst1[i]==lst2[j]):
                lst3.append(lst1[i])
    return lst3

def difference(lst1,lst2,lst3):
    for i in range(len(lst2)):
        if lst2[i] not in lst1:
            lst3.append(lst2[i])
        
    return lst3

def union(lst1,lst2,lst3):
    uni=lst1
    for i in range(len(lst2)):
        if lst2[i] not in lst1:
            uni.append(lst2[i])
    for i in range(len(lst3)):
        if lst3[i] not in lst1:
            uni.append(lst3[i])
    return uni


lstcric=[]
lstbad=[]
lstfoot=[]
inter=[]
inter2=[]
b=[]
f=[]
bc=[]
fb=[]
bf=[]
fc=[]
print("cricket:",listinput(lstcric))
print("Badminton:",listinput(lstbad))
print("Football:",listinput(lstfoot))
print("Student who play both cricket and badminton:",intersection(lstcric,lstbad,inter))
print("Student who play both cricket and football:",intersection(lstcric,lstfoot,inter2))
print("Students who donot play cricket",difference(lstcric,lstbad,b)," ",difference(lstcric,lstfoot,f))
print("Students who donot play badminton",difference(lstbad,lstcric,bc)," ",difference(lstbad,lstfoot,fb))
print("Students who donot play football",difference(lstfoot,lstbad,bf)," ",difference(lstfoot,lstcric,fc))
print("Union of all sets:",union(lstcric,lstbad,lstfoot))
