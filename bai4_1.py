#ba4_1

from SinhVien import *
from Khoa import *
#-------------------------------------------------
#them danh sach sv
l=[]
sv = SinhVien("57131597","Ma Phi Hung","57")
l.append(sv)
sv = SinhVien("0002","Lee Bum","58")
l.append(sv)
sv = SinhVien("0003","Tran Cung","57")
l.append(sv)
sv = SinhVien("0004","Ly Hoa","58")
l.append(sv)
sv = SinhVien("0005","Quang Tri","59")
l.append(sv)
#------------------------------------------------
#in danh sach sv
size = len(l) #lay do dai danh sach sv
i = 0
print "Danh sach SV:------------------- "
while i < size:
	l[i].xuat()
	i = i+1
print "\n"
#------------------------------------------------
#them cac khoa
lk=[]
k = Khoa("56","Khoa 56 CNTT")
lk.append(k)
k = Khoa("57","Khoa 57 CNTT")
lk.append(k)
k = Khoa("58","Khoa 58 CNTT")
lk.append(k)
k = Khoa("59","Khoa 59 CNTT")
lk.append(k)
#------------------------------------------------
#in danh sach khoa
size = len(lk) #lay do dai danh sach khoa
i = 0
print "Danh sach cac khoa:------------- "
while i < size:
	lk[i].xuat()
	i = i+1
print "\n"
#------------------------------------------------
#Bai 4_2
size = len(l) #lay do dai danh sach sv
i = 0

print "Danh sach SV khoa 57:----------- "
while i < size:
	if l[i].getKhoa()=="57":
		l[i].xuat()
	i = i + 1
