#given array of integers,perform atmost k operation so that

j=0
n=list(map(int,input().split(" ")))
print(n)
k=int(input("enter the no"))
for j in range (k):
    '''arr=max(n)//2
    n.remove(max(n))
    n.append(arr)
    print(n)
print(sum(n))'''
    max_value=max(n)
    i=n.index(max_value)
    n.remove(max_value)
    m=max_value//2
    n.insert(i,m)
print(sum(n))


