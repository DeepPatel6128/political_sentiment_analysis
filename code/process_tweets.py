import re
import pandas as pd
import numpy as np
from textblob import TextBlob
from time import sleep
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



# if __name__ == '__main__':
#     #get the tweets
#     tweets = pd.read_csv(r'C:\Users\31020\OneDrive\Desktop\final_year_project\code\bharatSolanki.csv')
#     print(df[0])

tweets = pd.read_csv(r'C:\Users\31020\OneDrive\Desktop\final_year_project\code\bharatSolanki.csv')
df = pd.DataFrame(tweets, columns = ['Date','Tweet'])
df['Date'] = pd.to_datetime(df['Date']).dt.date
print(df.head(10))