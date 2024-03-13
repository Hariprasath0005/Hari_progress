class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score=0
        self.question_list = q_list

    def still_has_question(self):
        if self.question_number< len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_input = input(f"{self.question_number}: {current_question.text}, True or False: ").lower()
        self.check_ans(user_input,current_question.answer)
    def check_ans(self,user_input,correct_ans):
        if user_input == correct_ans.lower():
            self.score+=1
            print("You are right!")
            
        else:
            print("Wrong Answer")
        print(f"Correct answer is {correct_ans}")
        print(f"You score: {self.score}/{self.question_number} \n")