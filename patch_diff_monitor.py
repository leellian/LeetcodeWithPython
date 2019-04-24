#-*- encoding: UTF-8 -*-

import os
import hashlib
import sys
from sendpopo import SendMsg

FLAG = ['NEW','MOD','SAME']
MD5_FILE = 'MD5.json'
CHECK_PATH = 'C:\\Users\\yuyujie\Desktop\\facebook\\2019.04.19'

class MD5Check(object):
	def __init__(self,path):
		self._working_directory = path
		self._MD5_dict = {}
		self._compare_MD5_result = {}
		self._output = {f:[] for f in FLAG}
		self._files_path = []
		
	def _MD5Generate(self):
		for file in self._files_path:
			with open(file,'r') as f:
				md5 = hashlib.md5()
				while True:
					t = f.read(8096)
					if not t:
						break
					md5.update(t)
				self._MD5_dict.setdefault(file,md5.hexdigest())
	
	def _MD5Compare(self):
		for file in self._files_path:
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
	
	def _GetFiles(self):
		for root,_,files in os.walk(self._working_directory):
			for file in files:
				#TODO filter files not needed
				self._files_path.append(os.path.join(root,file))
	
	def _SaveMD5ToFile(self):
		with open(MD5_FILE,"w") as f:
			json.dump(self._MD5_dict,f)
	
	def _LoadMD5FromFile(self):
		with open(MD5_FILE,"r") as f:
			self._MD5_dict = json.load(f)
	
	def UpdateMD5File(self):
		self._GetFiles()
		self._MD5Generate()
		self._SaveMD5ToFile()
	
	def MD5CompareResultOutput(self):
		self._GetFiles()
		self._LoadMD5FromFile()
		self._MD5Compare()
		for key,val in self._compare_MD5_result.iteritems():
			self._output[val].append(key)
		return self._output
	
def main():
	checker = MD5Check(CHECK_PATH)
	check_result = []
	if len(sys.argv) == 2: # need to update md5 file
		checker.UpdateMD5File()
		SendMsg('yuyujie@corp.netease.com',"已更新所有文件的MD5值","#color#120-10-0")
		return
	else:
		check_result = checker.MD5CompareResultOutput()
	# ['NEW','MOD','SAME']
	
	SendMsg('yuyujie@corp.netease.com',diff_result,"#color#120-10-0")
	
if __name__ == "__main__":
	main()
	#TODO 第一次需要计算MD5的值，存入文件。后续根据文件中的MD5值进行对比。
	# 如果有NEW报出来后，再更新文件中的MD5值