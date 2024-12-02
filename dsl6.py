
def getlst(lst,n):
    for i in range(n):
        a=float(input("Enter percentage:"))
        lst.append(a)
    print(lst)

def bubble(lst,n):
    #temp=0
    for i in range(n):
        for j in range(n-1):
            if(lst[j]>lst[j+1]):
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
    print(lst)

def selection(lst,n):
    #temp=0
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(lst[j]<lst[min]):
                min=j
        if(min!=i):
            temp=lst[min]
            lst[min]=lst[i]
            lst[i]=temp
    print(lst)

n=int(input("Enter total number students:"))
lst=[]
print("Unsorted list of percentage of students:")
getlst(lst,n)
print("Sorted list after sorting using bubble sort:")
bubble(lst,n)
print("Sorted list after sorting using selection sort:")
selection(lst,n)