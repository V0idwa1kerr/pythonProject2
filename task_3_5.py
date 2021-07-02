from random import choice


def get_jokes(n, no_repeat=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    array = []
    if no_repeat:
        array_2 = []
    for _ in range(n):
        array_3 = []
        if n > 5:
            no_repeat = False
        if no_repeat:
            new = choice(nouns)
            while new in array_2:
                new = choice(nouns)
            array_3.append(new)

            new = choice(adverbs)
            while new in array_2:
                new = choice(adverbs)
            array_3.append(new)

            new = choice(adjectives)
            while new in array_2:
                new = choice(adjectives)
            array_3.append(new)

        else:
            array_3.append(choice(nouns))
            array_3.append(choice(adverbs))
            array_3.append(choice(adjectives))
        array.append(" ".join(array_3))
        if no_repeat:
            array_2.extend(array_3)
    return array


print(get_jokes(n=5))
