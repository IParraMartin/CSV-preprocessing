import pandas as pd
import re
from cleantext import clean


def file_cleaner(files):
    n = 0

    for file in files:

        df = pd.read_csv(file)

        list_cols = ['Unnamed: 0', 'created_at', 'edit_history_tweet_ids', 'id', 'withheld']

        for col in list_cols:
            if col in df.columns:
                del df[col]

        df['text'] = df['text'].str.lower()

        # use re to remove punctuation
        df['text'] = df['text'].apply(lambda x: re.sub('[^a-zA-z0-9\s]', '', x))
        df['text'] = df['text'].apply(lambda x: re.sub('[0-9]', '', x))
        df['text'] = df['text'].apply(lambda x: clean(x, no_emoji=True))

        n += 1  
        df.to_csv('set-tweets-' + str(n) + '.csv', index=False)

all_files = []
file_cleaner(all_files)
