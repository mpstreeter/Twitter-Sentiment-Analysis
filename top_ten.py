'''
Determines the top ten most popular hash tags in given set of tweets
'''


import sys
from collections import defaultdict
import re
import json

'''
Build list of hashtags for all of the tweets
'''
def getAllTags( tweets_fp ):
    tags_lst = []

    # Go through each tweet
    for line in tweets_fp:
        data = json.loads( line )
        if "entities" in data.keys():
            entities = data["entities"]
            if "hashtags" in entities.keys():
                hashtags = entities["hashtags"]

                #Check if there are any hashtags
                if len(hashtags) > 0:
                    for dict in hashtags:
                        text = dict["text"]
                        tags_lst.append(text)
    return tags_lst 


'''
Count number of occurrences for each tag
'''
def countTags( tags_lst ):
    tagCount = defaultdict(int)
    for tag in tags_lst:
        tagCount[tag] += 1.0

    return tagCount

'''
Print the top ten hashtags
'''
def printTopTen( tagCount ):
    count = 10

    # Sort list then print the first 10
    for w in sorted( tagCount, key=tagCount.get, reverse=True):
        print w + " " + str(tagCount[w]) #Print hashtag with count
        count = count - 1;
        if count == 0: #Stop when you've printed 10
            break


def main():
    # Read in file of tweets in JSON format
    #tweet_file = open(sys.argv[1])
    tweet_file = open( "./output.txt" )

    # Build list of hashtags from all of the tweets
    tags = getAllTags(tweet_file)

    # Count the number of occurrences for each tag
    tagCount = countTags( tags )

    # Print the top ten hashtags
    printTopTen( tagCount )


if __name__ == '__main__':
    main()










