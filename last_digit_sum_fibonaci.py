def fibonaci(n):
    list1=[]
    list1.append(0)
    list1.append(1)
    for i in range(2,n+1):
        x=((list1[i-1]+list1[i-2])%10)
        list1.append(x)
    add=(sum(list1)%10)
    return (add)

num=int(input("enter  the number : "))
print(fibonaci(num))
