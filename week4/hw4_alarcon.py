from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import sys
import urllib
from bs4 import BeautifulSoup

# Author: Mauricio Alarcon <rmalarc@msn.com>

class TextFromURL:
    def __init__(self):
        self.alchemy_api = AlchemyAPI()

    def extract_text(self, url_param):
        """
        This method takes a URL and extracts the text contained in the page referenced by the URL using the alchemy
        text service.

        :param url_param:
        :return: Returns the parsed text
        """
        self.url = url_param
        self.response = self.alchemy_api.text('url', self.url)
        if self.response['status'] == 'OK':
            json.dumps(self.response, indent=4)
            self.parsed_text = self.response['text'].encode('utf-8')
        else:
            print('Error in text extraction call: ', self.response['statusInfo'])
        return (self.parsed_text)

    def extract_text_by_element_id(self, url_param, html_element_id):
        """
        This method extracts text from a webpage based on the ID of an element within the HTML code. It uses beautiful
        soup to parse the page and extract the content

        :param url_param:
        :param html_element_id: ID of the HTML element where the desired text is located
        """
        f = urllib.urlopen(url_param)
        website = f.read()
        soup = BeautifulSoup(website, 'html.parser')
        self.parsed_text = soup.find(id=html_element_id).get_text()
        return(self.parsed_text)



class KeywordsFromText:
    def __init__(self):
        self.alchemy_api = AlchemyAPI()

    def process_keywords(self, text):
        """
        This method processes the keywords contained in the text using the alchemy keywords service

        :param text:
        :return:
        """
        self.text = text
        self.response = self.alchemy_api.keywords('text', self.text, {'sentiment': 1})
        if self.response['status'] != 'OK':
            print('Error in text extraction call: ', self.response['statusInfo'])
        return

    def print_keywords(self, show_top=0):
        """
        Prints list of top-n keywords

        :param show_top: top-n keywords to display. The default shows all keywords
        :return:
        """
        if hasattr(self,'response'):
            if self.response['status'] == 'OK':
                i = 0
                for keyword in self.response['keywords']:
                    print('keyword: ', keyword['text'].encode('utf-8'))
                    print('relevance: ', keyword['relevance'])
                    print('sentiment: ', keyword['sentiment']['type'])
                    print('')
                    i += 1
                    if i == show_top:
                        break
            else:
                print("process_keywords did not succeed. Check the URL")
        else:
            print("Keywords haven't been processed yet. Run process_keywords()")
        return


if __name__ == "__main__":
    text_extractor = TextFromURL()
    keyword_extractor = KeywordsFromText()
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        url = "https://en.wikipedia.org/wiki/Pope_Francis"

    print("Extracting text using the Alchemy API from: "+url)
    text = text_extractor.extract_text(url)
    print("Extracting keywords using the Alchemy API:")
    keyword_extractor.process_keywords(text)
    keyword_extractor.print_keywords(10)

    print("==========================================")

    # Let's look at the "content" element ID from Pope Francis' Wikipedia page. (it works for any wikipedia pages)
    element_id = "content"
    print("Extracting text using BeautifulSoup from: "+url+", Element ID: " + element_id)
    text = text_extractor.extract_text_by_element_id(url,element_id)
    print("Extracting keywords using the Alchemy API: ")
    keyword_extractor.process_keywords(text)
    keyword_extractor.print_keywords(10)

