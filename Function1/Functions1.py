# Write a function which takes a dictionary as an arguement and returns two lists
# one for keys and other for values

def funca(**kwargs):
	c=list(kwargs.keys())
	d=list(kwargs.values())
	return c, d

a,b = funca(a="apple", b="orange")
print(a)
print(b)
