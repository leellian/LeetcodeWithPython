#-*- encoding: UTF-8 -*-

import os
import hashlib

FLAG = ['NEW','MOD','SAME']

class MD5Check(object):
	def __init__(self,path):
		self._working_directory = path
		self._MD5_dict = {}
		self._compare_MD5_result = {}
		self.output = {f:[] for f in FLAG}
		self.files_path = []
		
	def MD5Generate(self):
		for file in self.files_path:
			with open(file,'r') as f:
				md5 = hashlib.md5()
				while True:
					t = f.read(8096)
					if not t:
						break
					md5.update(t)
				self._MD5_dict.setdefault(file,md5.hexdigest())
	
	def MD5Compare(self):
		for file in self.files_path:
			self._compare_MD5_result.setdefault(file,FLAG[0])
			if file in self._MD5_dict.keys():
				file_md5 = ''
				original_md5 = self._MD5_dict[file]
				with open(file,'r') as f:
					md5 = hashlib.md5()
					while True:
						t = f.read(8096)
						if not t:
							break
						md5.update(t)
					file_md5 = md5.hexdigest()
				self._compare_MD5_result[file] = FLAG[2] if file_md5==original_md5 else FLAG[1]
	
	def MD5CompareResultOutput(self):
		for key,val in self._compare_MD5_result.iteritems():
			self.output[val].append(key)
	
	def GetFiles(self):
		for root,_,files in os.walk(self._working_directory):
			for file in files:
				#TODO filter files not needed
				self.files_path.append(os.path.join(root,file))
	
def main():
	path = 'C:\\Users\\yuyujie\Desktop\\facebook\\2019.04.19'
	checker = MD5Check(path)
	checker.GetFiles()
	checker.MD5Generate()
	checker.MD5Compare()
	checker.MD5CompareResultOutput()
	print 1
	
if __name__ == "__main__":
	main()
	#TODO 第一次需要计算MD5的值，存入文件。后续根据文件中的MD5值进行对比。
	# 如果有NEW报出来后，再更新文件中的MD5值