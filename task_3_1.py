def num_translate_adv(item):
    nums = {'zero': 'ноль',
            'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}
    if item[0].upper() and nums.get(item.lower()):
        return nums.get(item.lower()).capitalize()
    else:
        return nums.get(item)


user_inp = input("Пожалуйста, введите число от 0 до 10 на английском языке: ")
print(num_translate_adv(user_inp))
