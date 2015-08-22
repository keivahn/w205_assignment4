# Alex Smith
# MIDS W205
# Assignment #4

import urllib           # import urllib module to help with queries

class urlFormat:
    # class for creating URL formatted text from various data structures

    def singleString(self, query):
        """returns the URL formatted text for a string"""

        query = urllib.quote_plus(query)
        return query

    def stringList(self, strings):
        """returns a list of strings, all of which have been formatted to URL"""

        # create a blank list for holding the newly formatted strings
        query_list = []

        # iterate through the provided list, converting each element to URL format
        # and then appending onto the list
        for term in strings:
            term = urllib.quote_plus(term)
            query_list.append(term)

        return query_list
