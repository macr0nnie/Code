import requests
response = requests.get('https://google.com/')
print(response)

print(response.status_code)
if response :
    print('Response is Sucessful')
else:
    print('Request returned an error')

#C:/Users/*
#Absolute Paths vs Relative Paths
#. this directory
#.. the parent directory

#Style Guide 

print ('Hello there friend!\n how are you?')
c = 34
a =4
b = 3 
c = a + b
#no spaces after periods and functions
print("Spacing")  #two spaces for end of the line comments

#if you want to use two line of code you can put a semicolin to put in the same line
print('What is your name?') ; #name = input()
#what is Black? and should it be installed? Does visual studio not install it by default
number =str(number) # type: ignore

#choosing names for software
#Casing Styles
#python is case senstive
snake_case = "A way for programmers to style"
camelCase = "The java c# method"
PascalCase= "In java this is used for methods"

#bad code practices
#duplicate code
#magic numbres
#commented out code & dead code
#use the debugger instead of print debugging
#No need to write classes for code

#Writing Python Code
#the zen of python - contains the principals of coding in python

animals = ['cat','dog','moose']
for i, animal in enumerate(animals):
    print(animal)

for animal in animals:
    print(animal)

