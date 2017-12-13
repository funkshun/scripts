#!/usr/bin/python

import praw
import datetime
from random import randint
from subprocess import call
import requests
import shutil

def main():
    bot = praw.Reddit(client_id = 'Ht5mHlCE67S48g',
        client_secret = 'b1i2MBVzYFa0x7tgcBIhUbZYpCE',
        user_agent = 'linux:com.scripts.karma-vis:v0.0.1 (by /u/Deklyned)',
        username = 'Deklyned',
        password = 'elvIS!@34')

    allsubreddit= bot.subreddit('wallpaper')

    for submission in allsubreddit.top(limit = 50):
        val = randint(0, 50)
        if(val == 26):
            url = submission.url
            ext = get_extension(url)
            filename = "img." + ext
            response = requests.get(url, stream=True)
            with open('filename', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            call(["feh --bg-fill ~/scripts/general/" + filename])
            del response

    
def get_date(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

def get_extension(url):
    dots = 0;
    ext = ""
    for char in url:
        if(char == '.'):
            dots = dots + 1
        if(dots == 3):
            ext = ext + char
if __name__ == "__main__":
    main()
