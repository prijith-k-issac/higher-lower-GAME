from random import choice 
from game_data import data
from art import logo,vs
from replit import clear



def game_data():
    """returns each person data"""
    person_detail=choice(data)
    return person_detail
    
def statement_generator(person_data): 
    """shows person details to the user"""
    return f": {person_data['name']}, a {person_data['description']}, from {person_data['country']}"
    
def result_verifier(person_one_follower,person_two_follower):
    """ returns the result"""
    if person_one_follower > person_two_follower:
        answer = "a"
    else:
        answer = "b" 
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()       
    if user_input == answer:
        global score
        score +=1
        return False    
    else:
        return True 
         

score = 0 
is_game_over = False
first_person = game_data()
print(logo)


while not is_game_over:
    
    second_person = game_data()
    while first_person['follower_count'] == second_person['follower_count']:
        second_person = game_data()
    print(f"Compare A: {statement_generator(first_person)}")
    print(vs)
    print(f"Against B: {statement_generator(second_person)}")
    # print(f"Person a:{first_person['follower_count']}, Person b:{second_person['follower_count']}")
    is_game_over = result_verifier(first_person['follower_count'],second_person['follower_count'])
    first_person = second_person
    clear()
    print(logo)
    print(f"You're right! Current Score:{score}")

clear()
print(logo)
print(f"Sorry, that's wrong. Final Score:{score}")