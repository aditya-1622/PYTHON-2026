# QUIZ GAME WITH SCORE TRACKING

# This program:
# 1: Stores a list of quiz questions (each with options and a correct answer)
# 2: Shuffles the questions randomly each time
# 3: Asks the user each question and checks their answer
# 4: Tracks the score and shows a final result


import random   

# Step 1: Store all quiz questions as a list of dictionaries
# Each dictionary has: the question text, 4 options, and the correct answer


questions = [
    {
        "question": "What is the capital of India?",
        "options": {"A": "Mumbai", "B": "New Delhi", "C": "Kolkata", "D": "Chennai"},
        "answer": "B"
    },
    {
        "question": "Which language is this program written in?",
        "options": {"A": "Java", "B": "C++", "C": "Python", "D": "JavaScript"},
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": {"A": "Central Process Unit", "B": "Central Processing Unit",
                    "C": "Computer Personal Unit", "D": "Central Processor Utility"},
        "answer": "B"
    },
    {
        "question": "Which data type is used to store True/False values in Python?",
        "options": {"A": "int", "B": "str", "C": "bool", "D": "float"},
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {"A": "//", "B": "#", "C": "<!-- -->", "D": "/* */"},
        "answer": "B"
    }
]



# Function to ask a single question and check if the answer is correct...

def ask_question(question_data):
    print(f"\n{question_data['question']}")

    # Print all 4 options (A, B, C, D)
    for option_key, option_text in question_data["options"].items():
        print(f"  {option_key}. {option_text}")

    # Take user's answer, convert to uppercase in case if they type lowercase
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == question_data["answer"]:
        print("Correct!")
        return True   
    else:
        correct_option = question_data["answer"]
        correct_text = question_data["options"][correct_option]
        print(f"Wrong! The correct answer was {correct_option}. {correct_text}")
        return False   



# Function to run the entire quiz once..

def run_quiz():
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)

    score = 0  
    total_questions = len(shuffled_questions)

    print("\n===== QUIZ STARTED =====")

    # Loop through each question one by one.

    for question_data in shuffled_questions:
        is_correct = ask_question(question_data)
        if is_correct:
            score += 1

    show_result(score, total_questions)



# Function to display the final score and grade..

def show_result(score, total_questions):
    percentage = (score / total_questions) * 100

    print("\n===== QUIZ FINISHED =====")
    print(f"Score: {score} / {total_questions}")
    print(f"Percentage: {percentage:.2f}%")

    # Decide the grade/message based on percentage..

    if percentage >= 80:
        print("Result: Excellent! 🎉")
    elif percentage >= 50:
        print("Result: Good, but you can improve.")
    else:
        print("Result: Needs Improvement. Keep practicing!")



# MAIN PROGRAM
# Keeps asking the user if they want to play again..

if __name__ == "__main__":

    while True:
        run_quiz()

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break