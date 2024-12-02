# part A
def linear(lst,n,key):  # Linear search
    for i in range(n):
        if(lst[i]==key):
            return 1
    return -1
        
def sentinal(lst,n,key):   #sentinal search
    lst.append(key)
    for i in range(n+1):
        if(lst[i]==key and i<n):
            return 1
    return -1

lst1=[]
n=int(input("Enter the number of students:"))
print("Enter roll no for linear search and sentinal search")
for i in range(n):
    s=int(input("Enter the roll no:"))
    lst1.append(s)
print("Result of linear and sentinal search")
while(True):
    c=int(input("Enter your choice 1 or 2:"))
    if(c==1):
        print("End of program.")
        break
    elif(c==2):
        
        key=int(input("Enter the roll no to be searched:"))
        result1=linear(lst1,n,key)
        print("Result by linear search operation:")
        if(result1==1):
            print("Student has attended the training program.")
        else:
            print("Student has not attended the training program.")

        result2=sentinal(lst1,n,key)
        print("Result by sentinal search operation:")
        if(result2==1):
            print("Student has attended the training program.")
        else:
            print("Student has not attended the training program.")
    else:
        print("Invalid choice!")
#part B
def binary(lst,n,key):  #binary search
    for i in range(n):
        s=0
        e=n-1
        mid=(s+e)/2
        if(key==lst[i]):
            return 1
        elif (key<lst[i]):
         e=mid-1
        else:
            s=mid+1
    return -1

def fibonacci(lst,n,key):   #Fibonacci search
    f0=0
    f1=1
    f2=1
    start=-1
    while(f2<n):
        f0=f1
        f1=f2
        f2=f0+f1

    while(f2>1):
        for i in range(n):
            if(lst[i]<key):
                f2=f1
                f1=f0
                f0=f2-f1
                start=i
            elif(lst[i]>key):
                f2=f0
                f1=f1-f0
                f0=f2-f1
            else:
                return 1
    return -1

lst2=[]
n=int(input("Enter the number of students:"))
print("Enter roll no for binary search and fibonacci search in sorted order:")
for i in range(n):
    s=int(input("Enter the roll no:"))
    lst2.append(s)

print("Rsult of binary and fibonacci search")
while(True):
    c=int(input("Enter your choice 1 or 2:"))
    if(c==1):
        print("End of program.")
        break
    elif(c==2):
        key=int(input("Enter the roll no to be searched:"))
        result3=binary(lst2,n,key)
        print("Result by binary search search operation:")
        if(result3==1):
            print("Student has attended the training program.")
        else:
            print("Student has not attended the training program.")

        result4=fibonacci(lst2,n,key)
        print("Result by fibonacci search search operation:")
        if(result4==1):
            print("Student has attended the training program.")
        else:
            print("Student has not attended the training program.")
    else:
        print("Invalid choice!")






