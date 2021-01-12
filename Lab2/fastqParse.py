#!/usr/bin/env python3 
# Name: Manishankar Bhaskaran (mbhaska1)
# Group Members: Natalie Bratset (nbratset)

'''
Read a FASTQ seqnamme line from user input and print the fields separated by colons with their corresponding names

Example:
    input : @EAS139:136:FC706VJ:2:2104:15343:197393
    output: Instrument = EAS139
            Run ID = 136
            ...

Assume the input string will always have 7 fields
Assume the first character of the input string will always be "@"
'''

class FastqString(str):
    '''A class that takes a string as seqname line string as input and contains the method parse'''
    def parse(self):
        '''Print each part of the parsed input string with their corresponding fields.'''
        output = self                    # intialize a new string output with the string passed in through this instance of FastqString
        output = output.replace("@", "") # delete the "@" in output, which we assume will always be the first character of the input
        output = output.split(":")       # seperate output by colons and store the individual parts as a list in output
        fields = ["Instrument", "Run ID", "Flow Cell ID", "Flow Cell Lane", "Tile Number", "X-coord", "Y-coord"] # hardcode the name of the fields in a list called fields
        for i in range(0, len(output)):  # iterate i from 0 to the number of elements in fields
            print(fields[i] + " = " + output[i]) # print the field at intex i from fields and from output in the correct format

def main():
    '''Get user FastQ seqname line and print parsed line as individual fields'''
    line = input("Please enter a FastQ seqname line: ") # ask the user for a FastQ seqname line and store it in line
    seqLine = FastqString(line)                         # create a new instance of the FastqString class named seqLine and pass in the string line
    seqLine.parse()                                     # call the parse() method of FastqString on seqLine

main()