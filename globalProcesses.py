import queue
global twitterQueue 
global twitterCompletedTasks
global twitterHandles
global numberOfTweetsArray
global identifier

def init():
    global twitterQueue 
    global twitterCompletedTasks
    global twitterHandles
    global numberOfTweetsArray
    global identifier
    
    twitterQueue = queue.Queue(maxsize=40)
    twitterCompletedTasks = {}
    twitterHandles = []
    numberOfTweetsArray = []

    identifier = 5
