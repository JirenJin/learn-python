# import argv module
from sys import argv
# get the arguments
script, input_file = argv

def print_all(f):
    print f.read()
# moves the file to the 0 byte in the file.
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()
# open the file
current_file = open(input_file)

print "First let's print the whole file:\n"
# print all of the file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# moves the file to the 0 byte
rewind(current_file)

print "Let's print three lines:"
# manually count the current_line
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
