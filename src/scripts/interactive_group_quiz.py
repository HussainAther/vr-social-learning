# Define quiz questions and correct answers
quiz_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What element does 'O' represent on the periodic table?", "answer": "Oxygen"},
    {"question": "What is 5 * 6?", "answer": "30"}
]

# Track answers and scores
user_scores = {user.name: 0 for user in group.users}

# Function to conduct quiz
def conduct_quiz():
    for question in quiz_questions:
        print("Question:", question["question"])
        for user in group.users:
            answer = input(f"{user.name}, enter your answer: ")
            if answer.lower() == question["answer"].lower():
                user_scores[user.name] += 1
                print(f"Correct answer, {user.name}!")
            else:
                print(f"Incorrect, {user.name}.")

    # Display scores
    print("Quiz Results:")
    for user, score in user_scores.items():
        print(f"{user}: {score} out of {len(quiz_questions)}")

# Run the quiz
conduct_quiz()

