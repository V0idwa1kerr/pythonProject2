def thesaurus(*names):
    dictionary = dict()
    for name in names:
        i = name[0]
        if i not in dictionary:
            dictionary[i] = []
        dictionary[i].append(name)
    return dictionary


print(thesaurus())
