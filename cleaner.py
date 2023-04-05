import pandas as pd
import re
from cleantext import clean


class Cleaner:

    def __init__(self):

        try:
            import pandas as pd
        except:
            print('Pandas not installed. Try pip install pandas')

        try:
            import re
        except:
            print('re not installed. Try pip install re')
        
        try:
            from cleantext import clean
        except:
            print('cleantext not installed. Try pip install clean-text')



    def file_cleaner(files, del_column=None):

        n = 0

        for file in files:

            df = pd.read_csv(file)

            list_cols = del_column

            for col in list_cols:

                if col in df.columns:

                    del df[col]

            df['text'] = df['text'].str.lower()

            df['text'] = df['text'].apply(lambda x: re.sub('[^a-zA-z0-9\s]', '', x))
            df['text'] = df['text'].apply(lambda x: re.sub('[0-9]', '', x))
            df['text'] = df['text'].apply(lambda x: clean(x, no_emoji=True))

            n += 1
            df.to_csv('set-tweets-' + str(n) + '.csv', index=False)


    def file_merger(file_list):

        df = pd.DataFrame()

        for file in file_list:

            data = pd.read_csv(file)
            df = pd.concat([df, data], axis=0)
        
        df.to_csv('merged.csv')

