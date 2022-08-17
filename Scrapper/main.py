import urllib.request
from bs4 import BeautifulSoup
from modules import http_request
from modules import functions
from modules  import sqlite
import os
import sqlite3
import re
import sys
from dataclasses import replace

# Number of comments on a single page
number_of_comments_in_one_page = 15

url = 'https://www.website-name.com/'

cur_dir = os.path.dirname(__file__)
db_path = os.path.join(cur_dir, '..\Share\db\db.sqlite')

class main():
    @staticmethod
    def run():

        http_request_obj = http_request.http_connect_class()
        functions_obj = functions.funcions_class()
        db_obj = sqlite.db_sql_lite_class()
        conn = db_obj.open_database(db_path)   
  
        # We start with the page: 
        j = 1
        soup = http_request_obj.get_html(url)
        last_page = http_request_obj.get_lastpage(soup)
       
        while j <= last_page:
            url = site_url+product_url+str(j)+end_url
            try:
                soup = http_request_obj.get_html(url)
                          
            except Exception as e:
                print("******** Something went wrong:", e)
                pass
           
            rating_star_list = soup.findAll('span', {'class': re.compile("^review_badge*")})
            text_review_list = soup.findAll("div", {"class": "revz_txt"})
            
            #print("rating_star_list:", rating_star_list)
            #print("text_review_list", text_review_list)

            i = 0
            for  row in  rating_star_list:

                try:
                    rating_star = row.getText().replace("/ 5","")   #.replace(".0","")
                    text_review = text_review_list[i].getText()
                    text_review = functions_obj.clean_unnecessary_characters(text_review)
                        
                    db_obj.save_data_in_database(conn, db_path, rating_star, text_review)
                    i += 1

                except  Exception as e:
                    print("******** Something went wrong:", e)
                    pass
                
            # Footer
            print(j,"/",last_page, "=>" ,url)
            j += 1
                  
        print("\nDONE")
            
main.run()
