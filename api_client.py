import urllib.request as request
import json


class api_client():

    API_KEY = '66c2e12a4d234e33b3df8d3057ea4a5a'
    ENDPOINT = 'http://newsapi.org/v2/everything?from=2020-01-22&sortBy=popularity&sources=bbc-news'

    def __init__(self):
        self.params = {
            'from': '2020-01-22',
            'sortBy': 'popularity',
            'sources': 'bbc-news'
        }

    def get_by_keyword(self, keyword):
        # print(f'{self.ENDPOINT}&q={keyword}&apiKey={self.API_KEY}')
        with request.urlopen(f'{self.ENDPOINT}&q={keyword}&apiKey={self.API_KEY}') as url:
            data = json.loads(url.read().decode())
            return data

    @staticmethod
    def pretty_print_response(response):
        print(response['totalResults'])
        for i in response['articles']:
            print(i['title'])


if __name__ == '__main__':
    a = api_client()
    a.pretty_print_response(a.get_by_keyword('facebook'))
