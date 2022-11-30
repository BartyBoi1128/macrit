from __future__ import annotations
from django.db import models
from recipes.service import *
import recipes.utils.nutrition as tits
from abc import ABC, abstractmethod

# user class is initiated with default state


class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def create(cls, userid, password, email):
        cls.setUser(Unsubscribe())

        return cls(userid=userid, email=email, password=password)

    def __str__(self):
        return str(self.userid) + " " + self.email

    # Changes the state of the object
    def setUser(self, state: State):
        self._state = state
        self._state.user = self

    # Get the present state
    def presentState(self):
        print(f"Elevator is in {type(self._state).__name__}")

    # Methods to execute functionality. These are called depending on the state of the object and when they are called
    def subscribe(self):
        self._state.subscribe()

    def unsubscribe(self):
        self._state.unsubscribe()

# Common state class for all states to be called


class State(ABC):
    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, user: User) -> None:
        self._user = user

    @abstractmethod
    def subscribe(self) -> None:
        pass

    @abstractmethod
    def unsubscribe(self) -> None:
        pass


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    BMI = models.FloatField()
    age = models.IntegerField(default=None)
    gender = models.BooleanField(default=False)
    weight_goal = models.FloatField()
    weight_goal_time = models.DateField()
    vegeterian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.second_name

    def update(self, age, gender, height, weight, weight_goal, weight_goal_time, BMI):
        print("we update model here")
        self.age = age
        print(self.age)
        self.gender = gender
        self.height = height
        self.weight = weight
        self.weight_goal = weight_goal
        self.weight_goal_time = weight_goal_time
        self.BMI = bmiCalc(height, weight)


class Subscribe(State):
    # if up button is pushed, move upwards then it changes its state to second floor.
    def unsubscribe(self) -> None:
        print("You have unsubscribed")
        self.user.setUser(Unsubscribe())

    #
    def subscribe(self) -> None:
        print("You are already subscribed")


class Unsubscribe(State):
    # if up button is pushed, move upwards then it changes its state to second floor.
    def subscribe(self) -> None:
        print("You have subscribed")
        self.user.setUser(Subscribe())

    def unsubscribe(self) -> None:
        print("You have already unsubscribed")
        # output error message


class Food(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    amount = models.FloatField()
    calories = models.FloatField()
    fat = models.FloatField()
    saturates = models.FloatField()
    sugar = models.FloatField()
    salt = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fibre = models.FloatField()

    def __str__(self):
        return self.name
# START HERE


class Nutrition(models.Model):
    # def __init__(self, profile: Profile):
    maintenance_calories = models.FloatField()
    needed_fat = models.FloatField()
    needed_saturates = models.FloatField()
    needed_sugar = models.FloatField()
    needed_protein = models.FloatField()
    needed_carbs = models.FloatField()
    needed_fibre = models.FloatField()
    needed_salt = models.FloatField(default=6)

    def update(self, age, gender, weight, height, weightGoal, weightGoalTime, BMI):
        self.maintenance_calories = tits.get_maintenance_calories(
            gender, height, weight, age)
        self.needed_fat = tits.needed_fat(self.maintenance_calories)
        self.needed_saturates = tits.needed_saturates(
            self.maintenance_calories)
        self.needed_sugar = tits.needed_sugar(self.maintenance_calories)
        self.needed_protein = tits.needed_protein(weight)
        self.needed_carbs = tits.needed_carbs(self.maintenance_calories)
        self.needed_fibre = tits.needed_fibre(self.maintenance_calories)

    # @classmethod
    # def create(cls, age, gender, weight, height, weightGoal, weightGoalTime, BMI):

    #     print("HOWYA")
    #     maintenance_calories = tits.get_maintenance_calories(
    #         gender, height, weight, age)
    #     needed_fat = tits.needed_fat(cls.maintenance_calories)
    #     needed_saturates = tits.needed_saturates(cls.maintenance_calories)
    #     needed_sugar = tits.needed_sugar(cls.maintenance_calories)
    #     needed_protein = tits.needed_protein(weight)
    #     needed_carbs = tits.needed_carbs(cls.maintenance_calories)
    #     needed_fibre = tits.needed_fibre(cls.maintenance_calories)
    #     return cls(maintenance_calories=maintenance_calories, needed_fat=needed_fat, needed_saturates=needed_saturates, needed_sugar=needed_sugar, needed_protein=needed_protein, needed_carbs=needed_carbs, needed_fibre=needed_fibre)

# ENDS HERE


class Diary(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, primary_key=True)
    intake = models.ManyToManyField(Food, blank=True)
    nutrition = models.OneToOneField(Nutrition, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.first_name + " " + self.profile.second_name + "'s diary"


class ShoppingList(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Food)


class Recipe(Food):
    ingredients = models.ManyToManyField(Food, related_name='+')
    instructions = models.TextField()
    tags = models.CharField(max_length=254)

    def __str__(self):
        return self.name
