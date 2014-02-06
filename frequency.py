'''
Calculate frequency of each term in all of the tweets
frq = [# of occurrences of the term in all tweets] / [# of occurrences of ALL terms in all tweets]
'''

import sys
import re
import json


'''
Build list of tweet text
'''
def getTweets( tweets_fp ):
    tweets_lst = []

    #Go through every line
    for line in tweets_fp:
        data = json.loads( line )

        #Grab text
        if "text" in data.keys():
            text = data["text"]
            tweets_lst.append(text)
            
    return tweets_lst


'''
Determine the frequency of each word across all of the tweets
'''
def countTerms( tweets_lst ):
    termCounts = {}
    count = 0.0
    masterCount = 0.0

    # Go through each tweet in the list
    for tweet in tweets_lst: 
        words = tweet.split()

        # And every word in that tweet
        for word in words:
            if word in termCounts:
                termCounts[word] += 1
            else:
                termCounts[word] = 1

    #Count the total number of terms across all of the tweets
    for term in termCounts:
        masterCount += termCounts[term]

    # Print out frequency for each term
    for term in termCounts.keys():
        print term + " " + str(termCounts[term]/masterCount)



def main():
    # Read in file with list of tweets
    #tweet_file = open(sys.argv[2])
    tweet_file = open( "./output.txt" )
    
    # Extract the tweets from the file
    tweets = getTweets(tweet_file)

    # Count the frequency of each term in each tweet across all tweets
    countTerms( tweets )


if __name__ == '__main__':
    main()

