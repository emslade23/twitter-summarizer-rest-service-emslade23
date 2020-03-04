# References: https://code-maven.com/create-images-with-python-pil-pillow

import datetime
import time
import threading
import subprocess
import os
import shutil
from flask import Flask, render_template, request, send_file


import globalProcesses as gp
from getTweets import userTweets

shutil.copy('keys', 'keys.py')
from keys import *

app = Flask(__name__)


@app.route("/")
def getTweets():
    return "<h1>Welcome to Lizzy's API!</h1>"

@app.route("/tweetVideo", methods=['GET'])
def getTweetVideo():
    twitterHandle = '@elonmusk'
    tweetNumber = 10
    if 'handle' in request.args:
        twitterHandle = request.args['handle']
        gp.twitterHandles.append(twitterHandle)
        if 'tweetNumber' in request.args:
            tweetNumber = int(request.args['tweetNumber'])
            gp.numberOfTweetsArray.append(request.args['tweetNumber'])
        else: 
            gp.numberOfTweetsArray.append('10')
    else:
        gp.twitterHandles.append('@elonmusk')
        gp.numberOfTweetsArray.append('10')
    
    userTweetsObj = userTweets(consumer_key, consumer_secret, access_token, access_token_secret, twitterHandle, tweetNumber, gp.identifier)
    tasksInfo = {
        'twitterHandle': twitterHandle,
        'tweetNumber': tweetNumber,
        'status': "0% Completed"
    }
    gp.twitterCompletedTasks[gp.identifier] = tasksInfo
    gp.identifier = gp.identifier+1
    threads(userTweetsObj)
    

    print(gp.twitterHandles)
    return tweetVideo(userTweetsObj)


@app.route("/progressUpdate", methods=['GET'])
def progress():
    return render_template('progressUpdate.html', processes = gp.twitterCompletedTasks)

    
def threads(userTweets):
    gp.twitterQueue.put(userTweets)
    worker = threading.Thread(target=userTweets.getTweetDataAndCreateVideo())
    worker.setDaemon(True)
    worker.start()
    return worker
    
def tweetVideo(userTweetsObj):
    while gp.twitterCompletedTasks[userTweetsObj.identifier]['status'] != "100% Complete":
        pass
    gp.twitterCompletedTasks[userTweetsObj.identifier]['status'] = "Video Returned"
    return send_file(userTweetsObj.twitterHandle + str(userTweetsObj.identifier) + '_twitterVid.mp4')

def removeTweetImages():
    for file in os.listdir('.'):
        if file.endswith('.png'):
            os.remove(file)

def removeTweetVids():
    for file in os.listdir('.'):
        if file.endswith('.mp4'):
            os.remove(file)


if __name__ == '__main__':
    gp.init()
    removeTweetImages()
    removeTweetVids()

    # for i in range(len(gp.twitterHandles)):
    #     gp.twitterCompletedTasks[gp.twitterHandles[i]] = "Not Completed"

    # for i in range(0, len(gp.twitterHandles)):
    #     userTweetsObj = userTweets(consumer_key, consumer_secret, access_token, access_token_secret, gp.twitterHandles[i], gp.numberOfTweetsArray[i], gp.directoryNameArray[i])
    #     threads(userTweetsObj)

    app.run(debug=True)