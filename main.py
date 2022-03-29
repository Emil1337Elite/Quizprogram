from random import shuffle

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
        print(f"Pick one of the following answers: {self.alternative}")

class Quiz:
    def __init__(self, name, questions:list, score, num):
        self.name = name
        self.questions = questions
        self.score = score
        self.num = num
    
    def ask(self):
        askquestion = shuffle(self.questions)
        for i in self.questions:
            print(i.question)
            q=0
            for x in i.alternative:
                q += 1
                print(f"{q}: {x}")
            answer = input("Write the letter of your answer: ")
            if i.chkanswer(answer) == 1:
                self.score += 1
                self.num += 1
                print(f"""You answered correctly. Your current score is {self.score}.\n""")
            else:
                self.num += 1
                print(f"Current score: {self.score}\n")
    
    def get_score(self):
        return self.score

def main():
    
    #questions
    q1 = Question("When did the first Star Wars movie premiere?","c",["a) 18th September 1974","b) 2nd June 1981","c) 25th May 1977","d) 11th October 2000"])
    q2 = Question("Which is the largest US state by land area?","a",["a) Alaska","b) Hawaii","c) Texas","d) Wisconsin"])
    q3 = Question("How many republics did the Soviet Union consist of?","d",["a) 10","b) 12","c) 18","d) 15"])
    q4 = Question("What year did the first humans land on the Moon?","a",["a) 1969","b) 1973","c) 2006","d) 1959"])
    q5 = Question("What planet is closest to the Sun?","b",["a) Venus","b) Mecury","c) Earth","d) Jupiter"])
    q6 = Question("What was the eastern part of Rome called after it split in two?","b",["a) Assyria","b) Byzantium","c) Mesopotamia","d) Aztec Empire"])
    q7 = Question("Who was the worlds first billionaire?","c",["a) Donald Trump","b) Elon Musk","c) John D. Rockefeller","d) Henry Ford"])
    q8 = Question("What is the most populated city in the world?","d",["a) Jakarta","b) London","c) Shanghai","d) Tokyo"])

    quiz = Quiz("The Quiz", [q1 ,q2 ,q3 ,q4 ,q5 ,q6 ,q7 ,q8 ],0 ,1)

    start = input("Welcome to the quiz! Press 1 to start quiz.")
    if start == ("1"):
        quiz.ask()
        print("That was the last question.")
        pass
if __name__ == "__main__":
    main()