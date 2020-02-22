import json

dictionary = {}


# think about how keywords are set to values
# format {'potato': 4, 'oil': 1}
def insert_dictionary(str):
    words = str.split()
    for word in words:
        if word in counts:
            dictionary[word] += 1
        else:
            dictionary[word] = 1


insert_dictionary("potato potato potato potato oil")
print(dictionary)


def write_dictionary():
    with open('dictionary.json', 'w') as fp:
        json.dump(dictionary, fp)


def read_dictionary():
    with open('dictionary.json') as f:
        return json.load(f)


if __name__ == '__main__':
    pass
