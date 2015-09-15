from blessed import Terminal
from user import keyboard, User
from tabulate import tabulate

t = Terminal()

def getInfo():
	users = []
	users_file = open("/etc/passwd").readlines()
	for user_input in users_file:
		user_input = user_input.split(":")
		name	= user_input[0]
		active	= user_input[1]
		uid		= user_input[2]
		gid		= user_input[3]
		gecos	= user_input[4]
		home	= user_input[5]
		sh		= user_input[6]
		u = User(name, active, uid, gid, gecos, home, sh)
		users.append(u)
	return users

def display(users):
	tab = []
	for user in users:
		u = []
		u.append(user.name) # TODO isadmin bold
		u.append(user.isActive())
		u.append(user.uid)
		u.append(user.gid)
		u.append(user.groups if len(user.groups) <= 25 else user.groups[:25] + "..")
		u.append(user.gecos)
		u.append(user.home)
		u.append(user.sh)
		tab.append(u)
	headers = ["Name", "Active", "UID", "GID", "Groups", "Description", "Home", "Shell"]
	with t.location(0, 2):
		print tabulate(tab, headers)
	with t.location(t.width - 16, t.height - 1):
		print 'Press q to quit'

def groupsFilter(users):

	groups = []
	for user in users:
		for group in user.groups.rstrip().split(' '):
			if group not in groups:
				groups.append(group)
	groups.sort()
	for group in groups:
		print group

with t.fullscreen():

	users = getInfo()
	display(users)
	#groupsFilter(users)

	keyboard(t)























