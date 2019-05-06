x = int(input());
y = int(input());
s = int(x+y);
total = int(x-y);
time = int(x*y);
if y!=0:
    div = int(x/y);


print(x,"+",y,"=",s);
print(x,"-",y,"=",total);
print(x,"*",y,"=",time);
if y!=0:
    print(x,"/",y,"=",div);