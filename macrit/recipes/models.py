
from __future__ import annotations
from django.db import models
from abc import ABC, abstractmethod

#user class is initiated with default state
class User(models.Model):

	userid = models.IntegerField(primary_key=True)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)

	def create(cls, userid, password, email):
		cls.setUser(Unsubscribe())		
		
		return cls(userid=userid, email=email, password=password)

	def __str__(self):
		return str(self.userid) + " " + self.email

    #Changes the state of the object
	def setUser(self, state: State):
		self._state = state
		self._state.user = self

    #Get the present state
	def presentState(self):
		print(f"Elevator is in {type(self._state).__name__}")

    #Methods to execute functionality. These are called depending on the state of the object and when they are called
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
        #output error message


##This is test code if it was run seperately
# if __name__ == "__main__":
#     # The client code.

#     myUser = User(Unsubscribe())
#     myUser.presentState()

#     myUser.subscribe()

#     myUser.presentState()

#     myUser.unsubscribe()

#     myUser.presentState()

#     myUser.unsubscribe()

#     myUser.presentState()


	

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=100)
	height = models.FloatField()
	weight = models.FloatField()
	BMI = models.FloatField()
	age = models.IntegerField()
	gender = models.BooleanField(default=False)
	weight_goal = models.FloatField()
	weight_goal_time = models.DateField()
	vegeterian = models.BooleanField(default=False)
	vegan = models.BooleanField(default=False)

	def __str__(self):
		return self.first_name + ' ' + self.second_name

		
	def update(self,age, gender, height, weight, weight_goal, weight_goal_time, BMI):
		self.age = age
		self.gender = gender
		self.height = height
		self.weight = weight
		self.weight_goal = weight_goal
		self.weight_goal_time = weight_goal_time
		self.BMI = BMI

class HealthCondition(models.Model):
	abstract = True
	health_condition = models.CharField(max_length=100)
	doesUserHave = models.BooleanField(default=False)
	profile = models.ManyToManyField(Profile)

class Diary(models.Model):
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)

	def __str__(self):
		return self.profile

class Food(models.Model):
	nameOfIngredient = models.CharField(max_length=100, primary_key=True)
	intake = models.ManyToManyField(Diary)
	amountOfIngredient = models.FloatField()
	calories = models.FloatField()
	fat = models.FloatField()
	saturates = models.FloatField()
	sugar = models.FloatField()
	salt = models.FloatField()
	protein = models.FloatField()
	carbs = models.FloatField()
	fibre = models.FloatField()

	#class Meta:
		#abstract = True

	def __str__(self):
		return self.nameOfIngredient

class ShoppingList(models.Model):
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	ingredients = models.ManyToManyField(Food)

class Recipe(Food):
	nameOfRecipe = models.CharField(max_length=100, primary_key=True)
	ingredients = models.ManyToManyField(Food, related_name='+')
	instructions = models.TextField()
	tags = models.CharField(max_length=254)

	def __str__(self):
		return self.nameOfRecipe

