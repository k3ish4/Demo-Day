from color_quiz import ColorQuiz

if __name__ == '__main__':

    quiz = ColorQuiz()

    print("Welcome to my color quiz! I'll ask some yes or no questions and try to guess your favorite color.")

    ColorQuiz.ask_specific_question(1)
    answer = input()
    if answer.lower == "yes":
        ColorQuiz.add_point('red')
        ColorQuiz.add_point('yellow')
        ColorQuiz.add_point('blue')
    else:
        ColorQuiz.ask_specific_question(2)
        answer = input()
        if answer.lower == "yes":
            ColorQuiz.add_point('orange')
            ColorQuiz.add_point('green')
            ColorQuiz.add_point('violet')

    ColorQuiz.ask_specific_question(3)
    answer = input()
    if answer.lower == "yes":
        ColorQuiz.add_point('red')
        ColorQuiz.add_point('orange')
        ColorQuiz.add_point('yellow')
    else:
        ColorQuiz.ask_specific_question(4)
        answer = input()
        if answer == "yes":
            ColorQuiz.add_point('green')
            ColorQuiz.add_point('blue')
            ColorQuiz.add_point('violet')

    i = 5
    answer = 'no'
    while answer.lower != 'yes': 
        ColorQuiz.ask_specific_question(i)
        answer = input()
        i+=1
    
    if (i-1)== 5:
        ColorQuiz.add_point('red')
    if (i-1)== 6:
        ColorQuiz.add_point('orange')
    if (i-1)== 7:
        ColorQuiz.add_point('yellow')
    if (i-1)== 8:
        ColorQuiz.add_point('green')
    if (i-1)== 9:
        ColorQuiz.add_point('blue')
    if (i-1)== 10:
        ColorQuiz.add_point('violet')

    ColorQuiz.compute_result()
    