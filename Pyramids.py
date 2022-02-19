# Printing half Pyramid normal
x= "*"
d = int(input('Enter the value of star:'))
n = 0
for n in range(1,d+1):
    a = n * x
    n +=1
    print(a)

# Printing Half Pyramid opposite
y= "x"
c = int(input('Enter the value of star:'))
m = 0
for m in range(c,0,-1):
    b = m * y
    m -=1
    print(b)

