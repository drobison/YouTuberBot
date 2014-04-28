#! /usr/bin/Python
import praw, os
from util import success, warn, log, fail, special, bluelog

### Uncomment to debug
import logging
#logging.basicConfig(level=logging.DEBUG)

### Main program execution path
def YouTuberBot():
	OpenConfigFile()
	global r 
	r = LoginToReddit()
	SearchSubredditTitlesForKeywords("test", ['test', 'hello'])



### Opens a config file that contains configuration settings.
def OpenConfigFile():
	### Set root directory to script directory
	abspath = os.path.abspath(__file__)
	dname = os.path.dirname(abspath)
	os.chdir(dname)
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



def SearchSubredditTitlesForKeywords(subredditName, keyWords):

	already_done = []

	#Starting with a single subreddit.  This may later be changed to look at all comments 
	subreddit = r.get_subreddit(subredditName)
	for submission in subreddit.get_hot(limit=10):
		op_text = submission.selftext.encode('ascii', 'ignore').lower()		
		has_keyWords = any(string in op_text for string in keyWords)
		# Test if it contains a PRAW-related question
		if submission.id not in already_done and has_keyWords:
			msg = '[Keyword found](%s)' % submission.short_link
			success(msg)
			already_done.append(submission.id)



def SearchSubredditCommentsForKeywords(subredditName, keyWords):
	### To be implemented
	return


### Posts a reply to a comment
### Input - commentId of comment to reply to, message to reply with
def ReplyToComment(commentId, msg):
	### To be implemented
	return

### Retrieves video information.
### Input - youtube link 
### Output - Metadata for video
def GetVideoInformation(link):
	### To be implemented
	return


### Determines if a comment has already been processed.
### Input - reddit commentId
### Output - bool indicating processed status.
def IsCommentAlreadyProcessed(commentId):
	### To be implemented
	return


if __name__ == "__main__":
	YouTuberBot()
