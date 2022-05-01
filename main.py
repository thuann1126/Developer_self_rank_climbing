import random
import update_grade_table
from update_grade_table import*
import pandas

#get bot grade
def go_test():
    # Maindatory
    update_grade_table.get_test_grade("web", 5)
    update_grade_table.get_test_grade("web", 7)
    update_grade_table.get_test_grade("soft", 8)
    update_grade_table.get_test_grade("game", 7)

    update_grade_table.get_test_grade("cyber", 6)
    update_grade_table.get_test_grade("elective", 5)
go_test()

#Get player grade

#tier_list = data.query("Tier == 's'")

#tier_list["level"] = tier_list["level"].apply(lambda x: x+ random_grade)

#data.update(tier_list)

#print(data.sort_values(by=['Tier']))
print(update_grade_table.data.sort_values(by=["total-exp"], ascending=False))

update_grade_table.data.sort_values(by=["total-exp"], ascending= False).to_csv("./files/updated_rank_list.csv", index = False)

#data.sort_values(by=["total-exp"], ascending=False).to_csv("./files/updated_rank_list_v1.csv")