import praw
import twitter
import io
import json
import sys

#function for chars not supported in windows
def convert(t):
    with io.StringIO() as fd:
        for c in t:
            dummy = fd.write(c if ord(c) < 0x10000 else '')
            return fd.getvalue()
        
#function that provides a recap of the /r/Everton subreddit for the given time window

async def recap(self, window):
    reddit = praw.Reddit(client_id='',
                 client_secret='',
                 user_agent='',
                 username='',
                 password='')
    subreddit = reddit.subreddit('Everton')
    await self.say("Top 5 posts to /r/%s for the last %s\n"%(subreddit.display_name, window))
    for submission in subreddit.top(time_filter=window, limit=5):
        await self.say("%s | Score: %s \n%s"%(submission.title, submission.score, submission.shortlink))
    
#function that provides a list of the top items that mention "Everton" for the given time window in /r/soccer
async def soccerSearch(self, window):
    reddit = praw.Reddit(client_id='',
                 client_secret='',
                 user_agent='Script Test 0.1.0 (by /u/Lawlington)',
                 username='',
                 password='')
    subreddit = reddit.subreddit('Soccer')
    await self.say("Top 5 posts to /r/%s about Everton for the last %s\n"%(subreddit.display_name, window))
    for submission in subreddit.search('Everton', 'top', time_filter=window, limit=5):
        await self.say("%s\n%s"%(submission.title, submission.shortlink))
#general subreddit search command
async def searchSR(self, searchtype, time, sr_name, keyword):
    reddit = praw.Reddit(client_id='',
                 client_secret='',
                 user_agent='Script Test 0.1.0 (by /u/Lawlington)',
                 username='',
                 password='')
    subreddit = reddit.subreddit("%s"%(sr_name))
    await self.say("%s 5 posts to /r/%s about %s for the last %s\n"%(searchtype, sr_name, keyword, time))
    for submission in subreddit.search(keyword, searchtype, time_filter=time, limit=5):
        await self.say("%s\n%s"%(submission.title, submission.shortlink))

async def getUsage(self, cmd):

    if(cmd=="search"):
        await self.say("General search tool.\nUsage: !search <Search Type> <Timeframe> <Subreddit> <Keyword>\n\t<Search Type> is either Hot/Top/Best/New/Controversial\n\t<Timeframe> is either Hour/Day/Week/Month/Year/All \n\t<Subreddit> is the subreddit you want to search. If you want to search all, enter 'all' \n\t<Keyword> is the string you want to search for.\n")
    elif(cmd=="recap"):
        await self.say("Recap of /r/Everton for the last <time>\nUsage: !recap <time>\n\t<time> is either Hour/Day/Week/Month/Year/All")
    elif(cmd=="soccersearch"):
        await self.say("Searches /r/soccer for top posts for 'Everton' for the last <time>\nUsage: !soccersearch <time>\n\t<time> is either Hour/Day/Week/Month/Year/All")
    else:
        await self.say("Available functions: search, recap, soccersearch")
##
##    
##    d = {
##            "search" : 
##            "recap" : 
##            "soccersearch" : 
##        }
##    try:
##        d[cmd]
##    except KeyError:

        
#function that gets tweets from list on twitter
##todo: log last tweet, start pulling from there when new tweets come in. Need a data structure that keeps track of when items are posted into discord.
async def getTweets(self):
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode+1), 0xfffd)
    api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')
    tweetList = api.GetListTimeline(list_id='', count='5', include_rts='false', include_entities='false')
    await self.say("Getting the latest 5 tweets from Everton Transfer list")
    for i in tweetList:
            try:
                x = i.media[0].expanded_url
            except TypeError:
                await self.say("@%s on Twitter: \n%s\n "%(i.user.screen_name, i.text.translate(non_bmp_map)))
                ##await self.say("%s\n"%(i.text.translate(non_bmp_map)))

            else:
##                await self.say("@%s on Twitter: \n%s \n%s"%(i.user.screen_name, i.text.translate(non_bmp_map), x))
                await self.say("%s\n %s\n"%(i.text.translate(non_bmp_map), x))

                            
