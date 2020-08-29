import os, requests
from bs4 import BeautifulSoup as bs

url = 'https://xkcd.com'
os.makedirs('./xkcd comics', exist_ok = True)
os.chdir('/xkcd comics')

while not url.endswith('/1800'):  
    """Enter the number of the comics you want the script to stop at.
    The url of the first comic ends with # so the program stops when reach the first comic"""
    print('Downloading the page {}'.format(url))
    res = requests.get(url)
    res.raise_for_status()
    soup = bs(res.text, 'lxml')
    comic = soup.select('#comic img')
    if comic == []:
        print('no comic founded')
    else:
        comic_url = 'http:' + comic [0].get('src')
        res = requests.get(comic_url)
        res.raise_for_status()
        image = open(os.path.basename(comic_url), 'wb')
        for chunk in res.iter_content(10000):
            image.write(chunk)
        image.close()

        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prev_link.get('href')

print('done')
