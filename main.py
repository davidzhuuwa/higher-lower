# Print starting logo 
from art import logo,vs 
from game_data import data 
import random as rd 
from replit import clear 
print(logo)
score = 0

game_state = True 

# Comparison lines A and B, which uses information from data dictionary with the person's name, occupation and location
def select_person():
    choice = rd.choice(data)
    name = choice['name']
    follower_count = choice['follower_count']
    description = choice['description']
    country = choice['country']
    return name,follower_count,description,country,choice 

def compare(followerA,followerB, user_choice):
    Amore = False
    Bmore = False 
    if followerA > followerB:
        Amore = True 
    elif followerB > followerA:
        Bmore = True 
    if (user_choice == "a" and Amore):
        correct_choice = True 
    elif (user_choice == "b" and Bmore):
        correct_choice = True 
    else: 
        correct_choice = False
    return correct_choice 
def reset_graphics():
    clear()
    print(logo)

nameA,followerA,descriptionA,countryA,dataA = select_person()
nameB,followerB,descriptionB,countryB,dataB = select_person()
while game_state:
    print(f"Compare A: {nameA}, a {descriptionA}, from {countryA}, with {followerA} followers.")
    print(vs)
    print(f"Against B: {nameB}, a {descriptionB}, from {countryB}, with {followerB} followers.")
    choice = input('who has more followers? Type "A" or "B": ').lower
    correct_choice = compare(followerA=followerA,followerB=followerB,user_choice=choice)
    if correct_choice:
        score+=1
        reset_graphics()
        print("You're right! Current score: 1")
        nameA = nameB
        followerA = followerB
        descriptionA = descriptionB
        countryA = countryB 
        nameB,followerB,descriptionB,countryB,dataB = select_person()
    else:
        reset_graphics()
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_state = False





#print(rd.choice(data))
