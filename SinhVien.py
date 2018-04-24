#bai4.py

class SinhVien:
	
	def __init__(self,mssv,hoTen,khoa):
		self.mssv = mssv
		self.hoTen = hoTen
		self.khoa = khoa
	
	def setTen(self,ten):
		self.hoTen = ten
		
	def setMSSv(self,mssv):
		self.mssv = mssv
	
	def setKhoa(self,khoa):
		self.khoa = khoa
		
	def getTen(self):
		return self.hoTen
		
	def getMSSV(self):
		return self.mssv
		
	def getKhoa(self):
		return self.khoa
	
	def xuat(self):
		print self.mssv," - ",self.hoTen," - ",self.khoa