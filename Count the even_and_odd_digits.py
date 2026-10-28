num=int(input("Enter number: "))
even=0
odd=0
while num>0:
    a=num%10
    if a%2==0:
        even+=1
    elif a%2!=0:
        odd+=1

    num=num//10
print(even)
print(odd)
