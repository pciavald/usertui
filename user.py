import sys
import os
import subprocess

def keyboard(t):
	with t.cbreak():
		while(True):
			key = t.inkey()
			if key == 'q':
				sys.exit()

class User:

	def __init__(self, name, active, uid, gid, gecos, home, sh):
		self.name	= name
		self.active	= active
		self.uid	= uid
		self.gid	= gid
		self.groups	= self.getGroups()
		self.gecos	= gecos
		self.home	= home
		self.sh		= sh

	def isAdmin(self):
		if "sudo" in self.groups:
			return True
		elif "root" in self.groups:
			return True
		return False

	def isActive(self):
		if self.active == 'x':
			return "yes"
		elif self.active == '*':
			return "no"
		elif self.active == "*NP*":
			return "NIS"
		else:
			return self.active

	def getGroups(self):
		groups = "groups {}".format(self.name)
		ps = subprocess.Popen(groups.split(), stdout=subprocess.PIPE)
		return ps.communicate()[0].split(": ")[1] #25
