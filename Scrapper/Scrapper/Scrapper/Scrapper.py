import urllib.request
from bs4 import BeautifulSoup

j = 2
while j < 20:
   
    url = 'https://www.opineo.pl/produkty/eobuwie-pl/'+str(j)+',data#opinie'
    print("url:", url)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    soup = BeautifulSoup(response, 'html.parser')
   
    print("\n\n\n\n\n", soup)

    rating_star = soup.findAll("span", {"class": "review_badge pos"})
    text_review = soup.findAll("div", {"class": "revz_txt small prod"})

    i = 0

    while i < 15:
        print("rating_star: ", rating_star[i].getText().replace("/ 5",""))
        print("text_review: ", text_review[i].getText().replace("                    ",""))
        i += 1
   
    j += 1
   