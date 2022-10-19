x = str(4)
print(type(x))
x = "Bereket"
print(type(x))

y = 5.0
print(type(y))
y = int(5)
print(type(y))
y = int(6.0)
print(y)
print(type(y))

#Camel Case
myCamelCase = "My Camel Case Variable Declaration Standard --------> myCamelCase"
print(myCamelCase)
#Pascal Case
MyPascalCase  = "My Pascal Case Variable Declarations Standard ------> MyPascalCase"
print(MyPascalCase)
#Snake Case
my_snake_case = "My Snake Case Variable Declarations Standard -------> my_snake_case"
print(my_snake_case)


x, y, z = "Val 1", "Val 2",  "Val 3"
print(x)
print(y)
print(z)

x  = y = z = "The Same Value"

print(x+" On X")
print(y+" On Y")
print(z+" On Z")

myValues = "Python", "is", "Awesome I guess"
print(myValues)
x, y, z = myValues
print(x, y, z)
print(x+y+z)


myGlobalVariable = "My Global Variable is always Global"
def myFirstPythonFunction():
    global myGlobalVariable
    myGlobalVariable = "My Global Var is Local Now"
    print("My First Python Function")
    print("Local "+myGlobalVariable)
    print("Python functions looks like c++ functions")

myFirstPythonFunction()
print("Global "+myGlobalVariable)