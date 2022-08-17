import urllib.request
from bs4 import BeautifulSoup

class http_connect_class:
    # Downloads all HTML code
    def get_html(self, url):
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response, 'html.parser')
        return soup
    
    # The last page in this section
    def get_lastpage(self, soup):
        last_page = soup.findAll("span", {"class": "pagi_page"})
        return int(last_page[-1].getText())
        
