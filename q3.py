import random
# Update this dictionary with questions and answers:
flashcards = {
    "question": "answer"
}

# Get a list of keys (questions) from the dictionary
#### YOUR CODE HERE
keyslist = flashcards.keys()
# Randomly sample one question
#### YOUR CODE HERE
questionnumber = random.sample(keyslist, k=1)
# Use the `input` function to ask the user the question and get their response
#### YOUR CODE HERE
answer = input(f"Your question is: {questionnumber}. What is your answer?")
# Use the question as a key to look up the answer in the dicitonary
#### YOUR CODE HERE
if answer == flashcards[questionnumber]:
    print("You are correct!")
else:
    print("You are wrong.")
# Check if the response is the same as the answer, and give the user
# feedback based on whether their response was correct or incorrect
#### YOUR CODE HERE