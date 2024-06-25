#!/bin/bash
#Program asks user to enter a word and uses the entered words to complete a story
adjective = str(input("Enter an adjective: "))
noun = str(input("Enter an noun: "))
verb = str(input("Enter an verb: "))
pronoun = str(input("Enter a pronoun: "))

if adjective and noun and verb and pronoun:
    print("He was known for his", adjective, "swimming skills."
          " His love for", noun, "outmarched his desire to be a star!"
          " He traversed several continents chasing fame. He almost succeeded." 
          " Sadly, he lost the motivation just when he was supposed to", verb + "." 
          " It was rumoured that Sara was his poison,", pronoun,
          "was the one who lured him to a journey of no retreat. He got lost deep into drugs!")
