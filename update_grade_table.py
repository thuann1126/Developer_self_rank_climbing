import math
import numpy as np
from grade_generator import  GradeGenerator
import pandas
#*********NOTICE comment the line below after the first call
data = pandas.read_csv("./files/rank_list.csv")
#**********NOTICE uncomment the file below after the first call
#data = pandas.read_csv("./files/updated_rank_list.csv")

data = pandas.read_csv("./files/rank_list.csv")


data.to_csv("./files/updated_rank_list_draft.csv")
# Generate grade for each tier
s_tier = GradeGenerator("s")
a_tier = GradeGenerator("a")
b_tier = GradeGenerator("b")
c_tier = GradeGenerator("c")
d_tier = GradeGenerator("d")
e_tier = GradeGenerator("e")
f_tier = GradeGenerator("f")


def get_test_grade(subject, grade):
    # Generate grade

    # Get grade, update grade, subject,
    if subject.upper() == "WEB":
        tier_s_list = data.query("Tier == 's'")
        tier_s_list["web-dev"] = tier_s_list["web-dev"].apply(lambda x: x + s_tier.getGrade())


        tier_a_list = data.query("Tier == 'a'")
        tier_a_list["web-dev"] = tier_a_list["web-dev"].apply(lambda x: x + a_tier.getGrade())


        tier_b_list = data.query("Tier == 'b'")
        tier_b_list["web-dev"] = tier_b_list["web-dev"].apply(lambda x: x + b_tier.getGrade())


        tier_c_list = data.query("Tier == 'c'")
        tier_c_list["web-dev"] = tier_c_list["web-dev"].apply(lambda x: x + c_tier.getGrade())


        tier_d_list = data.query("Tier == 'd'")
        tier_d_list["web-dev"] = tier_d_list["web-dev"].apply(lambda x: x + d_tier.getGrade())


        tier_e_list = data.query("Tier == 'e'")
        tier_e_list["web-dev"] = tier_e_list["web-dev"].apply(lambda x: x + e_tier.getGrade())


        tier_f_list = data.query("Tier == 'f'")
        tier_f_list["web-dev"] = tier_f_list["web-dev"].apply(lambda x: x + f_tier.getGrade())

        player_list = data.query("name == 'Thuan'")
        player_list["web-dev"] = player_list["web-dev"].apply(lambda x: x + grade)

        data.update(tier_s_list)
        data.update(tier_a_list)
        data.update(tier_b_list)
        data.update(tier_c_list)
        data.update(tier_d_list)
        data.update(tier_e_list)
        data.update(tier_f_list)
        data.update(player_list)
        data["no-of-tests"] += 1


    elif subject.upper() == "SOFT":
        tier_s_list = data.query("Tier == 's'")
        tier_s_list["soft-dev"] = tier_s_list["soft-dev"].apply(lambda x: x + s_tier.getGrade())


        tier_a_list = data.query("Tier == 'a'")
        tier_a_list["soft-dev"] = tier_a_list["soft-dev"].apply(lambda x: x + a_tier.getGrade())


        tier_b_list = data.query("Tier == 'b'")
        tier_b_list["soft-dev"] = tier_b_list["soft-dev"].apply(lambda x: x + b_tier.getGrade())


        tier_c_list = data.query("Tier == 'c'")
        tier_c_list["soft-dev"] = tier_c_list["soft-dev"].apply(lambda x: x + c_tier.getGrade())


        tier_d_list = data.query("Tier == 'd'")
        tier_d_list["soft-dev"] = tier_d_list["soft-dev"].apply(lambda x: x + d_tier.getGrade())


        tier_e_list = data.query("Tier == 'e'")
        tier_e_list["soft-dev"] = tier_e_list["soft-dev"].apply(lambda x: x + e_tier.getGrade())


        tier_f_list = data.query("Tier == 'f'")
        tier_f_list["soft-dev"] = tier_f_list["soft-dev"].apply(lambda x: x + f_tier.getGrade())

        player_list = data.query("name == 'Thuan'")
        player_list["soft-dev"] = player_list["soft-dev"].apply(lambda x: x + grade)

        data.update(tier_s_list)
        data.update(tier_a_list)
        data.update(tier_b_list)
        data.update(tier_c_list)
        data.update(tier_d_list)
        data.update(tier_e_list)
        data.update(tier_f_list)
        data.update(player_list)
        data["no-of-tests"] += 1


    elif subject.upper() == "GAME":
        tier_s_list = data.query("Tier == 's'")
        tier_s_list["game-dev"] = tier_s_list["game-dev"].apply(lambda x: x + s_tier.getGrade())


        tier_a_list = data.query("Tier == 'a'")
        tier_a_list["game-dev"] = tier_a_list["game-dev"].apply(lambda x: x + a_tier.getGrade())


        tier_b_list = data.query("Tier == 'b'")
        tier_b_list["game-dev"] = tier_b_list["game-dev"].apply(lambda x: x + b_tier.getGrade())


        tier_c_list = data.query("Tier == 'c'")
        tier_c_list["game-dev"] = tier_c_list["game-dev"].apply(lambda x: x + c_tier.getGrade())


        tier_d_list = data.query("Tier == 'd'")
        tier_d_list["game-dev"] = tier_d_list["game-dev"].apply(lambda x: x + d_tier.getGrade())


        tier_e_list = data.query("Tier == 'e'")
        tier_e_list["game-dev"] = tier_e_list["game-dev"].apply(lambda x: x + e_tier.getGrade())


        tier_f_list = data.query("Tier == 'f'")
        tier_f_list["game-dev"] = tier_f_list["game-dev"].apply(lambda x: x + f_tier.getGrade())

        player_list = data.query("name == 'Thuan'")
        player_list["game-dev"] = player_list["game-dev"].apply(lambda x: x + grade)

        data.update(tier_s_list)
        data.update(tier_a_list)
        data.update(tier_b_list)
        data.update(tier_c_list)
        data.update(tier_d_list)
        data.update(tier_e_list)
        data.update(tier_f_list)
        data.update(player_list)
        data["no-of-tests"] += 1

    elif subject.upper() == "CYBER":
        tier_s_list = data.query("Tier == 's'")
        tier_s_list["cyber-secu"] = tier_s_list["cyber-secu"].apply(lambda x: x + s_tier.getGrade())


        tier_a_list = data.query("Tier == 'a'")
        tier_a_list["cyber-secu"] = tier_a_list["cyber-secu"].apply(lambda x: x + a_tier.getGrade())


        tier_b_list = data.query("Tier == 'b'")
        tier_b_list["cyber-secu"] = tier_b_list["cyber-secu"].apply(lambda x: x + b_tier.getGrade())


        tier_c_list = data.query("Tier == 'c'")
        tier_c_list["cyber-secu"] = tier_c_list["cyber-secu"].apply(lambda x: x + c_tier.getGrade())


        tier_d_list = data.query("Tier == 'd'")
        tier_d_list["cyber-secu"] = tier_d_list["cyber-secu"].apply(lambda x: x + d_tier.getGrade())


        tier_e_list = data.query("Tier == 'e'")
        tier_e_list["cyber-secu"] = tier_e_list["cyber-secu"].apply(lambda x: x + e_tier.getGrade())


        tier_f_list = data.query("Tier == 'f'")
        tier_f_list["cyber-secu"] = tier_f_list["cyber-secu"].apply(lambda x: x + f_tier.getGrade())

        player_list = data.query("name == 'Thuan'")
        player_list["cyber-secu"] = player_list["cyber-secu"].apply(lambda x: x + grade)

        data.update(tier_s_list)
        data.update(tier_a_list)
        data.update(tier_b_list)
        data.update(tier_c_list)
        data.update(tier_d_list)
        data.update(tier_e_list)
        data.update(tier_f_list)
        data.update(player_list)
        data["no-of-tests"] += 1


    elif subject.upper() == "ELECTIVE":
        tier_s_list = data.query("Tier == 's'")
        tier_s_list["elective"] = tier_s_list["elective"].apply(lambda x: x + s_tier.getGrade())


        tier_a_list = data.query("Tier == 'a'")
        tier_a_list["elective"] = tier_a_list["elective"].apply(lambda x: x + a_tier.getGrade())


        tier_b_list = data.query("Tier == 'b'")
        tier_b_list["elective"] = tier_b_list["elective"].apply(lambda x: x + b_tier.getGrade())


        tier_c_list = data.query("Tier == 'c'")
        tier_c_list["elective"] = tier_c_list["elective"].apply(lambda x: x + c_tier.getGrade())


        tier_d_list = data.query("Tier == 'd'")
        tier_d_list["elective"] = tier_d_list["elective"].apply(lambda x: x + d_tier.getGrade())


        tier_e_list = data.query("Tier == 'e'")
        tier_e_list["elective"] = tier_e_list["elective"].apply(lambda x: x + e_tier.getGrade())


        tier_f_list = data.query("Tier == 'f'")
        tier_f_list["elective"] = tier_f_list["elective"].apply(lambda x: x + f_tier.getGrade())


        player_list = data.query("name == 'Thuan'")
        player_list["elective"] = player_list["elective"].apply(lambda x: x + grade)

        data.update(tier_s_list)
        data.update(tier_a_list)
        data.update(tier_b_list)
        data.update(tier_c_list)
        data.update(tier_d_list)
        data.update(tier_e_list)
        data.update(tier_f_list)
        data.update(player_list)
        data["no-of-tests"] += 1


    # update the total-exp, level, no-of-tests, avg comlumn
    data["total-exp"] = data["web-dev"] + data["soft-dev"] + data["game-dev"] + data["cyber-secu"] + data["elective"]
    data["level"] = data["total-exp"].div(50)
    data["level"] = data["level"].round()
    data["avg"] = data["total-exp"].div(data["no-of-tests"])
    data["avg"] = data["avg"].round(2)


    # update grade, subjects, total
    # check if the player is level up or not

    # update type, no of types, avg
    # check if the type is level up