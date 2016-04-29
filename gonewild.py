# REQUIRES AUTHENTICATION
# This script archives the URL's automatically
import praw

def writeToFile(string):
    print "Let's remember this link!"
    with open("gonewild_logs.txt", "a") as myfile:
        myfile.write(string + "\n")
        print "Wrote to file"

UA = 'New Bot by u/meepcanon'
r = praw.Reddit(UA)
r.login()
cache = []
while True:
    subreddit = r.get_subreddit("gonewild")
    for submission in subreddit.get_new(limit=5000):
        if submission.url not in cache:
            cache.append(submission.url)
            writeToFile(submission.url)
