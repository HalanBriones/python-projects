#Halan Briones Merino

print("Enter your name: ")
name=input()

print("Enter x value")
xStr=input()

print("Enter y value")
yStr=input()

x=int(xStr)
y=int(yStr)

#print(type(x))
#print(type(y))

total=x+y #sum
diff=x-y #difference
prod=x*y #product
div=x/y #division

print(name, "Your calculation are: ",)
print(xStr +" + "+ yStr+" =",total)
print(xStr +" - "+ yStr+" =",diff)
print(xStr +" * "+ yStr+" =",prod)
print(xStr +" / "+ yStr+" =",div)