# Alex Smith
# MIDS W205
# Assignment #4

import whoosh   # import the whoosh module to help with indexing and searching my data
import os       # import the OS module to interact with the operating system, creating directories where necessary
import csv      # import the CSV module to help with getting the CSV file into python

# import the specific parts of whoosh we need to create the schema
from whoosh.fields import Schema, TEXT, KEYWORD, NUMERIC, ID, STORED

# import the specific field necessary to create the index
from whoosh.index import create_in

class ArchiveIndex:
    # a class to index data for easier searching and retrieval

    def whooshCSV(self, csvfile):
        """create a whoosh index for a CSV file"""

        # create the schema for our whoosh index
        my_schema = ArchiveIndex().createSchema()

        # create the index on the hard drive
        index = ArchiveIndex().createIndex(my_schema)

        # create the writer to write to whoosh
        writer = index.writer()

        # intialize the whoosh ID field
        whoosh_id = 0

        # open the file using the CSV module which splits by lines and then by commas automatically
        csvfile = csv.reader(csvfile)

        # iterate through each line, adding it to whoosh, treating each line as a list
        for line in csvfile:
            # increment the id counter by 1
            whoosh_id = whoosh_id + 1

            # check to make sure that the list has the correct number of elements and
            # is not one of the empty lines in the CSV file
            if len(line) > 1:

                # add each element to the whoosh document
                writer.add_document(id = whoosh_id,
                                    tweet_id = line[0],
                                    screen_name = line[1],
                                    date = line[2],
                                    time = line[3],
                                    text = line[4],
                                    hashtag = line[5])

        # commit the changes to the writer
        writer.commit()

        # run 4 sample queries to test the whoosh index
        ArchiveIndex().runSamples(index)

    def createSchema(self):
        """create the schema for whoosh to index the file by, using the same field that we scraped with our spider"""

        # use the whoosh fields to classify each scraped and store all fields for indexing
        schema = Schema(id = ID(unique=True, stored=True),
                            tweet_id = NUMERIC(stored=True),
                            screen_name = TEXT(stored=True),
                            date = TEXT(stored=True),
                            time = TEXT(stored=True),
                            text = TEXT(stored=True),
                            hashtags = TEXT(stored=True))

        return schema

    def createIndex(self, schema):
        """create a whoosh index in the local directory"""

        # create the directory and create the index using the schema
        os.mkdir("tweet_index")
        index = create_in("tweet_index", schema)

        # open the directory
        index = whoosh.index.open_dir("tweet_index")

        return index

    def runSamples(self, index):
        """run four sample queries to test the whoosh indexing"""

        # create the searcher based on the provided index
        searcher = index.searcher()

        # create the first query to search for all tweets by people with screennames including "Sue"
        query1 = whoosh.query.Term("screen_name", "Sue")
        print "All tweets by Sue's:"
        print searcher.search(query1)

        # create the second query to search for tweets by a specific screenname, "SueTrad",
        # that occurred on June 6th
        query2 = whoosh.query.And([whoosh.query.Term("screen_name", "SueTrad"), whoosh.query.Term("date","6 Jun 2015")])
        print "SueTrad's tweets from July 6th:"
        print searcher.search(query2)

        # create a third query to count the number of tweets on June 6th
        query3 = whoosh.query.Term("date", "6 Jun 2015")
        print "Number of tweets from June 6th:"
        print len(searcher.search(query3))

        # create a fourth query to count the number of tweets on June 6th containing the hashtag, "CAN" for Canada
        query4 = whoosh.query.And([whoosh.query.Term("hashtags", "CAN"), whoosh.query.Term("date","6 Jun 2015")])
        print "Number of tweets from June 6th with the hashtag Canada:"
        print len(searcher.search(query4))
