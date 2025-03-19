# Quiz questions and answers stored in a dictionary
questions = {
    "What is the capital of India?": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
    "Which is the largest planet?": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
    "Who developed Python?": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Bjarne Stroustrup"]
}

answers = {
    "What is the capital of India?": "B",
    "Which is the largest planet?": "C",
    "Who developed Python?": "B"
}

score = 0

print("Welcome to the Quiz Game!\n")

for index, (question, options) in enumerate(questions.items(), start=1):
    print(f"Question {index}: {question}")
    for option in options:
        print(option)

    user_answer = input("Enter your choice (A, B, C, or D): ").upper()

    correct_answer = answers[question]

    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}.\n")

print(f"Game Over! Your final score is {score}/{len(questions)}")
