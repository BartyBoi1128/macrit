from datetime import date
def bmiCalc(height, weight):
    bmi = (weight / (height*height))
    return bmi

def getCal(gender, height, weight, age):

    if gender == True:
        #Man
        calories = 66.47 +(13.75 * weight) + (5.003 * height) - (6.755 * age)

    else:
        #Woman
        calories = 655.1 +(9.563 * weight) + (1.850  * height) - (4.676 * age)

    return calories

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

def addCal(currCal, addedCal):
    currCal = addedCal + currCal
    return currCal

def removeCal(currCal, removeCal):
    currCal = currCal - removeCal
    return currCal

def neededCal(currCal, height, weight, age, gender):
    needed = getCal(gender,height, weight, age)
    leftToTake = needed - currCal
    return leftToTake

def addFat(currFat, addFat):
    currFat = currFat + addFat
    return currFat

def removeFat(currFat, removeFat):
    currFat = currFat - removeFat
    return currFat

def neededFat(currFat, height, weight, age, gender):
    needed = (getCal(gender,height, weight, age) *0.3)
    leftToTake = needed - currFat
    return leftToTake

def addSaturates(currSat, addSat):
    currSat = currSat + addSat
    return currSat

def removeSaturates(currSat, removeSat):
    currSat = currSat - removeSat
    return currSat

def neededSaturates(currSats, height, weight, age, gender):
    needed = (getCal(gender,height, weight, age) *0.1)
    leftToTake = needed - currSats
    return leftToTake

def addSugar(currSugar, addSugar):
    currSugar = currSugar + addSugar
    return currSugar

def removeSugar(currSugar, removeSugar):
    currSugar = currSugar - removeSugar
    return currSugar

def neededSugar(currSugar, height, weight, age, gender):
    needed = (getCal(gender,height, weight, age) *0.1)
    #put into grams
    needed = needed/4
    leftToTake = needed - currSugar
    return leftToTake

def addSalt(currSalt, addSalt):
    currSalt = currSalt + addSalt
    return currSalt

def removeSalt(currSalt, removeSalt):
    currSalt = currSalt - removeSalt
    return currSalt

def neededSalt(currSalt):
    leftToTake = 6 - currSalt
    # if leftToTake < 0:
    #     #how does this want to be outputted?
    #     #with a warning?
    #     leftToTake = abs(leftToTake)

    # elif leftToTake == 0:
    #     #daily goal reached!
    #     i = 1
    # else:
    #     #do something
    #     i =1
    return leftToTake

def addProtien(currProtien, addProtien):
    currProtien = currProtien + addProtien
    return currProtien

def removeProtien(currProtien, removeProtien):
    currProtien = currProtien - removeProtien
    return currProtien

def neededProtien(currProtien, weight):
    leftToTake = (weight * 0.36) - currProtien
    return leftToTake

def addCarbs(currCarbs, addCarbs):
    currCarbs = currCarbs + addCarbs
    return currCarbs

def removeCarbs(currCarbs, removeCarbs):
    currCarbs = currCarbs - removeCarbs
    return currCarbs

def neededCarbs(currCarbs, height, weight, age, gender):
    needed = (getCal(gender,height, weight, age) *0.55)
    #put into grams
    needed = needed/4
    leftToTake = needed - currCarbs
    return leftToTake

def addFibre(currFibre, addedFibre):
    currFibre = currFibre + addedFibre
    return currFibre

def removeFibre(currFibre, removeFibre):
    currFibre = currFibre - removeFibre
    return currFibre

def neededFibre(currFibre, height, weight, age, gender):
    needed = getCal(gender,height, weight, age)
    needed = needed / 1000
    needed = needed * 14
    leftToTake = needed - currFibre
    return leftToTake