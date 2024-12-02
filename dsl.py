def average(lst):
    sum=0
    for i in range(len(lst)):
        if(lst[i]!="abs"):
            sum=sum+int(lst[i])
        else:
           pass
    return sum/len(lst)

def maxelement(lst):
    max=0
    for i in range(len(lst)):
        if(lst[i]=="abs"):
            pass
        elif(max < int(lst[i])):
            max=int(lst[i])
    return max

def minelement(lst):
    lst.sort()
    return lst[0]

def abstcount(lst):
    abstno=0
    for i in range(len(lst)):
        if lst[i] == "abs":
            abstno = abstno+1
    return abstno

def frequency(lst):
    max=0
    res= lst[0]
    for i in lst:
        freq=lst.count(i)
        if(freq>max):
            max=freq
            res=i
    return res

n=int(input("Enter total number of students:"))
studentlist=[]
for i in range(n):
    print("\n")
    print("Roll no:"," ", (i+1),":")
    a=input("Enter marks(abs if absent):")
    while(True):
        if(a>="0" and a<="50"):
            break
        elif(a=="abs"):
            break
        else:
            print("Invalid number")
    studentlist.append(a)
print("\n")
print(studentlist)
print("Average:",average(studentlist))
print("Absent no of students:",abstcount(studentlist))
print("Maximum marks:",maxelement(studentlist))
print("Minimum marks:",minelement(studentlist))
print("Most frequency of marks:",frequency(studentlist))














