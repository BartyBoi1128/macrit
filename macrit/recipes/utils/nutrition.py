import numpy as np

    # Decorator that changes every value of the dictionary to be formatted as consumed/needed
def dict_decorator(func, diary, nutrition):
    def inner(func):
        plain_dict = func(nutrition)
        detailed_dict = dict()
        for key, value in plain_dict.items():
            consumed_key = key.replace('needed', 'consumed')
            macro_key = key.replace('needed_','')
            consumed = 0
            for food in diary.intake.all():
                consumed += getattr(food, macro_key)
            detailed_dict[consumed_key] = (consumed , value)

        # detailed_dict = {
        #     key.replace('needed', 'consumed'): str(np.sum(np.array([getattr(food, key.replace('needed_','')) for food in diary.intake.all()]))) + "/" + str(value) for key, value in zip(plain_dict.keys(), plain_dict.values())
        # }
        return detailed_dict
    return inner
    
def generate_dict(nutrition):
    return {
        'needed_calories': nutrition.maintenance_calories,
        'needed_fat': nutrition.needed_fat,
        'needed_saturates': nutrition.needed_saturates,
        'needed_sugar': nutrition.needed_sugar,
        'needed_protein': nutrition.needed_protein,
        'needed_carbs': nutrition.needed_carbs,
        'needed_fibre': nutrition.needed_fibre,
        'needed_salt': nutrition.needed_salt
    }

def get_maintenance_calories(gender, height, weight, age):

    #Calculates the different amount of calories the user needs based on weight height age and gender
    if gender == True:
        #Man
        calories = 66.47 +(13.75 * weight) + (5.003 * height) - (6.755 * age)

    else:
        #Woman
        calories = 655.1 +(9.563 * weight) + (1.850  * height) - (4.676 * age)

    return calories


#Calculate fat needed
def needed_fat(maintenance_calories):
    return (maintenance_calories / 10)


#Calculates saturates needed
def needed_saturates(maintenance_calories):
    return (maintenance_calories / 10)


#Calculates sugar needed
def needed_sugar(maintenance_calories):
    return (maintenance_calories / 40)


#Calculates protein needed
def needed_protein(weight):
    return (weight * 0.36)


#Calculates carbs needed
def needed_carbs(maintenance_calories):
    return (maintenance_calories * 0.55 / 4)


#Calculates fibre needed
def needed_fibre(maintenance_calories):
    return (maintenance_calories / 1000 * 14)


