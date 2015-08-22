# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TweetsItem(scrapy.Item):
    # class for holding the data that we store

    tweet_id = scrapy.Field()       # field for individual's name
    screen_name = scrapy.Field()    # field for individual's screen name
    date = scrapy.Field()           # field for the date of the tweet
    time = scrapy.Field()           # field for the time of the tweet
    text = scrapy.Field()           # field for the text of the tweet
    hashtag = scrapy.Field()        # field for the hashtags of a given tweet
