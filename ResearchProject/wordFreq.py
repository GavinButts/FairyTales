from pathlib import Path
import os
import re

def get_all_files(directoryPath):
    allfiles = []

    path_of_the_directory = os.path.expanduser(directoryPath)
    file_name = Path(path_of_the_directory ).glob('*')

    for i in file_name:
        allfiles.append(i)
    
    return allfiles

def read_all_files(file_loc):
    txt_file = []

    for file in file_loc:
        f = open(file, 'r')
        txt_file.append(f.readline())
        f.close

    return txt_file

def extract_words(text):
    list_of_lists = []
    for line in text:
        list_of_words = re.findall(r'\w+', line)
        list_of_lists.append(list_of_words)

    return list_of_lists

def make_list_of_words(text):
    final_list = []
    for list in text:
        for word in list:
            final_list.append(word.lower())
    
    return final_list

def make_word_dict(words):
    frequency_dict = {}
    wordcount = 0
    for word in words:
        wordcount += 1
        if frequency_dict.get(word) == None:
            frequency_dict[word] = 1
        else:
            x = frequency_dict[word]
            frequency_dict[word] = x+1
    
    return frequency_dict

def sort_dict(dictionary):
    sorted_frequency = sorted(dictionary.items(), key = lambda kv: kv[1], reverse=True)

    sorted_dictionary = dict(sorted_frequency)
    return sorted_dictionary

def frequent_words(frequency_dictionary):
    dict_as_list = list(frequency_dictionary)
    freq_words = []
    for i in range(50):
        freq_words.append(dict_as_list[i])

    return freq_words

fileLocations = get_all_files("~/Desktop/FALL2022/HNRS3200/Text")
text = read_all_files(fileLocations)
words_from_txt = extract_words(text)
all_words = make_list_of_words(words_from_txt)
freq_dict = sort_dict(make_word_dict(all_words))
print(frequent_words(freq_dict))
