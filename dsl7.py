def insertion(lst,n):
    for i in range(1,n):
        key=lst[i]
        j=i-1
        while(j>=0 and lst[j]>key):
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=key
    print(lst)

def shell(lst,n):
    gap=n//2
    while gap>0:
        j=gap
        while j<n:
            i=j-gap
            while i>=0:
                if lst[i+gap]>lst[i]:
                    break
            else:
                temp=lst[i+gap]
                lst[i+gap]=lst[i]
                lst[i]=temp
                i=i-gap
            j+=1
        gap=gap//2
    print(lst)
    

def input_lst(lst,n):
    for i in range(n):
        a=float(input())
        lst.append(a)
    print(lst)

n=int(input("Enter total number of students:"))
lst=[]
print("Enter the percentage of SE students:")
input_lst(lst,n)
print("Sorting by insertion sort:")
insertion(lst,n)
print("Sorting by shell sort:")
shell(lst,n)

