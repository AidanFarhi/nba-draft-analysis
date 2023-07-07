import pandas as pd
from time import sleep

BASE_URL = 'https://www.basketball-reference.com/draft'
DRAFT_PREFIX = 'NBA_'


def main():
    years = list(pd.read_html(f'{BASE_URL}')[0].Draft)
    for year in years[0]:
        sleep(.5)
        data = pd.read_html(f'{BASE_URL}/{DRAFT_PREFIX}{year}.html')
        print(data)

if __name__ == '__main__':
    main()
