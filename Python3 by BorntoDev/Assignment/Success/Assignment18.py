n = int(input());
j = n-1;
x = 1;
if n==0:
    pass;
else:
    for i in range(0,n):
        print(" "*j + "*"*x);
        x = x+2;
        j = j-1;