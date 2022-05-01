import random


class GradeGenerator:
    def __init__(self, tier):
        self.tier_list = tier

    def getGrade(self):
        a_grade = 0
        if self.tier_list == "s":
            a_grade = random.randint(8, 10)
            return a_grade
        elif self.tier_list == "a":
            a_grade = random.randint(7, 9)
            return a_grade
        elif self.tier_list == "b":
            a_grade = random.randint(6, 8)
            return a_grade
        elif self.tier_list == "c":
            a_grade = random.randint(5, 7)
            return a_grade
        elif self.tier_list == "d":
            a_grade = random.randint(4, 6)
            return a_grade
        elif self.tier_list == "e":
            a_grade = random.randint(3, 5)
            return a_grade
        elif self.tier_list == "f":
            a_grade = random.randint(0, 3)
            return a_grade


