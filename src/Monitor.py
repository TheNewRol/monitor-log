import os
import time

class Monitor:

	# Constructor
	def __init__(self,val):
		self.json= val
		self.logfile = open("./webscssl.error.log","r")

	def getLine(self):
		return self.logfile

	def readLine(self):
		self.logfile.seek(0, os.SEEK_END)

    	# start infinite loop
		while True:
			# read last line of file
			line = self.logfile.readline()
			# sleep if file hasn't been updated
			if not line:
				time.sleep(0.1)
				continue

			yield line	