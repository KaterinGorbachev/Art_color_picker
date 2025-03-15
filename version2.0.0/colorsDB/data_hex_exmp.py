

myVar1 = 255
myVar2 = [ 0xFF, 0xFF01FF, 17253, 0x0101, 9928, 0xFFFFFF ]

print(myVar1)
print(f"Hex print: {myVar2[1]:06X}")  #X grande x small

#print(f"#{myVar1:06x}")

query = f"INSERT INTO usuarios3 VALUES({myVar2[0]}, {0xFFFFFF}, {myVar2[2]}, {myVar2[3]}, {myVar2[4]})"
print(query)