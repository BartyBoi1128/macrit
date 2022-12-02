from recipes.warning import glutenWarning, vegetarianWarning, macrosWarning
from recipes.models import Food

#Checker for all of the macros that you are not going over
def check_macros(dict, food : Food):
    if food.calories > dict["consumed_calories"][1] - dict["consumed_calories"][0]:
        return "calories"
    elif food.protein > dict["consumed_protein"][1] - dict["consumed_protein"][0]:
        return "protein"
    elif food.carbs > dict["consumed_carbs"][1] - dict["consumed_carbs"][0]:
        return "carbs"
    elif food.fat > dict["consumed_fat"][1] - dict["consumed_fat"][0]:
        return "fat"
    elif food.sugar > dict["consumed_sugar"][1] - dict["consumed_sugar"][0]:
        return "sugar"
    elif food.fibre > dict["consumed_fibre"][1] - dict["consumed_fibre"][0]:
        return "fibre"
    elif food.salt > dict["consumed_salt"][1] - dict["consumed_salt"][0]:
        return "salt"
    elif food.saturates > dict["consumed_saturates"][1] - dict["consumed_saturates"][0]:
        return "saturates"
    else:
        return -1
    
#Checking if any of the food is outside of what the user can have
def buildWarning(food : Food, macro_dict):
    macroTypes = ["calories", "protein", "carbs", "fat", "sugar", "fibre", "salt", "saturates"]
    warningType = check_macros(macro_dict, food)
    if food.tags == None:
        return -1
    elif "gluten" in food.tags:
        return glutenWarning()
    elif "vegetarian" in food.tags:
        return vegetarianWarning()
    elif warningType in macroTypes:
        warning = macrosWarning()
        warning.setType(warningType)
        return warning
    else:
        return -1
