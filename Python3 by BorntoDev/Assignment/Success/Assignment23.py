n = int(input());
x = [];
if n==0:
    pass;
else:
    for i in range(0,n):
        x.append(int(input()));
    x.reverse();
    for z in x:
        print(z);