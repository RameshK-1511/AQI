# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import time
import requests
import sys


def get_data_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10): # month will be 1,2 in html it is 01,02
                # https://en.tutiempo.net/climate/02-2013/ws-431980.html
                url = 'http://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month,year)
            else:
                url = 'http://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month,year)
                
            texts=requests.get(url) # We need to get text data in html
            text_utf=texts.text.encode('utf-8')  # As the text would be having special char so encoding
        
            if not os.path.exists("Data/html_data/{}".format(year)): # Check if folder exists or not
                os.makedirs("Data/html_data/{}".format(year))    # create folder 
            with open("Data/html_data/{}/{}.html".format(year,month),"wb") as output: # write text data 
                output.write(text_utf)
            
        sys.stdout.flush()
        
if __name__ == "__main__":
    start_time = time.time()
    get_data_html()
    stop_time = time.time() - start_time
    print("Total time taken: {}".format(stop_time))