def Is_set_or_not(n,i):
    if (n&(1<<i))!=0:
        return True
    else:
        return False
    
n=int(input("Enter the number: "))
i=int(input("Enter the bit position to check: "))
if Is_set_or_not(n,i):
    print(f"The {i}th bit is set.")
else:
    print(f"The {i}th bit is not set.")