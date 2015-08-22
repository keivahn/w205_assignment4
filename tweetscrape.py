# Alex Smith
# MIDS W205
# Assignment #4

import urlformat        # import the urlformat module to convert queries to a format readable by twitter
import datetime         # import the datetime module to help limit the range of tweets

# language assumption. we choose to only pull English tweets
LANGUAGE = "en"

# basic url encodings for formulating the query
OR = "OR"
SPACE = "%20"
LANGUAGE_OPTION = "lang%3A"
BEGINNING_FRAME = "since%3A"
END_FRAME = "until%3A"
ENDING = "&src=typd&vertical=default&f=tweets"

# twitter's base search URL
TWITTER = "https://twitter.com/search?q="

# incremement for our search results
SEARCH_DELTA = datetime.timedelta(days = 1)


class TweetScrape:
    # class for generating URL for scraping tweets from Twitter

    def advancedSearch(self, query, query_list, begin, end):
        """method that takes a list of queries and searches Twitter's advanced search, limited to a specific beginning and ending time"""

        # convert the main query and query_list to url format
        query = urlformat.urlFormat().singleString(query)
        query_list = urlformat.urlFormat().stringList(query_list)

        # create the string for all team names by linking all team hashtags with or's and spaces
        or_URL = TweetScrape().combineOrURL(query_list)

        # gather all the URLs that we need to scrape
        URLs = TweetScrape().listURL(query, or_URL, begin, end)

        # print the URLs to the console to use in our spider
        print URLs

    def listURL(self, query, or_URL, begin, end):
        """create a list of URLs to search through, each only day long"""

        # create a blank list to store the URLs
        URLList = []

        # set current to begin to start the iterator
        current = begin

        # iterate through every day in the range, creating a new URL for each day's search results
        while current <= end:
            # create a list of URL based on the search terms
            url = TWITTER + query + SPACE + or_URL + SPACE + LANGUAGE_OPTION + LANGUAGE + SPACE + BEGINNING_FRAME + str(current) + SPACE + END_FRAME + str(current + SEARCH_DELTA) + ENDING
            URLList.append(url)
            current = current + SEARCH_DELTA

        # return the list of URLs
        return URLList


    def combineOrURL(self, query_list):
        """takes a list of queries and combines them into an OR statement for twitter's search URL"""

        # start a blank string
        or_URL = ""

        # iterate over all queries and combine them together using spaces
        for term in query_list:
            if or_URL == "":
                or_URL = or_URL + term
            else:
                or_URL = or_URL + SPACE + OR + SPACE + term

        return or_URL
