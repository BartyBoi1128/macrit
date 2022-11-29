from datetime import date
def bmiCalc(height, weight):
    height = height * 0.01
    bmi = (weight / (height*height))
    return bmi


def age(DOB):
    today = date.today()
    one_or_zero = ((today.month, today.day) < (DOB.month, DOB.day))
    year_difference = today.year - DOB.year
    age = year_difference - one_or_zero
    return age

def poundstokg(weightInLBS):
    weight = (weightInLBS *0.45359237)
    return weight

def feetToCm(feet, inches):
    inches = ((feet *12) + inches)
    height = inches * 2.54
    return height
