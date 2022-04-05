# 1 Напишите программу, которая получает от пользователя имя файла,
# открывает этот файл в текущем каталоге, читает его и выводит два слова:
# наиболее часто встречающееся из тех, что имеют размер более трех символов,
# и наиболее длинное слово на английском языке.
# В файле ожидается смешанный текст на двух языках — русском и английском.
# search_words.txt

def is_eng_word(str):
    eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba'
    for i in str:
        if i not in eng:
            return False
    return True

def prepare_text(str):
    result = str
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        result = result.replace(i, '')
    return result

def get_unique_items(items):
    unique_words = {}
    for i in words:
        count = unique_words.get(i)
        if count is None:
            unique_words[i] = 1
        else:
            unique_words[i] = count + 1
    return unique_words

def get_word_max_repeatable(dict_words, min_count_chars = 3):
    dictionary_words_more_3 = {}
    for i in dict_words.keys():
        if len(i) > min_count_chars:
            dictionary_words_more_3[i] = dict_words.get(i)

    max_count_repeatable = 0
    result_key = ""
    for i, j in dictionary_words_more_3.items():
        if j > max_count_repeatable:
            max_count_repeatable = j
            result_key = i
    return result_key

def get_longest_english_word(dict_words):
    long_eng_word = ""
    count_char_in_eng_word = 0
    for i in dict_words.keys():
        if len(i) > count_char_in_eng_word and is_eng_word(i):
            count_char_in_eng_word = len(i)
            long_eng_word = i
    return long_eng_word




filename = input('Введите имя файла: ')

try:
    file = open(filename, 'r')
    data = file.read()
    file.close()

except Exception as ex:
    print('Файл не существует.')
else:
    data = prepare_text(data)
    words = data.split()

    dictionary_words = get_unique_items(words)
    max_count_key = get_word_max_repeatable(dictionary_words)
    long_eng_word = get_longest_english_word(dictionary_words)

    print("Наиболее часто встречающееся из тех, что имеют размер более трех символов:", max_count_key)
    print("Наиболее длинное слово на английском языке:", long_eng_word)
