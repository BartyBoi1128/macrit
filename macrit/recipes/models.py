from __future__ import annotations
from django.db import models
import recipes.utils.nutrition as nutrition
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

#Profile model, with a one to one relationship with user as every profile will have a user
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
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    tags = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.second_name

	#Update function that gets called by our "usersettings" subject
    def update(self, age, gender, height, weight, weight_goal, weight_goal_time, BMI, tags):
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.weight_goal = weight_goal
        self.weight_goal_time = weight_goal_time
        self.BMI = bmiCalc(height, weight)
        self.tags = tags


class Subscribe(State):
    # if up button is pushed, move upwards then it changes its state to second floor.
    def unsubscribe(self) -> None:
        print("You have unsubscribed")
        self.user.setUser(Unsubscribe())

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
    tags = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

#Nutrition model that gets used with our Diary
class Nutrition(models.Model):
    maintenance_calories = models.FloatField()
    needed_fat = models.FloatField()
    needed_saturates = models.FloatField()
    needed_sugar = models.FloatField()
    needed_protein = models.FloatField()
    needed_carbs = models.FloatField()
    needed_fibre = models.FloatField()
    needed_salt = models.FloatField(default=6)

    def update(self, age, gender, weight, height, weightGoal, weightGoalTime, BMI, tags):
        self.maintenance_calories = nutrition.get_maintenance_calories(
            gender, height, weight, age)
        self.needed_fat = nutrition.needed_fat(self.maintenance_calories)
        self.needed_saturates = nutrition.needed_saturates(
            self.maintenance_calories)
        self.needed_sugar = nutrition.needed_sugar(self.maintenance_calories)
        self.needed_protein = nutrition.needed_protein(weight)
        self.needed_carbs = nutrition.needed_carbs(self.maintenance_calories)
        self.needed_fibre = nutrition.needed_fibre(self.maintenance_calories)

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

    def __str__(self):
        return self.name
