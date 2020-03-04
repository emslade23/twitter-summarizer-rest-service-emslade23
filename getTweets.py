import tweepy
import requests
import PIL
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import subprocess
import time
import globalProcesses 
import os
import shutil

class userTweets:
    
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, twitterHandle, numberOfTweets, identifier):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.twitterHandle = twitterHandle
        self.numberOfTweets = numberOfTweets
        self.textOfTweets = []
        self.imagesOfTweets = []
        self.identifier = identifier

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


    def getTweetDataAndCreateVideo(self):
        self.getTweetData()
        self.createImagesofTweets()
        self.convertImagestoVideo()
        globalProcesses.twitterQueue.task_done()
        print("\n A thread for " + self.twitterHandle + " has completed.")
        
    def getTweetData(self):
        # post is the entire element from api, tweet is the plain text tweet with links
        for post in tweepy.Cursor(self.api.user_timeline, screen_name=self.twitterHandle, tweet_mode="extended", include_entities=True).items(self.numberOfTweets):
            if( hasattr(post,'extended_entities')):
                for element in post.extended_entities['media']:
                    if(element['type'] == 'photo'):
                        self.imagesOfTweets.append(element['media_url_https'])
            else:
                self.imagesOfTweets.append('0')
            self.textOfTweets.append(post.full_text)
        print("Tweets: ", self.textOfTweets)
    
    def insertNewLines(self, tweet):
        if len(tweet) < 60:
            return tweet
        revisedTweet = ""
        
        for i in range(60, len(tweet), 60):
            revisedTweet = revisedTweet + tweet[i-60:i] + '\n' 
            if len(tweet)-i < 60:
                revisedTweet = revisedTweet + tweet[i:len(tweet)]
        return revisedTweet
    
    def createImagesofTweets(self):
        counter = 0
        indexArray = 0
        font = ImageFont.truetype("arial.ttf", 15)
        for tweet in self.textOfTweets:
            revisedTweet = self.insertNewLines(tweet)
            
            img = Image.new('RGB', (500, 500), color = (0, 0, 0))
            d = ImageDraw.Draw(img)
            d.text((20,10), self.twitterHandle+":\n\n"+ revisedTweet, fill=(255,255,255), font=font)

            
            img.save(self.twitterHandle+str(self.identifier)+'_frame'+str(counter)+'.png')
            counter += 1
            
            if self.imagesOfTweets[indexArray] != '0':
                response = requests.get(self.imagesOfTweets[indexArray])
                img = Image.open(BytesIO(response.content))
                img.save(self.twitterHandle+str(self.identifier)+'frame'+str(counter)+'.png')
                counter += 1
                indexArray += 1
        
        globalProcesses.twitterCompletedTasks[self.identifier]['status'] = "50% Complete"

    
    def convertImagestoVideo(self):
        naming = self.twitterHandle + str(self.identifier)
        os.system('ffmpeg -r .3 -f image2 -s 1920x1080 -i ' + naming + '_frame%d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p ' + naming + '_twitterVid.mp4')
        globalProcesses.twitterCompletedTasks[self.identifier]['status'] = "100% Complete"
