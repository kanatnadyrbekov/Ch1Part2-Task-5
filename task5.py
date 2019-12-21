a = int(input("Students in Class1:"))
b = int(input("Students in Class2:"))
c = int(input("Students in Class3:"))
# Desks = x1,x2,x3
x1 = a / 2
if x1 % 2 == 0:
    print(x1)
else:
    print(round(x1))  
x2 = b / 2
if x2 % 2 == 0:
    print(x2)
else:
    print(round(x2))    
x3 = c / 2
if x3 % 2 == 0:
    print(x3)
else:
    print(round(x3))    
result = x1 + x2 + x3
print(round(result))
