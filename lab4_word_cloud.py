# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 10-10-2019
# purpose: Lab 4

import string


class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary

        self.create_html(self.my_dict)

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurrence of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

        # your code goes here!
        fo.write('<span style="font-size: 10px"> HELLO </span>')

        for i in the_dict:
            fo.write('<span style="font-size: ' + str((the_dict[i] * 10)) + 'px">' + i +'</span>')

        fo.write('</div>\
            </body>\
            </html>')


    # opens the input file gettisburg.txt
    # remember to open in in the correct mode
    # reads the file line by line
    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):
        my_dict = {}
        # your code goes here:

        text = open("gettisburg.txt", "r")


        for line in text:
            word = line.split()

            for i in word:
                self.add_to_dict(i, my_dict)
        print(my_dict)
        return my_dict

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurrence counter to 1
    # returns a dictionary
    def add_to_dict(self, word, the_dict):
        # your code goes here
        if word not in the_dict:
            the_dict[word] = 1
        else:
            the_dict[word] += 1

        return the_dict


wc = WordCloud()
