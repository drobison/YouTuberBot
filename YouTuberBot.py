#! /usr/bin/Python
import praw
from util import success, warn, log, fail, special, bluelog

### Uncomment to debug
import logging
#logging.basicConfig(level=logging.DEBUG)

### Main program execution path
def YouTuberBot():
	OpenConfigFile()
	global r 
	r = LoginToReddit()
	SearchSubredditForKeywords("test", ['test', 'hello'])



### Opens a config file that contains configuration settings.
def OpenConfigFile():
	with open ('datafile.inf', 'r') as myfile:
		datafile_lines=myfile.readlines()
		return datafile_lines



### Login to reddit
def LoginToReddit():
	datafile_lines = OpenConfigFile()
	r = praw.Reddit("LearnRedditAPI - Alpha .1")
	USERNAME = datafile_lines[0].strip()
	PASSWORD = datafile_lines[1].strip()
	Trying = True
	while Trying:
		try:
			r.login(USERNAME, PASSWORD)
			success("LOGGED IN")
			Trying = False
			return r
		except praw.errors.InvalidUserPass:
			fail("WRONG USERNAME OR PASSWORD")
			exit()
		except Exception as e:
		  fail("%s"%e)
		  time.sleep(5)



def SearchSubredditForKeywords(subredditName, keyWords):

	already_done = []

	#Starting with a single subreddit.  This may later be changed to look at all comments 
	subreddit = r.get_subreddit(subredditName)
	for submission in subreddit.get_hot(limit=10):
		op_text = submission.selftext.encode('ascii', 'ignore').lower()
		success(op_text)
        has_keyWords = any(string in op_text for string in keyWords)
        # Test if it contains a PRAW-related question
        if submission.id not in already_done and has_keyWords:
            msg = '[Keyword found](%s)' % submission.short_link
            success(msg)
            already_done.append(submission.id)
    


if __name__ == "__main__":
	YouTuberBot()
