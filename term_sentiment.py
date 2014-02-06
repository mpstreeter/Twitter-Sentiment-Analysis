import sys


'''
Create dictionary of words in sentiments file: Word --> score
'''
def makeSentsDict(sentiments_fp):
    scores = {} 
    for line in sentiments_fp:
        term, score  = line.split("\t")  
        scores[term] = int(score)  
    
    return scores

'''
Create dictionary of tweets: Tweet --> calculated score
'''
def makeTweetsDict(tweets_fp, sentsDict):
    tweetsDict = {}
    
    for line in tweets_fp:
        words = line.split()
        score = 0

        #Calculate sentiment of this tweet
        for word in words:
            if word in sentsDict:
                score = score + sentsDict[word]

        #Add to dictionary
        tweetsDict[line] = score
        
    return tweetsDict

'''
Calculate sentiment for words not in sentiment file
'''
def calcNewSents(sents_fp, sents_dict, tweets_dict):
    newSentsDict = {}
    
    for line in tweets_dict.keys():
        words = line.split()
        score = 0
        
        for word in words:
            if word not in sents_dict:
                newSentsDict[word] = calcWordSentiment(tweets_dict, word)
                print word + " " + str(newSentsDict[word])

'''
Aggregate sentiment for a term: 1/(# relevant tweets) * [sum of sentiment scores for each of those relevant tweets]
'''
def calcWordSentiment(tweetsDict, word):
    count = 0
    sumSent = 0

    for tweet in tweetsDict:
        if word in tweet:
            count = count + 1
            sumSent = sumSent + tweetsDict[tweet]
            
    score = (1.0/count)*(sumSent)

    return score


def main():
    # Read in files: sentiment words, list of tweets
    #sent_file = open(sys.argv[1])
    sent_file = open( "./AFINN-111.txt" )
    #tweet_file = open(sys.argv[2])
    tweet_file = open( "./output.txt" )
    
    # Make dictionaries out of the two files
    sentsDict = makeSentsDict(sent_file)
    tweetsDict = makeTweetsDict(tweet_file, sentsDict)

    # Calculate sentiment of words not in dictionary
    calcNewSents(sent_file, sentsDict, tweetsDict)

if __name__ == '__main__':
    main()


'''
Notes:
'''

#Sentiment file has list of new sentiments to assign scores
#Tweet file has relevant tweets
#Using Afinn

#Aggregate sentiment for a term: 1/(# relevant tweets) * [sum of sentiment scores for each of those relevant tweets]

#Sentiment score for each tweet based on sentiments file

#make dictionary: tweets --> sentiment score

#walk through each tweet, for every word NOT in the sentiment file:
    #find all of the tweets in tweet file that talk about that topic. grab from dict the sentiment scores from those tweets

    #calculate aggregate sentiment for the new term. store in new term/score dict.

    #print term/score dict



