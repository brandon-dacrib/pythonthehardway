#import the argv method from the sys module
from sys import argv

#say that 2 arguments will be passed where the 1st is the script name automagically and the second will be filename
script, filename = argv

#open the file that is the var filename
txt = open(filename)

#print the filename
print "Here's your file %r:" % filename
#read in the var for txt and print it
print txt.read()

#ask you to type the filename again
print "Type the filename again:"
#set the file_again var based on what is input using "> " as the prompt
file_again = raw_input("> ")

#open what is in file_again
txt_again = open(file_again)

#print the output of running the read method against txt_again with no arguments 
print txt_again.read()