from random import shuffle,choice

class Question:
    def __init__(self, question, tanswer, alternative:list):
        self.question = question
        self.tanswer = tanswer
        self.alternative = alternative

    def chkanswer(self, answer):
        if answer == self.tanswer:
            return 1
        else: 
            print(f"Your answer is incorrect. The correct answer was: {self.tanswer}")
    
    def write_alternatives(self):
        print(f"Pick one of the following answers: {self.alteranative}")

class Quiz:
    def __init__(self, name, questions:list, score):
        self.name = name
        self.questions = questions
        self.score = score
    
    def ask(self):
        for i in self.questions:
            print(i.question)
            q=0
        for x in i.alternative:
            q += 1
            print(f"{q}: {x}")
        answer = input("Write your answer: ")
        if i.chkanswer(answer) == 1:
            self.score += 1
            print(f"Your current score is {self.score}")
        else:
            print(f"Your answer is incorrect. Current score: {self.score}\n")
        
    def get_name(self):
        return self.name
    
    def get_score(self):
        return self.score
    
    # def start(self):
    #     print(f"Welcome to the {self.name}.\n")

def main():
   quiz = Quiz("The Cool Quiz",[], 0)
   
if __name__ == "__main__":
    main()