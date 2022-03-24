from questions import question_data

class Question:
    def __init__(self, question, tanswer):
        self.question = question
        self.tanswer = tanswer

    def choose_answer(self, answer):
        if answer == self.tanswer:
            return 1

class Quiz:
    def __init__(self, name, q_list):
        self.name = name
        self.question_list = q_list
        self.score = 0
        self.question_num = 0

    def nxt_question(self):
        this_question = self.question_list
        self.question_num += 1
        uanswer = input(f"{self.question_num}: {this_question.question} (True/False): ")
        self.right_answer(uanswer, this_question.answer)
    
    def questions_left(self):
        return self.question_num < len(self.question_list)

question_list=[]
for i in question_list:
    question_q = i["question"]
    question_a = i["answer"]
    new_question = Question(question_q, question_a)
    question_list.append(new_question)

def main():
    pass
if __name__ == "__main__":
    main()