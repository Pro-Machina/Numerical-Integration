print "TRAPAZOIDAL METHOD"
print ""

a = float(raw_input("Enter a: "))
b = float(raw_input("Enter b: "))
n = int(raw_input("Enter n: "))

h = (b - a)/n

f = []
i = 0

while i <= (n):
	x = float(raw_input("Enter f%s: " % i))
	f.append(x)
	i += 1
	pass

result2 = 0
j = 1

while j <= (n - 1):
	result2 += f[j]
	j += 1
	pass

result2 *= 2

result1 = f[0] + f[n]

result = (h/2)*(result1 + result2)

print "The value of integral is: %s" % result