#!/usr/bin/env python3
"""
Twitter Sentiment Analysis with Real-Time Data
Performs sentiment analysis on Twitter tweets using TextBlob and VADER (NLTK)
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
from termcolor import colored, cprint

# Download required NLTK data
nltk.download('vader_lexicon', quiet=True)
nltk.download('stopwords', quiet=True)

def clean_tweet(tweet):
    """
    Clean and preprocess tweet text:
    - Remove URLs
    - Remove mentions (@user)
    - Remove hashtags
    - Remove special characters
    - Convert to lowercase
    - Tokenize
    - Remove stopwords
    """
    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+', '', tweet)
    # Remove mentions
    tweet = re.sub(r'@\w+', '', tweet)
    # Remove hashtags (keep the text)
    tweet = re.sub(r'#', '', tweet)
    # Remove special characters and numbers
    tweet = re.sub(r'[^A-Za-z\s]', '', tweet)
    # Lowercase
    tweet = tweet.lower()
    # Tokenize
    tokens = tweet.split()
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Join back to string
    return ' '.join(tokens)

def percentage(part, whole):
    """Calculate percentage safely"""
    return 100 * float(part) / float(whole) if whole != 0 else 0

def main():
    """Main function to orchestrate sentiment analysis"""
    print(colored("\n=== Twitter Sentiment Analysis ===", 'cyan', attrs=['bold']))
    
    # Get API credentials from user
    print(colored("\nEnter your Twitter API credentials:", 'yellow'))
    consumerKey = input("Consumer Key: ")
    consumerSecret = input("Consumer Secret: ")
    accessToken = input("Access Token: ")
    accessTokenSecret = input("Access Token Secret: ")

    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)

    # Get search parameters from user
    keyword = input("\nPlease enter keyword or hashtag to search: ")
    try:
        nooftweets = int(input("Enter number of tweets to analyse: "))
    except ValueError:
        print(colored("Invalid input. Using default value of 100.", 'red'))
        nooftweets = 100

    cprint("\nAnalyzing the Tweets...", 'red', attrs=['blink'])

    # Fetch tweets
    try:
        tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang='en', tweet_mode='extended').items(nooftweets)
    except Exception as e:
        print(colored(f"Error fetching tweets: {e}", 'red'))
        return

    # Initialize counters and lists
    pos = 0
    neg = 0
    neu = 0
    polarity = 0
    tweet_list = []
    neu_list = []
    neg_list = []
    pos_list = []

    sia = SentimentIntensityAnalyzer()

    # Process each tweet
    for tweet in tweets:
        # Get full text
        text = tweet.full_text if hasattr(tweet, 'full_text') else tweet.text
        cleaned = clean_tweet(text)
        
        # Skip empty tweets
        if not cleaned.strip():
            continue
        
        tweet_list.append(cleaned)
        
        # Perform sentiment analysis
        analysis = TextBlob(cleaned)
        score = sia.polarity_scores(cleaned)
        polarity += analysis.sentiment.polarity
        
        # Classification using compound score
        if score['compound'] >= 0.05:
            pos_list.append(cleaned)
            pos += 1
        elif score['compound'] <= -0.05:
            neg_list.append(cleaned)
            neg += 1
        else:
            neu_list.append(cleaned)
            neu += 1

    # Calculate percentages
    total = pos + neg + neu
    if total == 0:
        print(colored("No tweets were processed. Please check your search parameters.", 'red'))
        return
    
    pos_p = percentage(pos, total)
    neg_p = percentage(neg, total)
    neu_p = percentage(neu, total)
    polarity_p = percentage(polarity, total)

    pos_p = format(pos_p, '.1f')
    neg_p = format(neg_p, '.1f')
    neu_p = format(neu_p, '.1f')

    # Create DataFrames
    tweet_df = pd.DataFrame(tweet_list, columns=['Tweet'])
    neutral_df = pd.DataFrame(neu_list, columns=['Tweet'])
    negative_df = pd.DataFrame(neg_list, columns=['Tweet'])
    positive_df = pd.DataFrame(pos_list, columns=['Tweet'])

    # Print results
    print(colored("\n=== Analysis Results ===", 'cyan', attrs=['bold']))
    print(f"Total tweets analyzed: {len(tweet_df)}")
    print(f"Positive tweets: {len(positive_df)}")
    print(f"Negative tweets: {len(negative_df)}")
    print(f"Neutral tweets: {len(neutral_df)}")

    # Visualization
    plt.figure(figsize=(12, 8))
    
    # Pie chart
    plt.subplot(2, 1, 1)
    labels = [f'Positive [{pos_p}%]', f'Neutral [{neu_p}%]', f'Negative [{neg_p}%]']
    sizes = [float(pos_p), float(neu_p), float(neg_p)]
    colors = ['green', 'yellow', 'red']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90, shadow=True, autopct='%1.1f%%')
    plt.style.use('default')
    plt.legend(labels, loc='upper left')
    plt.title(f"Sentiment Analysis Result for keyword: {keyword}", fontsize=14, fontweight='bold')
    plt.axis('equal')

    # Bar chart
    plt.subplot(2, 1, 2)
    k1 = [len(positive_df), len(negative_df), len(neutral_df)]
    k2 = ["POSITIVE", "NEGATIVE", "NEUTRAL"]
    c = ["green", "red", "yellow"]
    z = plt.bar(k2, k1, color=c, width=0.4)
    plt.title("Tweet Count Based on Emotion", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Tweets")
    
    # Add emoji labels
    labels_emoji = ['😊', '😠', '😐']
    for rect1, label in zip(z, labels_emoji):
        height = rect1.get_height()
        plt.annotate(label, (rect1.get_x() + rect1.get_width() / 2, height + 0.05), 
                    ha="center", va="bottom", fontsize=25)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\n\nAnalysis cancelled by user.", 'yellow'))
    except Exception as e:
        print(colored(f"\nAn error occurred: {e}", 'red'))
