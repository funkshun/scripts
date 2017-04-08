#!/usr/bin/python

import praw
import matplotlib
import numpy
import datetime

def main():
    bot = praw.Reddit(client_id = 'Ht5mHlCE67S48g',
        client_secret = 'b1i2MBVzYFa0x7tgcBIhUbZYpCE',
        user_agent = 'linux:com.scripts.karma-vis:v0.0.1 (by /u/Deklyned)',
        username = 'Deklyned',
        password = 'elvIS!@34')

    allsubreddit= bot.subreddit('all')

    for submission in allsubreddit.top('all', limit = 50):
        print (get_date(submission))
    
def get_date(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

if __name__ == "__main__":
    main()
