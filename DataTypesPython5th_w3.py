x = "String"
print(type(x))
x = 1
print(type(x))
x = 1.0
print(type(x))
x = 1j
print(type(x))
x = ["List01", "List02", "List03"]
#["List11", "List12", "List13"]["List21", "List22", "List23"]
print(type(x))
x = ("List01", "List02", "List03")
#("List11", "List12", "List13")("List21", "List22", "List23")
print(type(x))
x = range(6)
print(type(x))
x = {"name":"Bereket", "age":"What?", "wt": 75, "ht": 1.75}
#print(x)
print(type(x))
x = {"List01", "List02", "List03"}
#{"List11", "List12", "List13"}{"List21", "List22", "List23"}
print(type(x))
x = frozenset({"List01", "List02", "List03"})
#,{"List11", "List12", "List13"},{"List21", "List22", "List23"})
#print(x)
print(type(x))
x = True
print(type(x))
x = b"Hello"
#print(x)
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
#print(x)
print(type(x))
x = None
print(type(x))