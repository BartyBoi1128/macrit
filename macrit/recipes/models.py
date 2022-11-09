from django.db import models

# Create your models here.
class User(models.Model):
	userid = models.IntegerField(primary_key=True)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)

	def __str__(self):
		return self.userid + ' ' + self.email

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

	def update(self, weight, height, weightGoal , weightGoalTime, BMI):
		self.height = height
		self.weight = weight
		self.weight_goal = weightGoal
		self.weight_goal_time = weightGoalTime
		self.BMI = BMI

class HealthCondition(models.Model):
	abstract = True
	health_condition = models.CharField(max_length=100)
	doesUserHave = models.BooleanField(default=False)
	profile = models.ManyToManyField(Profile)

class Diary(models.Model):
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	dateOfIntake = models.DateField(primary_key=True)

	def __str__(self):
		return self.dateOfIntake

class Ingredient(models.Model):
	nameOfIngredient = models.CharField(max_length=100, primary_key=True)
	intake = models.ManyToManyField(Diary)
	amountOfIngredient = models.FloatField()

	def __str__(self):
		return self.nameOfIngredient

class ShoppingList(models.Model):
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	ingredients = models.ManyToManyField(Ingredient)

class Recipe(models.Model):
	nameOfRecipe = models.CharField(max_length=100, primary_key=True)
	ingredients = models.ManyToManyField(Ingredient)
	instructions = models.TextField()
	tags = models.CharField(max_length=254)

	def __str__(self):
		return self.nameOfRecipe

class Macro(models.Model):
	diary = models.ManyToManyField(Diary)
	ingredient = models.ManyToManyField(Ingredient)
	abstract = True
	calories = models.FloatField()
	fat = models.FloatField()
	saturates = models.FloatField()
	sugars = models.FloatField()
	salt = models.FloatField()
	protein = models.FloatField()
	carbohydrates = models.FloatField()
	fibre = models.FloatField()