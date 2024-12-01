
#questions dictionary
questions = {
 "Which country has the largest population?: ": "A",
 "What year did England win the world cup?: ": "B",
 "Which country has the most islands?: ": "C",
 "Is the Earth round?: ": "A",
 "How many planets are in our solar system?: ": "D"
}

options = [["A. India", "B. China", "C. USA", "D. Egypt"],
          ["A. 1989", "B. 1966", "C. 2000", "D. 2016"],
          ["A. Canada", "B. Philippines", "C. Sweden", "D. Indonesia"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"],
          ["A. 5","B. 9", "C. 6", "D. 8"]]

def new_game():

    

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)

        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D):")
        guess = guess.upper()
        guesses.append(guess)    

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)    



def check_answer(answer, guess):

    if answer == guess:
        print("Correct")
        return 1
    else: 
        print("Wrong")
        return 0        
    
def display_score(correct_guesses, guesses):
    print("Answers: ", end="")       
    for i in questions:
        print(questions.get(i), end=" ") 
    print() 

    print("Answers: ", end="")       
    for i in guesses:
        print(i, end=" ") 
    print()   

    score = correct_guesses/len(questions)*100
    print("Your score is: "+str(score)+"%")
    print("Thank you for playing")





new_game()          