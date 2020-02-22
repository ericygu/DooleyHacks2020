import json
import re

API_KEY = '66c2e12a4d234e33b3df8d3057ea4a5a'


def get_articles():
    from newsapi import NewsApiClient
    newsapi = NewsApiClient(api_key=API_KEY)

    def get_page(n, source='bbc-news'):
        return newsapi.get_everything(
            q='facebook',
            sources=source,
            from_param='2020-01-22',
            language='en',
            sort_by='relevancy',
            page=n
        )

    def parse_article(article):
        p = re.compile('[\^\'!\.?:,]+')
        return {
            'title': p.sub("", article['title'].lower()),
            # 'content': p.sub("", article['content'].lower()),
            'description': p.sub("", article['description'].lower()),
            'date_published': article['publishedAt']
        }

    page_1 = get_page(1)
    hits = page_1['totalResults']
    articles = []
    cur_page = 1

    while len(articles) <= hits:
        print(len(articles))
        try:
            page = get_page(cur_page)
        except:
            break
        articles += [parse_article(art) for art in page['articles']]
        cur_page += 1

    return articles


def write_articles(articles):
    with open('articles.json', 'w') as fp:
        json.dump(articles, fp)


def read_articles():
    with open('articles.json') as f:
        return json.load(f)


if __name__ == '__main__':
    write_articles(get_articles())
