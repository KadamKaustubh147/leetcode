import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # return dataframe not series

    # this below code won't work cuz len(tweets['content']) is the number of rows
    # To check the character length of the string inside each individual row, you need to use pandas' built-in string accessor .str.len().
    results = tweets[tweets['content'].str.len() > 15]
    return results[['tweet_id']]