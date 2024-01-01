'''
Write a program that prints the number of times the string 'iti'
occurs in anystring.
'''

sentense = "iti:information technology institute, ITI have many branches."

#sentense.lower() #convert to case-sensitive

itiNumbers=sentense.lower().count('iti')

print(itiNumbers)