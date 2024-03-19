import requests
from bs4 import BeautifulSoup

def crawl_print_url(url):
    """
    Crawls the given URL and prints all the href links found on the page.

    Args:
        url (str): The URL to crawl.

    Returns:
        None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        href = link.get('href')
        print(href)

def crawl_print_adress(url):
    """
    Crawls the given URL and prints all urls starting with '/adresse/' 
    found in the HTML.

    Args:
        url (str): The URL to crawl.

    Returns:
        None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for link in soup.find_all('a'):
        href = link.get('href')
        try:
            if href.startswith('/adresse/'):
                print(href)
        except:
            pass

def crawl_save_adress(url, filename):
    """
    Crawls the given URL, extracts addresses from the HTML content, and saves them to a file.

    Args:
        url (str): The URL to crawl.
        filename (str): The name of the file to save the addresses to.

    Returns:
        None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    with open(filename, 'w') as file:
        for link in soup.find_all('a'):
            href = link.get('href')
            try:
                if href.startswith('/adresse/'):
                    file.write('https://www.boligsiden.dk' + href + '\n')
            except:
                pass

def looping_adress_crawler(url, filename, num_pages=1):
    """
    Crawls through the given URL and extracts addresses from the web pages.
    
    Args:
        url (str): The base URL to crawl.
        filename (str): The name of the file to save the extracted addresses.
        num_pages (int): The number of pages to crawl. Default is 1.
    
    Returns:
        None
    """
    with open(filename, 'w') as file:
        for page in range(1, num_pages+1):
            response = requests.get(f'{url}{page}')
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a'):
                href = link.get('href')
                try:
                    if href.startswith('/adresse/'):
                        file.write('https://www.boligsiden.dk' + href + '\n')
                except:
                    pass

if __name__ == '__main__':
    crawl_print_url('https://www.boligsiden.dk/tilsalg?page=1')
    # crawl_print_adress('https://www.boligsiden.dk/tilsalg?page=1')
    # crawl_save_adress('https://www.boligsiden.dk/tilsalg?page=1', 'adress.txt')
    # looping_adress_crawler('https://www.boligsiden.dk/tilsalg?page=', 'adress.txt')