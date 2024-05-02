import pandas as pd
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk


nltk.download('vader_lexicon')

import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def preprocess_tweet(sen):
    '''Cleans text data up, leaving only 2 or more char long non-stepwords composed of A-Z & a-z only
    in lowercase'''

    sentence = sen.lower()

    # Remove RT
    sentence = re.sub('RT @\w+: ', " ", sentence)

    # Remove special characters
    sentence = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ',
                      sentence)  # When we remove apostrophe from the word "Mark's", the apostrophe is replaced by an empty space. Hence, we are left with single character "s" that we are removing here.

    # Remove multiple spaces
    sentence = re.sub(r'\s+', ' ',
                      sentence)  # Next, we remove all the single characters and replace it by a space which creates multiple spaces in our text. Finally, we remove the multiple spaces from our text as well.

    return sentence
def csv(path: str):
    tweet_list = pd.read_csv(path)
    # Creating new dataframe and new features
    tweet_list_df = pd.DataFrame(tweet_list)
    tweet_list_df = pd.DataFrame(tweet_list_df['text'])
    cleaned_tweets = []

    for tweet in tweet_list_df['text']:
        cleaned_tweet = preprocess_tweet(tweet)
        cleaned_tweets.append(cleaned_tweet)
    tweet_list_df['cleaned'] = pd.DataFrame(cleaned_tweets)
    tweet_list_df[['polarity', 'subjectivity']] = tweet_list_df['cleaned'].apply(
        lambda Text: pd.Series(TextBlob(Text).sentiment))
    for index, row in tweet_list_df['cleaned'].items():
        score = SentimentIntensityAnalyzer().polarity_scores(row)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        comp = score['compound']
        if comp <= -0.05:
            tweet_list_df.loc[index, 'sentiment'] = "negative"
        elif comp >= 0.05:
            tweet_list_df.loc[index, 'sentiment'] = "positive"
        else:
            tweet_list_df.loc[index, 'sentiment'] = "neutral"
        tweet_list_df.loc[index, 'neg'] = neg
        tweet_list_df.loc[index, 'neu'] = neu
        tweet_list_df.loc[index, 'pos'] = pos
        tweet_list_df.loc[index, 'compound'] = comp
        print(tweet_list_df)
        tweet_list_df.to_csv("../c2_sentimentanalysis_output.csv", sep=',', encoding='UTF-8')


csv('../Tweets.csv')



