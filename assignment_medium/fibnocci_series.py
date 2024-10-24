# Fibnocci series

n=int(input("please enter the no of fibnocci numbers you want to generate :"))

n1,n2=0,1

fibnocciList=[0,1]

if n==1:
    print(fibnocciList[0:1])
elif n==2:
    print(fibnocciList[0:2])
else:
    i=1
    while i <= n-2:
        temp=n1+n2
        fibnocciList.append(temp)

        n1=n2
        n2=temp

        i+=1
    
    print(fibnocciList)
 