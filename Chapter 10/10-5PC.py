# This program creates a Trivia class and
# then produces a two player trivia game.
# It then displays the correct answer and
# determines a winner.

class Trivia:
    def __init__(self, question, ans1, ans2, ans3, ans4, correct):
        self.__ques = question
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans4 = ans4
        self.__correct = correct

        # Class attributes
    def set_question(self, question):
        self.__ques = question
    def set_answer1(self, ans1):
        self.__ans1 = ans1
    def set_answer2(self, ans2):
        self.__ans2 = ans2
    def set_answer3(self, ans3):
        self.__ans3 = ans3
    def set_answer4(self, ans4):
        self.__ans4 = ans4
    def set_correct(self, correct):
        self.__correct = correct

        # Retrieves the accesors for the class
    def get_question(self):
        return self.__ques
    def get_answer1(self):
        return self.__ans1
    def get_answer2(self):
         return self.__ans2
    def get_answer3(self):
         return self.__ans3
    def get_answer4(self):
        return self.__ans4
    def get_correct(self):
        return self.__correct

        # Displays the question and choices
    def ask_question(self):
        print('Question: ' + self.__ques + \
                '\nAnswers:' + \
                '\n1. ' + self.__ans1 + \
                '\n2. ' + self.__ans2 + \
                '\n3. ' + self.__ans3 + \
                '\n4. ' + self.__ans4)

# Trivia Game function
def trivia_game(question_objs):
    player1_correct = 0
    player2_correct = 0

    print('\nTrivia Quiz')
    print('-------------')

    for i in range(10):
        if i % 2 == 0:
            print("\nPlayer 1's Turn: ")
            question_objs[i].ask_question()
            choice = int(input('Enter your answer (1-4): '))
            if choice == question_objs[i].get_correct():
                player1_correct += 1
        else:
            print("\nPlayer 2's Turn: ")
            question_objs[i].ask_question()
            choice = int(input('Enter your answer (1-4): '))
            if choice == question_objs[i].get_correct():
                player2_correct += 1

    print("Player 1's Score:", player1_correct)
    print("Player 2's Score:", player2_correct)
    if player1_correct > player2_correct:
        print('Player 1 has Won!')
    elif player1_correct < player2_correct:
        print('Player 2 has Won!')
    else:
        print('It was a draw.')

# The main function
def main():
    questions = []
    answers = [4, 2, 4, 3, 1, 3, 2, 2, 3, 4]
    for i in range(10):
        ques = 'Question #' + str(i + 1) + '\n--------------------' + \
               '\nWhat is 2+2?' + '\n--------------------'           
        ans1 = '12'
        ans2 = '16'
        ans3 = '3'
        ans4 = '4'
        question = Trivia(ques, ans1, ans2, ans3, ans4, answers[i])
        questions += [question]
    trivia_game(questions)

# Call the main function
main()
    
                  
