#sohoc.py

def Cong(a,b):
	print a," + ",b," = ",a+b
	
def Tru(a,b):
	print a," - ",b," = ",a-b

def Nhan(a,b):
	print a," * ",b," = ",a*b
	
def Chia(a,b):
	if b==0:
		print "Phep tinh khong hop le!"
	else:
		print a," / ",b," = ",a/b

def LuyThua(a,b):
	i = 1
	ketqua = 1
	while i <= b:
		ketqua = ketqua*a
		i = i + 1
	print a,"^",b," = ",ketqua

def LayDu(a,b):
	print a,"%",b," = ",a%b
	

a = input("a = ")
b = input("b = ")
Cong(a,b)
Nhan(a,b)
Chia(a,b)
Tru(a,b)
LuyThua(a,b)
LayDu(a,b)