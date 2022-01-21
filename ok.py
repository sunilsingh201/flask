def armstrong(n):
    sum=0
    copy= n
    power = len(str(n))
    while(n>0):
        digit = n%10
        sum =sum+digit**power
        n=n//10
    if copy==sum:
        print(f"{copy} is an armstrong number ")
        return "True"
    else:
        print(f"{copy} is not a armstrong number ")
        return "False"

armstrong(153)