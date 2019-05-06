grade = [];
s = 0;
for i in range(0,5):
    grade.append(float(input()));
    s = s + grade[i];
print("THAI =",grade[0]);
print("MATH =",grade[1]);
print("ENGLISH =",grade[2]);
print("SCIENCE =",grade[3]);
print("SPORT =",grade[4]);
print("---");
print("GPA =",float(s/5));