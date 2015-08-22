# Alex Smith
# MIDS W205
# Assignment #4

import tweetscrape      # import the module to scrape the tweets using twitter's advanced search
import datetime         # import the datetime module to help limit the range of tweets
import archiveindex     # import the module to archive the data in a whoosh index

CSV_FILE_NAME = "tweets\WC2015.csv"    # name of CSV file

# main hashtag & all team hashtags
QUERY = "#FIFAWWC"
QUERY_LIST = ["#CAN","#USA","#MEX","#CRC","#COL","#ECU","#BRA","#NOR","#SWE","#ENG","#NED","#GER","#FRA","#SUI","#ESP","#CIV","#NGA","#CMR","#CHN","#THA","#KOR","#JPN","#AUS","#NZL"]

# set the range for the tweets we'll be collecting
BEGIN = datetime.date(2015, 6, 6)
END = datetime.date(2015, 7, 5)

# run the tweet scrape function to generate the URLs for the query
# copy and paste the list into the tweetspider.py start_URLs field
tweetscrape.TweetScrape().advancedSearch(QUERY, QUERY_LIST, BEGIN, END)

# archive the tweets with whoosh and run four sample queries
archiveindex.ArchiveIndex().whooshCSV(CSV_FILE_NAME)
