fileOpen = open("test.txt","w");
fileOpen.write("ABCDEFG");
fileOpen.close();

fileRead = open("test.txt","r");
x = fileRead.read(5);
print(x);
fileRead.close();