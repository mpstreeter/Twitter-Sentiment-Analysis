'''
Find the U.S. state with the happiest (i.e. most positive) tweets
'''


import sys
from collections import defaultdict
import re
import json

'''
Build dictionary of tweets: U.S. state --> list of tweets from that state
'''
def getUSTweets( tweets_fp ):
    tweets_byState = defaultdict(list)

    # Go through each tweet
    for line in tweets_fp:
        data= json.loads( line )

        # Get location info
        if "place" in data.keys():
            place_info = data["place"]

            if place_info is not None and "country_code" in place_info.keys():
                country_code = place_info["country_code"]
                
                # If tweet is in US
                if country_code == 'US':
                    if "full_name" in place_info.keys():
                        city_state = place_info["full_name"]
                        comma_index = city_state.index( ',' )
                        state = city_state[ comma_index+2: ] #get state

                        # Check to make sure state is actually a state...
                        if len( state ) == 2:            
                            #add tweet to list for that state
                            tweets_byState[state].append( data["text"] )
    
    return tweets_byState



'''
Determine which state is happiest by finding the highest sentiment sum of each state's tweets
'''
def findHappiestState( tweets_byState, sent_file ):
    sent_byState = {}
    for state in tweets_byState:
        sentVal = 0
        for tweet in tweets_byState[state]:
            sentVal += calcSentiment( tweet, sent_file )
        sent_byState[state] = sentVal
            
    sortedStates = sorted( sent_byState, key=sent_byState.get, reverse=True)
    print sortedStates[0]

    
'''
Calculate sentiment score for given tweet and return it
'''
def calcSentiment( tweet, scores ):
    score = 0

    # Tweet sentiment score = sum of sentiment scores for each sentiment word in tweet
    for word in tweet:
        if word in scores:
            score = score + scores[word]

    return score
    

'''
Create dictionary of words in sentiments file
'''
def makeDir( sentiments_fp ):
    
    scores = {} 

    # Build dictionary from file of words -> scores
    for line in sentiments_fp:
        term, score  = line.split("\t")  
        scores[term] = int(score)  

    return scores



def main():
    # Read in files: sentiment words, list of tweets
    #sent_file = open(sys.argv[1])
    sent_file = open( "./AFINN-111.txt" )
    #tweet_file = open(sys.argv[2])
    tweet_file = open( "./output.txt" )

    # Build dictionary of tweets posted in the U.S. 
    tweets = getUSTweets(tweet_file)

    #Find the happiest state (i.e. state with most positive tweet sentiment)
    findHappiestState( tweets, makeDir(sent_file) )

if __name__ == '__main__':
    main()










