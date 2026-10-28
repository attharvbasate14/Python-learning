n=abs(int(input("Enter number: ")))
original=n
reverse=0
while n>0:
    a=n%10
    reverse=reverse*10+a
    n=n//10

if original==reverse:
        print("palindrome")
else: print("not palindrome")