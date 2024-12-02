def more_500(lst1,lst2,lst3):
    for i in range(len(lst1)):
        if(lst1[i]>500):
            lst3.append(lst2[i])
    print(lst3)

def less_500(lst1,lst2,lst3):
    for i in range(len(lst1)):
        if(lst1[i]<500):
            lst3.append(lst2[i])
    print(lst3)

def sorted_list(lst):
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if(lst[i]>lst[j]):
                lst[i],lst[j]=lst[j],lst[i]
    print(lst)

def duplicate(lst):
    temp=[]
    for i in lst:
        if i not in temp:
            temp.append(i)     
    print(temp)

n=int(input("Enter the number of books in the library:"))
book_list=[]
cost_list=[]
lst_500m=[]
lst_500l=[]
nonduplicate=[]
for i in range(n):
    book=input("Enter the name of the book:")
    cost=int(input("Enter the the cost of the book:"))
    book_list.append(book)
    cost_list.append(cost)

print("List of book is:",book_list)
print("Cost of books are:",cost_list)
print("Books which costs more than 500:")
more_500(cost_list,book_list,lst_500m)
print("Books which costs less 500:")
less_500(cost_list,book_list,lst_500l)
print("Sorted list of cost is:")
sorted_list(cost_list)
print("List of books after removing duplicate books:")
duplicate(book_list)
