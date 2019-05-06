point = int(input());
if point>=90:
    print("A");
elif point>=85 and point<=89:
    print("B+");
elif point>=80 and point<=84:
    print("B");
elif point>=75 and point<=79:
    print("C+");
elif point>=70 and point<=74:
    print("C");
elif point>=65 and point<=69:
    print("D+");
elif point>=60 and point<=64:
    print("D");
elif point<60:
    print("F");