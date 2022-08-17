from bs4 import BeautifulSoup
import requests
from typing import List,Dict


def read_htm(text_path:str) ->str:

    # connect to path and get the text using request
    # clean data using soup  
    response = requests.get(text_path)
    #remove html tags < />
    data = BeautifulSoup(response.content,"html.parser")
    output = data.get_text()
    return output

def preprosses(output:str)->List:
    #remove changes made by parsing from html file 
    output = output.replace("\r\n", " ")
    output = output.replace("\n\r", " ")
    output = output.replace("\n\n", " ")
    output = output.replace("\xa0", " ")

    #remove numbers
    for i in range(10):
        output = output.replace(str(i),"")

    #remove punctuation
    output = output.replace("-"," ")
    output = output.replace(","," ")
    output = output.replace("."," ")
    output = output.replace(";"," ")
    output = output.split('\n')
    return output


def print_max(dict:Dict,number_of_max=20)->None:

    for i in range(number_of_max):
        #find max 20 words 
        var = max(dict,key=dict.get)
        print(str(dict[var])+' - '+var[::-1])
        del dict[var]


def main(text_path:str):
    words_dict = {}
    output = read_htm(text_path=text_path)
    output = preprosses(output=output)
    for line in output:
        split_line = line.split(' ')
        for word in split_line:
            if(len(word)<2):
                #skip space,chars and '' 
                continue
            if word in words_dict:
                words_dict[word] +=1
            else:
                words_dict[word] = 1
    print_max(words_dict)
    

if __name__ == '__main__':
    text_path = 'https://mechon-mamre.org/i/t/x/x01.htm'
    main(text_path=text_path)
