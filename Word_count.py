import argparse
import sys

def file_split (file_name):
    #function for splitting file to words
    text_file = []
    f = open(file_name , 'r')
    for line in f:
        for word in line.split()    :
            text_file.append(word)
    return text_file

def file_compare (text_file , sample):
    #function to compare the sample word with ones in a file
    words_found = []
    flag = 0
    words_not_found = []
    for sample_word in sample:
        for words in text_file:
            if sample_word.lower() == words.lower():
                flag=1

        if flag==1:
            words_found.append(sample_word)
            flag=0
        else:
            words_not_found.append(sample_word)

    print ("the words found are: ")
    print (words_found)
    print ("the words not found are: ")
    print (words_not_found)








def main():
    arg_list = []
    parse= argparse.ArgumentParser()
    parse.add_argument('--file')
    parse.add_argument('-q',nargs='*')
    arg1=parse.parse_args()
    file_name1 = arg1.file
    arg_list = arg1.q
    text =  file_split (file_name1)
    file_compare(text , arg_list)

    #print (file_name1)
    #print (text)
    #print (arg_list)


if __name__ == "__main__":
    main()
