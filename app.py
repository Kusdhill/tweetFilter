# Fresh filtered tweets

import twitter
import json
import keys
import os
import string

# Initialize API
api = twitter.Api(consumer_key=keys.consumer_key,
					consumer_secret=keys.consumer_secret,
					access_token_key=keys.access_token_key,
					access_token_secret=keys.access_token_secret)

user = keys.user


def main():
	
	if(not os.path.isfile('./posts.JSON')):
		print("No posts file")
		print("Getting max_id")
		max_id = get_first_max_id()
		print("Creating posts file")
		get_posts(max_id)
	else:
		print("Restarting posts.JSON and results.txt files")
		os.remove('./posts.JSON')
		os.remove('./results.txt')
		print("Getting max_id")
		max_id = get_first_max_id()
		print("Creating posts file, allow a few minutes")
		get_posts(max_id)		

	
	print("Filtering posts")
	filter_posts()


# API allows a limited number of statuses, so we have to do some finagling to get around it. Using max ID's works. Not the cleanest solution
# but it will suffice.
def get_first_max_id():

	# verify that all of your keys are correct
	#print(api.VerifyCredentials())

	newest_status = api.GetUserTimeline(screen_name=user, count=1)
	
	max_id = newest_status[0].id_str
	
	# Begin posts.JSON with open bracket for JSON readability
	with open('posts.JSON', 'a') as outfile:
		outfile.write('[')

	return(max_id)


# Pass max ID's to get post. Max ID's change based on where we are in reading the tweets.
def get_posts(max_id):
	statuses = api.GetUserTimeline(screen_name=user, max_id=max_id)

	counter=0
	for status in statuses:
		counter+=1

		if counter==20:
			max_id = status.id_str
			get_posts(max_id)

		with open('posts.JSON', 'a') as outfile:
			json.dump({'created_at':status.created_at, 'id_str':status.id_str, 'text':status.text}, outfile)
			outfile.write(','+'\n')
		

# Filters results into results.txt based on filter terms
def filter_posts():

	# Remove last brace and comma from posts.JSON
	with open('posts.JSON', 'rb+') as outfile:
		outfile.seek(-1,os.SEEK_END)
		outfile.truncate()
		outfile.seek(-1,os.SEEK_END)
		outfile.truncate()

	# End posts.JSON with closing bracket for JSON readability
	with open('posts.JSON', 'a') as outfile:	
		outfile.write(']')

	# Add desired filter terms here
	Filter = keys.Filter
	tweet_list = []

	with open('posts.JSON') as data_file:    
		data = json.load(data_file)

	for tweet in data:
		tweet_list.append(tweet)

	for i in range(0, len(tweet_list)):
		for word in tweet_list[i]['text'].split():
			for filter_term in Filter:
				if word.lower()==filter_term:

					with open('results.txt', 'a') as outfile:
						outfile.write(tweet_list[i]['text'].encode('utf8'))
						outfile.write('\n')

	print("Complete! Go check results.txt for the results!")

if __name__ == '__main__':
	main()