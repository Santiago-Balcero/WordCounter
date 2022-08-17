#This script reads a text from txt file, creates a string with it and counts words
#TO DO: present the resulting dictionary as a word map.

import os
import codecs

TEXT_NAME = "Texto.txt"

def word_count(text: str):
    #Returns a dictionary with {word: number of times it appears in text}.
    text = text.lower()
    #Avoid has spanish words to avoid in count
    avoid = ["que", "a", "la", "en", "el", "los", "las", "y", "una", "no", "sí", "si", "de", "sin", "con", "como", "cómo"]
    #To_replace has characters to remove from string to clean it before processing.
    to_replace = [".", ",", "!", "¡", "?", "¿", ":", ";", "-", "_", "/",
                  "''", "%", "(", ")", "=", "+", "*", "|", "°"]
    words = {}
    for character in to_replace:
        text = text.replace(character,"")
    text = text.split()
    for word in text:
        if word in avoid:
            continue
        elif word not in words:
            words[word] = 1
        else:
            words[word] += 1
    #RESULTADO ORDENADO sort_words = sorted(words.items(), key=lambda x:x[1], reverse=True)
    return words

def create_text(text_name: str):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, text_name)
    with codecs.open(filename, encoding='utf-8') as text:
        text_string = ""
        for line in text:
            text_string += line
    return text_string

def popular_word(words: dict):
    
    popular_word = ""
    number_times = 0
    for word in words:
        if words[word] > number_times:
            popular_word = word
            number_times = words.get(word)
    return (popular_word, number_times)    
    
to_process = create_text(TEXT_NAME)
words_count= word_count(to_process)
pop_word = popular_word(words_count)
print(f"Most common word is '{pop_word[0].upper()}' and appears {pop_word[1]} times.")