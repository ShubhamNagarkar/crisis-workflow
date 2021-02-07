#!/usr/bin/env python3
import nltk
from nltk.corpus import stopwords
from pathlib import Path
import pandas as pd
import re
import argparse

def preprocess(path):
    """
    Reads tweets.csv file and removes urls, hashtags, punctuations, stopwords
    :return: processed and clean dataframe
    """
    df = pd.read_csv(path)
    # Removing URL mentions
    df['tweet_text']=df['tweet_text'].apply(lambda x:' '.join(re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", x).split()))
    # Removing Hashtags
    df['tweet_text']=df['tweet_text'].apply(lambda x:' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x).split()))

    # Removing stop words
    stop = stopwords.words('english')
    df['tweet_text']=df['tweet_text'].apply(lambda x:' '.join([word for word in x.split() if word not in (stop)]))
    # Removing punctuations
    df['tweet_text']=df['tweet_text'].str.replace('[^\w\s]','')
    
    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', help='Enter path to the csv file to pre-process')
    parser.add_argument('--o', help='Enter path to the output csv file')
    args = parser.parse_args()
    ip_csv = args.i
    op_csv = args.o
    df = preprocess(ip_csv)
    df.to_csv(op_csv, mode='w', index=False, header=False)
    