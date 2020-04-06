# Twitter Summarizer REST Service 
### by Elizabeth Slade

this is a flask app.

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

