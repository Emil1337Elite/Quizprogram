from random import choice

class Question:
    def __init__(self, question, tanswer, alternative : list):
        self.question = question
        self.tanswer = tanswer
        self.alternative = alternative

    def choose_answer(self, answer):
        if answer == self.tanswer:
            return 1

    def write_alternatives(self):
        print(f"These are the alternatives: {self.alternative}")

class Quiz:
    def __init__(self, name, questions : list, score):
        self.name = name
        self.questions = questions
        self.score = score

    def ask_question(self):
        for x in len(self.questions):
            choice(Question)

    if __name__ == "__main__":
        main()