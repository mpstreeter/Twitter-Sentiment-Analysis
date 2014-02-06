'''
Calculates and prints the sentiment for each tweet in the tweets file
'''


import sys

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

'''
Calculate sentiment score for each tweet and print it
'''
def calcSentiment( tweets_fp, scores ):

    #For each tweet, calculate the sentiment score 
    for line in tweets_fp:
        words = line.split()
        score = 0

        # Tweet sentiment score = sum of sentiment scores for each sentiment word in tweet
        for word in words:
            if word in scores:
                score = score + scores[word]

        print score


def main():
    # Read in files: sentiment words, list of tweets
    #sent_file = open(sys.argv[1])
    sent_file = open( "./AFINN-111.txt" )
    #tweet_file = open(sys.argv[2])
    tweet_file = open( "./output.txt" )

    # Make dictionary of sentiment words -> sentiment scores
    scores = makeDir(sent_file)

    # Calculate the sentiment for each tweet in the tweets file
    calcSentiment(tweet_file, scores)

if __name__ == '__main__':
    main()
