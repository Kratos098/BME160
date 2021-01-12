#!/usr/bin/env python3 
# Name: Manishankar Bhaskaran (mbhaska1)
# Group Members: Natalie Bratset (nbratset)

'''
Read a DNA string from user input and return a collapsed substring of embedded Ns to: {count}.

Example: 
 input: AaNNNNNNGTC
 output: AA{6}GTC

Any lower case letters are converted to uppercase
'''

class DNAstring (str):
    def length(self):
        return (len(self))
    
    def purify(self):
        ''' Return an upcased version of the string, collapsing a single run of Ns.'''
        pureDNA = ""                  # create a new string called pureDNA and intialize it to be empty
        unpureDNA = str(self).upper() # store an uppercase version of the input string in unpureDNA
        i = 0                         # create a new integer called i and intialize it to 0
        count = 0                     # create a new integer called count and intialize it to 0
        while i < len(unpureDNA):     # iterate i from 0 to the length of unpureDNA
            if unpureDNA[i] == "N":                                # if the character at index i in unpureDNA is "N"
                while i < len(unpureDNA) and unpureDNA[i] == "N":  # loop until either the character at index i isn't an N or we have reached the end of unpureNDA
                    count += 1 # increment count by 1
                    i += 1     # increment i by 1
                pureDNA += "{" + str(count) + "}" # add the number of N's as well as brackets to the pureDNA string
                count = 0                         # reintialize count to 0
            pureDNA += unpureDNA[i] # add the current character at index i to the string pureDNA
            i += 1                  # increment i by 1
        return pureDNA # return the final string pureDNA

def main():
    ''' Get user DNA data and clean it up.'''
    data = input("DNA data?" )
    thisDNA = DNAstring(data)
    pureData = thisDNA.purify()
    print(pureData)
    
main()