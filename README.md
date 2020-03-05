# Twitter Summarizer REST Service 
### by Elizabeth Slade

## System Setup
1. git clone this repo
2. Get a virtual environment.
        
        source env/bin/activate
        
3. Install requirements. 
        
        pip install -r requirements.txt 
        
4. Run local server
       
        python3 getVideo.py 

## Routes

this is a flask app.

1. "/": the welcome page
2. "/tweetVideo"
    - adding **"?handle=@elizabeth&tweetNumber=5"** to the end of the URL 
        - **handle** changes the twitter handle
        - **tweetNumber** gives you control over how many tweets you want
3. "/progressUpdate"
    - gives you the current progress of all threads
