import sys
import numpy as np
import pandas as pd
import praw
from praw import Reddit
from utils.constants import POST_FIELDS

def initialize_reddit_connection(client_id, client_secret, user_agent) -> Reddit:
    """Establishes a connection to the Reddit API using PRAW."""
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)
        print("Successfully connected to Reddit!")
        return reddit
    except Exception as error:
        print(f"Error connecting to Reddit: {error}")
        sys.exit(1)

def fetch_top_posts(reddit_instance: Reddit, subreddit_name: str, time_filter: str, limit=None):
    """Fetches top posts from a subreddit based on specified filters."""
    subreddit = reddit_instance.subreddit(subreddit_name)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    post_data = []
    for post in posts:
        post_details = vars(post)
        filtered_post = {key: post_details[key] for key in POST_FIELDS}
        post_data.append(filtered_post)

    return post_data

def clean_post_data(posts_df: pd.DataFrame):
    """Transforms and cleans the extracted posts data."""
    posts_df['created_utc'] = pd.to_datetime(posts_df['created_utc'], unit='s')
    posts_df['over_18'] = np.where(posts_df['over_18'], True, False)
    posts_df['author'] = posts_df['author'].astype(str)
    edited_default = posts_df['edited'].mode()
    posts_df['edited'] = np.where(posts_df['edited'].isin([True, False]),
                                  posts_df['edited'], edited_default).astype(bool)
    posts_df['num_comments'] = posts_df['num_comments'].astype(int)
    posts_df['score'] = posts_df['score'].astype(int)
    posts_df['title'] = posts_df['title'].astype(str)

    return posts_df

def save_data_to_csv(data: pd.DataFrame, file_path: str):
    """Saves the transformed data to a CSV file."""
    data.to_csv(file_path, index=False)
