from django.db import models

# Create your models here.
class User(models.Model):
	userid = models.IntegerField(primary_key=True)
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)

	def __str__(self):
		return self.userid + ' ' + self.email

class Profile(models.Model):
	first_name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=100)
	diary = models.OneToOneField(Diary, on_delete=models.CASCADE)
	shopping_list = models.OneToOneField(ShoppingList, on_delete=models.CASCADE)
	height = models.FloatField()
	weight = models.FloatField()
	BMI = models.FloatField()
	age = models.IntegerField()
	gender = models.BooleanField(default=False)
	weight_goal = models.FloatField()
	weight_goal_time = models.DateField()
	vegeterian = models.BooleanField(default=False)
	vegan = models.BooleanField(default=False)
	health_condtions = models.ManyToManyField(HealthCondition)

class HealthCondition(models.Model):
	abstract = True
	health_condition = models.CharField(max_length=100)
	doesUserHave = models.BooleanField(default=False)

class Diary(models.Model):
	intake = ManyToManyField(Ingredient)
	macros = ManyToManyField(Macro)

class Ingredient(models.Model):
	name = models.CharField(max_length=100)
	macros = ManyToManyField(Macro)
	amountOfIngredient = models.FloatField()

class ShoppingList(models.Model):
	ingredients = models.ManyToManyField(Ingredient)

class Recipe(models.Model):
	ingredients = ManyToManyField(Ingredient)
	instructions = models.TextField()
	tags = ListCharField( 
		base_field = CharField(max_length=254),
		size=100,)

class Macro(models.Model):
	abstract = True
	calories = models.FloatField()
	fat = models.FloatField()
	saturates = models.FloatField()
	sugars = models.FloatField()
	salt = models.FloatField()
	protein = models.FloatField()
	carbohydrates = models.FloatField()
	fibre = models.FloatField()