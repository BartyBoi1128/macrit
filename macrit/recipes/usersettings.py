from service import *

class usersettings:
    def __init__(self):
        self._obververs = set()
        self.profile_weight = None
        self.profile_height = None
        self.profile_weight_goal = None
        self.profile_weight_goal_time = None
        self.profile_bmi = bmiCalc(usersettings.profile_height,usersettings.profile_weight)

    def attach(self,observer):
        observer.user = self
        self._observers.add(observer)

    def detach(self, observer):
        observer.user = None
        self._observers.discard(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self.profile_weight,self.profile_height,self.profile_weight_goal,self.profile_weight_goal_time, self.profile_bmi)

    #Setters
    def setWeight(self,newWeight):
        self.profile_weight = newWeight
        bmiCalc(self.profile_height, self.profile_weight)

    def setHeight(self, newHeight):
        self.profile_height = newHeight
        bmiCalc(self.profile_height, self.profile_weight)

    def setWeightGoal(self, newGoal):
        self.profile_weight_goal = newGoal

    def setWeightGoalTime(self, newGoalTime):
        self.profile_weight_goal_time = newGoalTime

    #Getters
    def getWeight(self):
        return self.profile_weight

    def getHeight(self):
        return self.profile_height

    def getWeightGoal(self):
        return self.getWeightGoal
    
    def getWeightGoalTime(self):
        return self.getWeightGoalTime