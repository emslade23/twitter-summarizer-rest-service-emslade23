# Twitter Summarizer Rest Service 
### by Elizabeth Slade

## Routes

this is a flask app.

1. "/": the welcome page
2. "/tweetVideo"
    - adding **"?handle=@elizabeth&tweetNumber=5"** to the end of the URL 
        - **handle** changes the twitter handle
        - **tweetNumber** gives you control over how many tweets you want
3. "/progressUpdate"
    - gives you the current progress of all threads
