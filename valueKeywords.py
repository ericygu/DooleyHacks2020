dictionary = {}


# think about how keywords are set to values
# format {'potato': 4, 'oil': 1}


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


print(word_count("potato potato potato potato oil"))
