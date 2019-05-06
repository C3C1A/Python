x = [];
n = int(input());
if n==0:
    pass;
else:
    for i in range(0,n):
        x.append(int(input()));
    x.sort();
    x.reverse();
    for z in x:
        print(z);