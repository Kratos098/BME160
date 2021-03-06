#!/usr/bin/env python3
# Name: Manishankar Bhaskaran (mbhaska1)
# Group Members: Natalie Bratset (nbratset)

class ProteinParam :
# These tables are for calculating:
#     molecular weight (aa2mw), along with the mol. weight of H2O (mwH2O)
#     absorbance at 280 nm (aa2abs280)
#     pKa of positively charged Amino Acids (aa2chargePos)
#     pKa of negatively charged Amino acids (aa2chargeNeg)
#     and the constants aaNterm and aaCterm for pKa of the respective termini
#  Feel free to move these to appropriate methods as you like

# As written, these are accessed as class attributes, for example:
# ProteinParam.aa2mw['A'] or ProteinParam.mwH2O

    aa2mw = {
        'A': 89.093,  'G': 75.067,  'M': 149.211, 'S': 105.093, 'C': 121.158,
        'H': 155.155, 'N': 132.118, 'T': 119.119, 'D': 133.103, 'I': 131.173,
        'P': 115.131, 'V': 117.146, 'E': 147.129, 'K': 146.188, 'Q': 146.145,
        'W': 204.225, 'F': 165.189, 'L': 131.173, 'R': 174.201, 'Y': 181.189
        }

    mwH2O = 18.015
    aa2abs280= {'Y':1490, 'W': 5500, 'C': 125}

    aa2chargePos = {'K': 10.5, 'R':12.4, 'H':6}
    aa2chargeNeg = {'D': 3.86, 'E': 4.25, 'C': 8.33, 'Y': 10}
    aaNterm = 9.69
    aaCterm = 2.34

    def __init__(self, protein):
        '''Initialize class variables to be used by the class methods.'''
        self.protein = protein                  # class variable protein is the given protein sequence
        self.composition = self.aaComposition() # class varaible composition is the dictionary returned by aaCompostion()

    def aaCount(self):
        '''Returns the total number of valid amino acid characters found in the protein string'''
        # initialize a list called validChars that contains all valid characters that the aaCount() should count
        validChars = ["A", "C", "D", "E", "F", "G", "H", "I", "L", "K", "M", "N", "P", "Q", "R", "S", "T", "V", "Y", "W"]
        count = 0                           # initialize an intager count to zero
        for char in (self.protein).upper(): # iterate over every character of an uppercase version of the protein string
            if char in validChars:          # if the current character is in validChars, increment count by 1
                count += 1
        return count                        # return count

    def aaComposition(self):
        '''Returns a dictionary with (key, value) pairs of (animo acid character, count in protein string)'''
        # define a dictionary named charDict with the valid amino acid chars as keys and all values as 0
        charDict = {
            "A": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "L": 0, "K": 0,
            "M": 0, "N": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "V": 0, "Y": 0, "W": 0
            }
        for char in (self.protein).upper(): # iterate over every character of an uppercase version of the protein string
            if char in charDict:            # if the current character exists in the dictionary, increment its value by 1
                charDict[char] = charDict.get(char) + 1 
        return charDict                     # return charDict

    def molarExtinction(self):
        '''Return the extinction coefficient of the native protein in water'''
        exCo = {"Y": 1490, "W": 5500, "C": 125} # include the table provided and name it exCo
        comp = self.composition                 # initialize variable named comp to be class varaible composition
        # return the extinction coefficient using the formula given
        return (comp.get("Y")*exCo.get("Y")) + (comp.get("W")*exCo.get("W")) + (comp.get("C")*exCo.get("C"))

    def massExtinction(self):
        myMW =  self.molecularWeight()
        return self.molarExtinction() / myMW if myMW else 0.0

    def molecularWeight(self):
        '''Return the total molar weight of the entire protein sequence'''
        # include the aa2mw table provided for calculations
        aa2mw = {
        'A': 89.093,  'G': 75.067,  'M': 149.211, 'S': 105.093, 'C': 121.158,
        'H': 155.155, 'N': 132.118, 'T': 119.119, 'D': 133.103, 'I': 131.173,
        'P': 115.131, 'V': 117.146, 'E': 147.129, 'K': 146.188, 'Q': 146.145,
        'W': 204.225, 'F': 165.189, 'L': 131.173, 'R': 174.201, 'Y': 181.189
        }
        mwH2O = 18.015          # include the value of mwH2O provided for calulcations
        molW = mwH2O            # intializa a variable molW to the value of mwH2O
        comp = self.composition # intialize a dictionary comp to be the class variable composition
        for char in comp:       # for every character in the dictionary, incremenet molW with the proper calulation
            molW += comp.get(char) * (aa2mw.get(char) - mwH2O)
        return molW             # return molW
    
    def _charge_(self, pH):
        '''Returns the net charge of the given protein at the specified pH'''
        # include tables and values included for calculations
        aa2chargePos = {'K': 10.5, 'R':12.4, 'H':6}
        aa2chargeNeg = {'D': 3.86, 'E': 4.25, 'C': 8.33, 'Y': 10}
        aaNterm = 9.69
        aaCterm = 2.34

        protein = self.protein  # initialize variable named protein to be class varaible protein
        comp = self.composition # initialize variable named comp to be class varaible composition

        chargePos = (10**aaNterm)/((10**aaNterm)+(10**pH)) # initialize chargePos to be the relevant part of the equation with Nterm
        chargeNeg = (10**pH)/((10**aaCterm)+(10**pH))      # initialize chargeNeg to be the relevant part of the equation with Cterm
        for char in protein.upper():   # for every character in the uppercase version of protein
            if char in aa2chargePos:   # if char is in aa2chargePos, apply the relevant part of the equation and increment chargePos
                numer = (10 ** aa2chargePos.get(char))
                denom = (10 ** aa2chargePos.get(char)) + (10 ** pH)
                chargePos += numer/denom
            
            elif char in aa2chargeNeg: # if char is in aa2chargeNeg, apply the relevant part of the equation and increment chargeNeg
                numer = (10 ** pH)
                denom = (10 ** aa2chargeNeg.get(char)) + (10 ** pH)
                chargeNeg += numer/denom
        
        return chargePos - chargeNeg # return the difference between chargePos and chargeNeg
    
    def pI(self):
        '''Returns the pH of the The theoretical isolelectric point of the protein'''
        # intialize pH, maxpH, charge, and maxCharge to reasonable values
        pH        = 0.0
        maxpH     = 42.0
        charge    = 0.0
        maxCharge = 999
        while pH <= 14: # while pH is less than or equal to 14
            charge = self._charge_(pH) # call the _charge_ method and assign its value to charge
            if abs(maxCharge) >= abs(charge): # if the abs val of maxCharge is greater than or equal to the abs val of charge, 
                                              # maxpH is pH and maxCharge is charge
                maxpH = pH
                maxCharge = charge
            pH += 0.01 # increment pH by 0.01
        return maxpH #return maxpH

# Please do not modify any of the following.  This will produce a standard output that can be parsed

import sys
def main():
    inString = input('protein sequence?')
    while inString :
        myParamMaker = ProteinParam(inString)
        myAAnumber = myParamMaker.aaCount()
        print ("Number of Amino Acids: {aaNum}".format(aaNum = myAAnumber))
        print ("Molecular Weight: {:.1f}".format(myParamMaker.molecularWeight()))
        print ("molar Extinction coefficient: {:.2f}".format(myParamMaker.molarExtinction()))
        print ("mass Extinction coefficient: {:.2f}".format(myParamMaker.massExtinction()))
        print ("Theoretical pI: {:.2f}".format(myParamMaker.pI()))
        print ("Amino acid composition:")
        myAAcomposition = myParamMaker.aaComposition()
        keys = list(myAAcomposition.keys())
        keys.sort()
        if myAAnumber == 0 : myAAnumber = 1  # handles the case where no AA are present 
        for key in keys :
            print ("\t{} = {:.2%}".format(key, myAAcomposition[key]/myAAnumber))
            
        inString = input('protein sequence?')

if __name__ == "__main__":
    main()
# VLSPADKTNVKAAW