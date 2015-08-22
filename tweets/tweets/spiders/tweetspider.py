# Alex Smith
# MIDS W205
# Assignment #4

import scrapy                           # import the scrapy module to create the spider and scrape the web
from tweets.items import TweetsItem     # import the TweetsItem type from items.py file
import os                               # import the os module to help determine if the CSV file already exists

CSV_FILE_NAME = "WC2015.csv"            # name of CSV file

class TweetSpider(scrapy.Spider):
    name = "tweet_spider"
    allowed_domains = ["twitter.com"]
    start_urls = [
        'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-06%20until%3A2015-06-07&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-07%20until%3A2015-06-08&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-08%20until%3A2015-06-09&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-09%20until%3A2015-06-10&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-10%20until%3A2015-06-11&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-11%20until%3A2015-06-12&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-12%20until%3A2015-06-13&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-13%20until%3A2015-06-14&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-14%20until%3A2015-06-15&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-15%20until%3A2015-06-16&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-16%20until%3A2015-06-17&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-17%20until%3A2015-06-18&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-18%20until%3A2015-06-19&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-19%20until%3A2015-06-20&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-20%20until%3A2015-06-21&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-21%20until%3A2015-06-22&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-22%20until%3A2015-06-23&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-23%20until%3A2015-06-24&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-24%20until%3A2015-06-25&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-25%20until%3A2015-06-26&src=typd&vertical=default&f=tweets', \
        'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-26%20until%3A2015-06-27&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-27%20until%3A2015-06-28&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-28%20until%3A2015-06-29&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-29%20until%3A2015-06-30&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-06-30%20until%3A2015-07-01&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-07-01%20until%3A2015-07-02&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-07-02%20until%3A2015-07-03&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-07-03%20until%3A2015-07-04&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-07-04%20until%3A2015-07-05&src=typd&vertical=default&f=tweets', 'https://twitter.com/search?q=%23FIFAWWC%20%23CAN%20OR%20%23USA%20OR%20%23MEX%20OR%20%23CRC%20OR%20%23COL%20OR%20%23ECU%20OR%20%23BRA%20OR%20%23NOR%20OR%20%23SWE%20OR%20%23ENG%20OR%20%23NED%20OR%20%23GER%20OR%20%23FRA%20OR%20%23SUI%20OR%20%23ESP%20OR%20%23CIV%20OR%20%23NGA%20OR%20%23CMR%20OR%20%23CHN%20OR%20%23THA%20OR%20%23KOR%20OR%20%23JPN%20OR%20%23AUS%20OR%20%23NZL%20lang%3Aen%20since%3A2015-07-05%20until%3A2015-07-06&src=typd&vertical=default&f=tweets'
    ]


    def parse(self, response):
        """method to parse a webpage based on the start URLs"""

        # create the xpath to identify all the tweets on the page
        hxs = scrapy.selector.HtmlXPathSelector(response)
        tweets = hxs.select("//div[contains(@class,'js-stream-tweet')]")

        # create a items list to hold all the scraped information
        items = []

        # iterate through tweets on the page
        for tweet in tweets:

            # set item to the TweetsItem class defined in items.py file
            item = TweetsItem()

            # scrape each field and store in the appropriate item
            # we store the first item of the list as a string
            item["tweet_id"] = str(tweet.select("@data-tweet-id").extract()[0])
            item["screen_name"] = str(tweet.select("@data-screen-name").extract()[0])

            # store the date time information in a single variable
            date_time = tweet.select("div[@class='content']/div/small/a/@title").extract()
            date_and_time = TweetSpider().splitDateTime(date_time)

            # add the distinct date and time values to the appropriate fields
            item["date"] = date_and_time[1]
            item["time"] = date_and_time[0]

            # use distinct methods to find all the text and hashtags in the tweet and
            # concatenate appropriately before storing into the item type
            item["text"] = TweetSpider().findText(tweet)
            item["hashtag"] = TweetSpider().findTags(tweet)

            # append each tweet's information to the list
            items.append(item)

            # write each item to the CSV file
            TweetSpider().writetoCSV(item)

    def splitDateTime(self, date_time):
        """method to split a date_time input into two outputs to store the date and the time separately"""

        # convert the list object to a string so that we can split it
        date_time = str(date_time[0])

        # split the date_time by the hyphen, "-"
        date_and_time = date_time.split(" - ")

        # return the date_and_time
        return date_and_time

    def findText(self, tweet):
        """method to find all the text for a given tweet"""

        # extract all the text
        all_words = tweet.select("div[@class='content']/p/text()").extract()

        # begin an empty string to store the text
        tweet_text = ""

        # loop through all the text and concatenate the values
        for word in all_words:
            tweet_text = tweet_text + str(word)

        # return the tweet text
        return tweet_text

    def findTags(self,tweet):
        """method to find all the hashtags for a given tweet"""

        # extract all the hashtags
        all_tags = tweet.select("div[@class='content']/p/a/b/strong/text()").extract()

        # concatenate the list of hashtags, separated by spaces, so we can
        # store it in a single CSV field

        # begin an empty string to store the hashtags
        hashtags = ""

        # loop through all the hashtags and concatenate them, add a space
        # before if its not the first hashtags
        for hashtag in all_tags:
            if hashtags == "":
                hashtags = hashtags + hashtag
            else:
                hashtags = hashtags + " " + hashtag

        # return the concatenated hashtags
        return str(hashtags)

    def writetoCSV(self,tweet):
        """method to write the items scraped to a CSV file"""

        # create a new CSV file for storing the tweet DataFrame
        # if the file does not already exist
        if os.path.exists(CSV_FILE_NAME) == False:
            newfile = open(CSV_FILE_NAME, "w")
        # if it does exist, open it to append to it
        else:
            newfile = open(CSV_FILE_NAME, "a")

        # print a new line to begin each tweet on a separate row
        newfile.write("\n")

        # because dictionaries are unordered, print each element
        # distinctly rather than using a for loop
        row = tweet["tweet_id"] + ", " + tweet["screen_name"] + ", " + tweet["date"] + ", " + tweet["time"] + ", " + "\"" + tweet["text"] + "\"" + ", " + tweet["hashtag"]
        newfile.write(row)

        # close the file for neatness
        newfile.close()


        # code to download the entire page
        #filename = "TEST" + '.html'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
