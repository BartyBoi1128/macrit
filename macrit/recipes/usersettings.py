from recipes.models import *
from recipes.utils.nutrition import BMI_calc

#Initiliaze our usersettings subject for observer design pattern
#usersettings has a set of observers as well as variables that will be updated for notifying our observers
class usersettings:
    def __init__(self):
        self._observers = set()
        self.profile_weight = None
        self.profile_height = None
        self.profile_weight_goal = None
        self.profile_weight_goal_time = None
        self.profile_age = None
        self.profile_gender = None
        self.profile_tags = None
        if (self.profile_height != None and self.profile_weight != None):
            self.profile_bmi = bmiCalc(usersettings.profile_height,usersettings.profile_weight)

    #Functions to add our observers to our set, and remove them from our set
    def attach(self,observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    #Function to notify our observers about the changes made in these specific variables using the update function within our observers
    def notify(self):
        for observer in self._observers:
            observer.update(self.profile_age, self.profile_gender, self.profile_weight,self.profile_height,self.profile_weight_goal,self.profile_weight_goal_time, self.profile_bmi, self.profile_tags)

    #Setter for a new tag
    def setTag(self, newTag):
        self.profile_tags = newTag

    #Setter for age
    def setAge(self, newAge):
        self.profile_age = newAge

    #Setter for gender
    def setGender(self, newGender):
        self.profile_gender = newGender

    #Setter for weight
    def setWeight(self,newWeight):
        self.profile_weight = newWeight
        self.profile_bmi = bmiCalc(self.profile_height, self.profile_weight)

    #Setter for height
    def setHeight(self, newHeight):
        self.profile_height = newHeight
        self.profile_bmi = bmiCalc(self.profile_height, self.profile_weight)

    #Setter for Weight goal
    def setWeightGoal(self, newGoal):
        self.profile_weight_goal = newGoal

    #Setter for time to achieve the weight goal
    def setWeightGoalTime(self, newGoalTime):
        self.profile_weight_goal_time = newGoalTime

    #Setter for everything
    def setAll(self, newAge, newGender, newWeight, newHeight, newGoal, newGoalTime, tags):
        self.profile_age = newAge
        self.profile_gender = newGender
        self.profile_weight = newWeight
        self.profile_height = newHeight
        self.profile_weight_goal = newGoal
        self.profile_weight_goal_time = newGoalTime
        self.profile_tags = tags
        if (self.profile_height != None and self.profile_weight != None):
            self.profile_bmi = bmiCalc(self.profile_height,self.profile_weight)

    #Getter for the tag
    def getTag(self):
        return self.profile_tags
    
    #Getter for the age
    def getAge(self):
        return self.profile_age

    #Getter for the gender
    def getGender(self):
        return self.profile_gender

    #Getter for the weitght
    def getWeight(self):
        return self.profile_weight

    #Getter for the height
    def getHeight(self):
        return self.profile_height

    #Getter for the weight goal
    def getWeightGoal(self):
        return self.getWeightGoal
    
    #Getter for time to achieve the weight goal
    def getWeightGoalTime(self):
        return self.getWeightGoalTime