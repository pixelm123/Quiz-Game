print("Welcome To My Quiz Game\nAn Exciting Game to Play")

player = input("Do you want to play the game?\n")

if player.lower() != 'yes':
    print("Goodbye")
    quit()

name_player = input("Enter Your Name: ")

print("Let's Start the Game :)", name_player)

score = 0

# Define a function to ask multiple-choice questions
def ask_mc_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    answer = input("Enter the number of your choice: ")
    if answer.isdigit() and 1 <= int(answer) <= len(options):
        if options[int(answer) - 1].lower() == correct_option.lower():
            print("Correct")
            return 1
    print('Wrong')
    return 0

# Question 1
score += ask_mc_question("What is the capital city of Japan?", ["Tokyo", "Seoul", "Beijing"], "Tokyo")

# Question 2
score += ask_mc_question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter"], "Mars")

# Question 3
score += ask_mc_question("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe"], "Blue Whale")

# Question 4
score += ask_mc_question("Who wrote the play 'Romeo and Juliet'?", ["Jane Austen", "William Shakespeare", "Charles Dickens"], "William Shakespeare")

# Question 5
score += ask_mc_question("Which gas is most abundant in Earth's atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide"], "Nitrogen")

# Question 6
score += ask_mc_question("In what year did the Titanic sink?", ["1908", "1912", "1920"], "1912")

# Question 7
score += ask_mc_question("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci"], "Leonardo da Vinci")

# Question 8
score += ask_mc_question("What is the largest ocean on Earth?", ["Atlantic", "Indian", "Pacific"], "Pacific")

# Question 9
score += ask_mc_question("Which country is known as the Land of the Rising Sun?", ["China", "Korea", "Japan"], "Japan")

# Question 10
score += ask_mc_question("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Endoplasmic Reticulum"], "Mitochondria")

print("You got " + str(score) + " correct answers out of 10.")
print("Your score is " + str((score / 10) * 100) + "%.")
