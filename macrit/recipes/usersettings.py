from recipes.service import *

class usersettings:
    def __init__(self):
        self._obververs = set()
        self.profile_weight = None
        self.profile_height = None
        self.profile_weight_goal = None
        self.profile_weight_goal_time = None
        self.profile_age = None
        self.profile_gender = None
        if (self.profile_height != None and self.profile_weight != None):
            self.profile_bmi = bmiCalc(usersettings.profile_height,usersettings.profile_weight)

    def attach(self,observer):
        observer.user = self
        self._observers.add(observer)

    def detach(self, observer):
        observer.user = None
        self._observers.discard(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(observer, self.profile_age, self.profile_gender, self.profile_weight,self.profile_height,self.profile_weight_goal,self.profile_weight_goal_time, self.profile_bmi)

    #Setters
    def setAge(self, newAge):
        self.profile_age = newAge

    def setGender(self, newGender):
        self.profile_gender = newGender

    def setWeight(self,newWeight):
        self.profile_weight = newWeight
        self.profile_bmi = bmiCalc(self.profile_height, self.profile_weight)

    def setHeight(self, newHeight):
        self.profile_height = newHeight
        self.profile_bmi = bmiCalc(self.profile_height, self.profile_weight)

    def setWeightGoal(self, newGoal):
        self.profile_weight_goal = newGoal

    def setWeightGoalTime(self, newGoalTime):
        self.profile_weight_goal_time = newGoalTime

    def setAll(self, newAge, newGender, newWeight, newHeight, newGoal, newGoalTime):
        self.profile_age = newAge
        self.profile_gender = newGender
        self.profile_weight = newWeight
        self.profile_height = newHeight
        self.profile_weight_goal = newGoal
        self.profile_weight_goal_time = newGoalTime
        if (self.profile_height != None and self.profile_weight != None):
            self.profile_bmi = bmiCalc(usersettings.profile_height,usersettings.profile_weight)
        

    #Getters
    def getAge(self):
        return self.profile_age

    def getGender(self):
        return self.profile_gender

    def getWeight(self):
        return self.profile_weight

    def getHeight(self):
        return self.profile_height

    def getWeightGoal(self):
        return self.getWeightGoal
    
    def getWeightGoalTime(self):
        return self.getWeightGoalTime