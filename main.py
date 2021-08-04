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
    Tie = False 
    if followerA > followerB:
        Amore = True 
    elif followerB > followerA:
        Bmore = True 
    elif followerA == followerB: 
        # Case when there's a tie - game keeps going but score isn't updated
        Tie = True
        correct_choice = False
        return correct_choice, Tie 
    if (user_choice == "a" and Amore):
        correct_choice = True 
    elif (user_choice == "b" and Bmore):
        correct_choice = True 
    else: 
        correct_choice = False
    return correct_choice,Tie 

def reset_graphics():
    clear()
    print(logo)

nameA,followerA,descriptionA,countryA,dataA = select_person()
nameB,followerB,descriptionB,countryB,dataB = select_person()
while game_state:
    print(f"Compare A: {nameA}, a {descriptionA}, from {countryA}.")
    print(vs)
    print(f"Against B: {nameB}, a {descriptionB}, from {countryB}.")
    choice = input('Who has more followers? Type "A" or "B": ').lower()
    correct_choice,Tie = compare(followerA=followerA,followerB=followerB,user_choice=choice)
    if correct_choice:
        score+=1
        reset_graphics()
        print(f"You're right! Current score: {score}.")
        nameA = nameB
        followerA = followerB
        descriptionA = descriptionB
        countryA = countryB 
        nameB,followerB,descriptionB,countryB,dataB = select_person()
        if dataA == dataB: 
            account_equal = True
            while account_equal:
                nameB,followerB,descriptionB,countryB,dataB = select_person()
                if dataA != dataB:
                    account_equal = False
    elif Tie:
        reset_graphics()
        print(f"The number of followers are equal! The game is not over \n but your score remains the same.")
    else:
        reset_graphics()
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_state = False





#print(rd.choice(data))
