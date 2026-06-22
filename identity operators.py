x=5
if type(x)==int:
    print("True")
else:
    print("False")

y=5.5
if type(y)==str:
    print("True")
else:
    print("False")

z="Saatvik"
if type(z)==str:
    print("True")
else:
    print("False")

#Identity Operators
a=20
b=20
if(a is b):
    print("a and b share the same identity")
else:
    print("a and b do not share the same identity")

b=30
if(a is not b):
    print("True")
else:
    print("False")

i=-50
g=49
if(i is g):
    print("i and g are the same")
else:
    print("i and g are not the same")

if(i is not g):
    print("True")
else:
    print("False")