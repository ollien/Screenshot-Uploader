import threading
import os
import time
import random
import ftputil
from termcolor import colored,cprint
class checkThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.new=[]
		self.check=[]
		self.checked=False
		self.i=0
	def run(self):
		self.new=self.check=os.listdir("Path/To/Screenshots/Folder")
		while True:
			if self.checked==False:
				self.check=os.listdir("Path/To/Screenshots/Folder")
				#print "check ",self.check
				self.checked=True
				
			elif self.checked==True:
				for item in self.check:
					if item not in self.new:
						print item
						print "FOUND A NEW ITEM!!!!!"
						self.new.append(item)
						upload=uploadThread(str(item))
						upload.start()
						break
						break
					else:
						self.i+=1
						#print "failed ",self.i
				self.checked=False
				self.new=os.listdir("Path/To/Screenshots/Folder")
				time.sleep(3)
class uploadThread(threading.Thread):
	def __init__(self,filepath):
		print "UPLOADING 'MUDDAFUCKA"
		threading.Thread.__init__(self)
		self.ftp=ftputil.FTPHost('ftp.server.ip.here','FTPUserNameHere','FTPPasswordHere')
		self.chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		self.usedFile=open('usedScreenshotIds.txt','ab+')
		self.usedFile.seek(0,0)
		self.i=0
		self.fileName=""
		self.filepath=filepath
		print self.filepath
		self.url=""
	def run(self):
		while self.i<5:
			self.fileName=self.fileName+random.choice(self.chars)
			self.i+=1
		if self.fileName+"\n" in self.usedFile.readlines():
			self.usedFile.seek(0,0)
			print self.fileName," has already been used!"
			ftp.close()
		else:
			self.usedFile.seek(0,0)
			self.usedFile.write(self.fileName+"\n")
			print "using ",self.fileName
			print "now uploading ",
			print self.fileName
			print self.filepath
			self.ftp.upload("Path/To/Screenshots/Folder/"+self.filepath,self.fileName+'.png','b')
			self.url='http://myWebsite.com/'+self.fileName+'.png'
			cprint(self.url,"green",None)
			os.system("echo '"+self.url+"'|pbcopy")
			self.ftp.close()

checkT=checkThread()
checkT.start()
