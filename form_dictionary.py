import json
from load_articles import read_articles

dictionary = {}


# think about how keywords are set to values
# format {'potato': 4, 'oil': 1}
def insert_dictionary(str):
    words = str.split()
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1


def write_dictionary():
    with open('dictionary.json', 'w') as fp:
        json.dump(dictionary, fp)


def read_dictionary():
    with open('dictionary.json') as f:
        return json.load(f)


if __name__ == '__main__':
    articles = read_articles()
    for article in articles:
        insert_dictionary(article["title"])
        insert_dictionary(article["description"])
    write_dictionary()
    print(len(dictionary))
