name = [];
year = [];
gender = [];
n = int(input());
x = Scanner.next();
y = Scanner.next()
if n==0:
    pass;
else:
    for i in range(0,n):
        name.append(input());
        year.append(2017 - int(input()));
        gender.append(input());
    print("--Customers Information--");
    for j in range(0,n):
        print(name[j] + " (age : ",year[j],")",sep="");