n=int(input("Enter No : "))

if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("No Is not Prime!!")
            break
        else:
            print("No Is  Prime!!")