import pandas as pd
from os import listdir

def process():
    filenames = listdir('/Users/junwei/Desktop/tap2023_dsaidde/section1/data')
    files = [filename for filename in filenames if filename.endswith('.csv')]
    for f in files:
        print(f)
        df = pd.read_csv('/Users/junwei/Desktop/tap2023_dsaidde/section1/data/' + f)
        df.dropna(subset=['name'], inplace=True)
        df['price'] = df['price'].astype(float)
        df['first_name'] = [x.split(' ')[0] for x in df['name']]
        df['last_name'] = [x.split(' ')[1] for x in df['name']]
        df['above_100'] = df['price'] > 100
        df.to_csv('/Users/junwei/Desktop/tap2023_dsaidde/section1/processed/processed_' + f, index=False)
