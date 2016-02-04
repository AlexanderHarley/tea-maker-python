#Name:      Collatz-conjecture-python
#Author:    Ethan Dunford
#Email:     ethan@ethandunford.com
#Version:   1.0
# Concept > Build tea maker web app in python
# 1) Write basic function to split string into list and select random
# 2) Convert to web application
# Feel free to rewrite this script if can shorten it
import random

def teamakers(raw):
    raw = raw.split()
    print random.choice(raw).title()#tite method can be put on here of after split
teamakers(raw = raw_input("Please enter peoples names:"))
#assigning raw to raw_input and calling the function like that saves a few lines of code
