#string to parse
str = 'X-DSPAM-Confidence:0.8475'

#find the location of the : character
x = str.find(':')
print(x)

#find the location following the : character
a = str.find(' ',x)
print(a)

#slice the string at the identified points
number = str[x+1:a]

#turn into a float
number = float(number)
print(number)
