from recipes.models import Diary, Food
import numpy as np

class Nutrition():
    def __init__(self, gender, height, weight, age):
        self.maintenance_calories = get_maintenance_calories(gender, height, weight, age)
        self.needed_fat = needed_fat(self.maintenance_calories)
        self.needed_saturates = needed_saturates(self.maintenance_calories)
        self.needed_sugar = needed_sugar(self.maintenance_calories)
        self.needed_protein = needed_protein(weight)
        self.needed_carbs = needed_carbs(self.maintenance_calories)
        self.needed_fibre = needed_carbs(self.maintenance_calories)
        self.needed_salt = 6
    
    # Decorator that changes every value of the dictionary to be formatted as consumed/needed
    def dict_decorator(func, diary: Diary):
        def inner(self):
            plain_dict = func(self)
            detailed_dict = {
                key.replace('needed', 'consumed'): str(np.sum(np.array([getattr(food, key.replace('needed_','')) for food in Food.objects.filter(intake=diary)]))) + "/" + value for key, value in zip(plain_dict.keys(), plain_dict.values())
            }
            return detailed_dict
        return inner
        

    @dict_decorator
    @classmethod
    def generate_dict(cls):
        return {
            'needed_calories': cls.maintenance_calories,
            'needed_fat': cls.needed_fat,
            'needed_saturates': cls.needed_saturates,
            'needed_sugar': cls.needed_sugar,
            'needed_protein': cls.needed_protein,
            'needed_carbs': cls.needed_carbs,
            'needed_fibre': cls.needed_fibre,
            'needed_salt': cls.needed_salt
        }


    
def get_maintenance_calories(gender, height, weight, age):

    if gender == True:
        #Man
        calories = 66.47 +(13.75 * weight) + (5.003 * height) - (6.755 * age)

    else:
        #Woman
        calories = 655.1 +(9.563 * weight) + (1.850  * height) - (4.676 * age)

    return calories

def needed_fat(maintenance_calories):
    return (maintenance_calories / 10)


def needed_saturates(maintenance_calories):
    return (maintenance_calories / 10)


def needed_sugar(maintenance_calories):
    return (maintenance_calories / 40)


def needed_protein(weight):
    return (weight * 0.36)


def needed_carbs(maintenance_calories):
    return (maintenance_calories * 0.55 / 4)


def needed_fibre(maintenance_calories):
    return (maintenance_calories / 1000 * 14)


