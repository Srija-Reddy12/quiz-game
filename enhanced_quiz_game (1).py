
import time
import random

# Quiz questions
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used to write Python programs?",
        "options": ["A. Python", "B. Java", "C. C++", "D. HTML"],
        "answer": "A"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
        "answer": "C"
    },
    {
        "question": "What is the output of 3 + 2 * 2?",
        "options": ["A. 10", "B. 7", "C. 8", "D. 6"],
        "answer": "B"
    },
    {
    "question": "Which keyword is used to define a function in Python?",
    "options": ["A. func", "B. define", "C. def", "D. function"],
    "answer": "C"
    },
    {
    "question": "Which planet is known as the Red Planet?",
    "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    "answer": "B"
    },
    {
    "question": "What is the result of 9 // 2 in Python?",
    "options": ["A. 4.5", "B. 5", "C. 4", "D. 5.0"],
    "answer": "B"
    },
    {
    "question": "Who is the current CEO of Tesla (as of 2024)?",
    "options": ["A. Jeff Bezos", "B. Elon Musk", "C. Tim Cook", "D. Sundar Pichai"],
    "answer": "B"
    },
    {
    "question": "What does HTML stand for?",
    "options": ["A. Hyper Trainer Marking Language", "B. Hyper Text Marketing Language", "C. Hyper Text Markup Language", "D. Hyper Text Markup Leveler"],
    "answer": "C"
    },

    ]

# Shuffle questions
random.shuffle(quiz)

# Get user name
name = input("Enter your name: ")

score = 0

# Ask questions with timer
for q in quiz:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)

    start_time = time.time()
    user_ans = input("Enter your answer (A/B/C/D): ").upper()
    end_time = time.time()

    if end_time - start_time > 10:
        print("Time's up! You didn't answer in 10 seconds.")
        continue

    if user_ans == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}\n")

# Final score and percentage
percentage = (score / len(quiz)) * 100
print(f"Your final score is: {score}/{len(quiz)}")
print(f"You got {percentage:.2f}% correct answers.")

# Save results to file
with open("quiz_results.txt", "a") as f:
    f.write(f"{name} scored {score}/{len(quiz)} ({percentage:.2f}%)\n")
print("Your result has been saved to 'quiz_results.txt'")
