from crawler import looping_adress_crawler
from scraper import create_data_frame

if __name__ == '__main__':
    url = 'https://www.boligsiden.dk/tilsalg?page='
    filename = 'addresses.txt'
    looping_adress_crawler(url, filename)
    df = create_data_frame(filename)
    print(df)