dictionary = {}


# think about how keywords are set to values
# format {'potato': 4, 'oil': 1}


def insert_dictionary(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return counts

insert_dictionary("potato potato potato potato oil")
print(dictionary)

