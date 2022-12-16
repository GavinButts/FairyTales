import PySimpleGUI as sg
import numpy as np
from pathlib import Path
import os
import re

#START FILE FREQ
def get_all_files(directoryPath):
    allfiles = []

    path_of_the_directory = os.path.expanduser(directoryPath)
    file_name = Path(path_of_the_directory ).glob('*')

    for i in file_name:
        allfiles.append(i)
    
    return allfiles

def read_all_files(file_loc):
    txt_file = []
    numfiles = 0

    for file in file_loc:
        f = open(file, 'r')
        txt_file.append(f.readline())
        f.close
        numfiles+=1

    return txt_file, numfiles

def extract_words(text):
    list_of_lists = []
    for line in text:
        list_of_words = re.findall(r'\w+', line)
        list_of_lists.append(list_of_words)

    return list_of_lists

def make_list_of_words(text):
    final_list = []
    wordcount = 0
    for list in text:
        for word in list:
            final_list.append(word.lower())
            wordcount += 1
    
    return final_list, wordcount

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

#END FILE FREQ

#START GUI ALGORITHM
sg.theme('LightBrown11')

layout = [  [sg.Text('Please enter your story below.')],
            [sg.Text('Story:'), sg.Multiline(key="texto", size=(50, 20))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]


window = sg.Window('Fairy Tale Text', layout, size=(500, 300))

while True:
    event, values = window.read()
    input_text = values['texto']
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Ok':
        break

window.close()
#END GUI ALGORITHM

#START INPUT TO VECTORS
def relative_freq(dictionary, numfiles):
    relative_freq_dict = {}

    for word in dictionary:
        relative_freq_dict[word] =  int(dictionary[word])/numfiles
    
    return relative_freq_dict

def new_relative_freq(input_text):

    wordcount = 0
    new_freq_dict = {}
    for word in input_text:
        wordcount += 1

        if new_freq_dict.get(word) == None:
            new_freq_dict[word] =  1

        else:   
            x = new_freq_dict[word]
            new_freq_dict[word] = x+1
    
    for word in new_freq_dict:
        freq = new_freq_dict[word]
        freq /= wordcount
        new_freq_dict[word] = freq
    
    return new_freq_dict
#END INPUT VECTORS

#START VECTOR TRIMMING
def make_similar(input_dict, compare_dict):

    dict_len = len(input_dict)
    compare_list = list(compare_dict)

    new_input_dict = {}
    new_compare_dict = {}

    for i in range(dict_len):
        compare_word = compare_list[i]

        new_compare_dict[compare_word] = compare_dict[compare_word]
        
        if compare_dict.get(compare_word) == None:
            new_input_dict[compare_word] = 0
        else:
            new_input_dict[compare_word] = input_dict.get(compare_word)

    return (new_input_dict, new_compare_dict)

def make_vector(input_dict, compare_dict):

    input_list_num = []
    compare_list_num = []

    for word in input_dict:
        input_list_num.append(input_dict[word])
        compare_list_num.append(compare_dict[word])
    
    return (input_list_num, compare_list_num)
#END VECTOR TRIMMING

#START COMPARE
def dot_product(input_vector, compare_vector):
    for i in range(len(input_vector)):
        if input_vector[i] == None:
            input_vector[i] = 0
        
    confidence = np.dot(input_vector, compare_vector)
    return confidence*100
#END COMPARE

#RETURN RESULT
def return_result(confidence):
    print(confidence)
    if confidence < 0.3:
        print("I think this is a fairy tale.")
        return True
    else:
        print("I don't think this is a fairy tale")
        return False
#END COMPARE


fileLocations = get_all_files("~/Desktop/FALL2022/HNRS3200/Text")
text, numfiles = read_all_files(fileLocations)
words_from_txt = extract_words(text)
all_words, wordcount = make_list_of_words(words_from_txt)
freq_dict = sort_dict(make_word_dict(all_words))
print(freq_dict)
freq_dict = relative_freq(freq_dict, wordcount)
print(freq_dict)
input_freq_dict = new_relative_freq(input_text)
dict_tup = make_similar(input_freq_dict, freq_dict)
input_freq_dict = dict_tup[0]
freq_dict = dict_tup[1]
vector_tup = make_vector(input_freq_dict, freq_dict)
input_vector = vector_tup[0]
compare_vector = vector_tup[1]
confidence = dot_product(input_vector, compare_vector)
return_result(confidence)

