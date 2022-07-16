for a in range(1,10):
    if a%2==0:
        print(a,'\t',sep='',end='')
for b in range(1,100):
    if b%2==0:
        if b%20>=10:
            print(b,'\t',sep='',end='')
            if (b-10)%10==0:
                print()