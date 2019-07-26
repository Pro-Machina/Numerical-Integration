print "SIMPSON 1/3 RULE"
print ""

a = float(raw_input("Enter a: "))
b = float(raw_input("Enter b: "))
n = int(raw_input("Enter n: "))

h = (b - a)/(2*n)

f = []
i = 0

while i <= (2*n):
	x = float(raw_input("Enter f%s: " % i))
	f.append(x)
	i += 1
	pass

s0 = 0
s1 = 0
s2 = 0

j = 1

while j <= (2*n - 1):
	s1 += f[j]
	j += 2
	pass

k = 2

while k <= (2*n - 2):
	s2 += f[k]
	k += 2
	pass

s0 = f[0] + f[2*n]

result = (s0 + 4*s1 + 2*s2)*(h/3)

print "The value of Integral is: %s" % result