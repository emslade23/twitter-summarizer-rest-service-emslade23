# Twitter Summarizer REST Service 
### by Elizabeth Slade
## Summary
For this project, I developed an application that allows a user to input a twitter handle, and the number of tweets they would like to see. It is currently online, 
            and multiple users are able to request tweets at a time. I acheived the multiple requests to my API feature using threads. 
            Then, using the Tweepy API, I retreive the tweets from that respective user. I designed this project using object oriented programming and decided it would be best to store
            the tweets in a userTweets object that I could reference throughout my code. After I stored the tweets, I then generated images of all of the tweets using the Pillow library's image feature. Some tweets had text and images which
            needed to be taken into account. After I generated images for the tweets and saved them in a directory, I then used ffmpeg to create a video of the images of tweets. Once the video is generated it gets displayed back on the page for
            the user to see!
            


example call: https://twitter-video-app.herokuapp.com/tweetVideo?handle=@lifemathmoney&tweetNumber=30

## Routes for Heroku Deployment
### Website Link: https://twitter-video-app.herokuapp.com !


1. "/": the welcome page
2. "/tweetVideo": default collects most recent 10 tweets of @elonmusk
    - adding **"?handle=@elonmusk&tweetNumber=30"** to the end of the website link 
        - **handle** changes the twitter handle to @elonmusk
        - **tweetNumber** changes the number of tweets for the video
3. "/progressUpdate"
    - gives you the current progress of all threads



## Local System Setup Instructions
1. git clone this repo
2. Get a virtual environment.
        
        source env/bin/activate
        
3. Install requirements. 
        
        pip install -r requirements.txt 
        
4. Run local server
       
        python3 getVideo.py 

