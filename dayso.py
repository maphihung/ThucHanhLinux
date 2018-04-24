#dayso.py

def indayso(n):
	i = 1
	while i <= n:
		print " ",i
		i = i + 1

def tinhtong(n):
	i = 1
	tong = 0
	while i <= n:
		if i%2 == 0:
			tong = tong + i
	print "tong day so chan tu 1 den ",n," la: ",tong

n = input("n = ")
indayso(n)
tinhtong(n)