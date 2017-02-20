# tweetFilter
I wrote tweetFilter as a quick way to search a Twitter user's tweets without having to scroll down far into the user's timeline. In its current state, it's basically a glorified ctrl+f using the Twitter API, but it's still a neat tool to play with nonetheless.

# Setup
For first time setup you should download this repo and make sure you have the python wrapper for the Twitter API. This is listed in the requirements.txt folder so to install you can just type the following in your terminal:

```
pip install -r requirements.txt
```

Next, you'll have to <a href="https://dev.twitter.com/oauth/overview/application-owner-access-tokens">generate tokens</a> for authorization. You will need a twitter account for this.

Once you have all the tokens, place the appropriate keys in the keys.py folder. It's blank initially, so make sure you fill it out. You can also edit which user's tweets you want to filter here. They do have to be a public user.

# Usage
You can run the app with:

```
python app.py
```

If a posts.JSON file exists (it will after you run the app the first time), any subsequent time you run the app the program will restart a new posts.JSON file and a new results.txt file. If this is a hassle, you can alter the main() function to do whatever you want. You can edit what filter terms you want in the filter_posts() function.

Enjoy!