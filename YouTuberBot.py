#! /usr/bin/Python
import praw
from util import success, warn, log, fail, special, bluelog


with open ('datafile.inf', 'r') as myfile:
	datafile_lines=myfile.readlines()

### Login
r = praw.Reddit("YouTuberBot - Alpha .1")
USERNAME = datafile_lines[0].strip()
PASSWORD = datafile_lines[1].strip()
Trying = True
while Trying:
	try:
		r.login(USERNAME, PASSWORD)
		success("LOGGED IN")
		Trying = False
	except praw.errors.InvalidUserPass:
		fail("WRONG USERNAME OR PASSWORD")
		exit()
	except Exception as e:
	  fail("%s"%e)
	  time.sleep(5)