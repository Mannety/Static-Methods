class Student:
    def __init__(self, scores = []):
        self.scores = scores
    
    def avg(self):
        return round(sum(self.scores) / len(self.scores))

    @staticmethod
    def notice():
        return "Exams next week!"

print(Student.notice())