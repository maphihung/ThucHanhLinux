#bai4.py

class Khoa:
	
	def __init__(self,maKhoa,tenKhoa):
		self.maKhoa = maKhoa
		self.tenKhoa = tenKhoa
		
	def setMaKhoa(self,ma):
		self.maKhoa = ma
	def setTenKhoa(self,ten):
		self.tenKhoa = ten
	def getMaKhoa(self,ma):
		self.maKhoa = ma
	def getTenKhoa(self,ten):
		self.tenKhoa = ten
	
	def xuat(self):
		print self.maKhoa," - ",self.tenKhoa