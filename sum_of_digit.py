n=abs(int(input("enter number: ")))
total=0
a=0
while n>0:
    a=n%10
    n=n//10
    total=total+a
print("sum of digit is :",total)

 
 