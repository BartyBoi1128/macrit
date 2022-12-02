from django.test import TestCase
import recipes.utils.nutrition as nutri
from recipes.models import Recipe, Food, User, Profile, Nutrition, Diary
from datetime import datetime

# Create your tests here.


class NutritionTestCase(TestCase):

    def test_BMI_calc(self):
        BMI = nutri.BMI_calc(180, 90)
        self.assertAlmostEqual(BMI, 27.777, 2)

    def test_get_maintenance_calories(self):
        gender = True
        height = 180
        weight = 90
        age = 20
        maintenance_calories = nutri.get_maintenance_calories(
            gender, height, weight, age)
        self.assertAlmostEqual(maintenance_calories, 2069.41)

    def test_needed_fat(self):
        maintenance_calories = 1177.8754
        self.assertAlmostEqual(nutri.needed_fat(
            maintenance_calories), 117.78754)

    def test_needed_saturates(self):
        maintenance_calories = 1177.8754
        self.assertAlmostEqual(nutri.needed_saturates(
            maintenance_calories), 117.78754)

    def test_needed_sugar(self):
        maintenance_calories = 1177.8754
        self.assertAlmostEqual(nutri.needed_sugar(
            maintenance_calories), 29.446885)

    def test_needed_protein(self):
        weight = 90
        self.assertAlmostEqual(nutri.needed_protein(weight), 32.4)

    def test_needed_carbs(self):
        maintenance_calories = 1177.8754
        self.assertAlmostEqual(nutri.needed_carbs(
            maintenance_calories), 161.9578675)

    def test_needed_fibre(self):
        maintenance_calories = 1177.8754
        self.assertAlmostEqual(nutri.needed_fibre(
            maintenance_calories), 16.4902556)

    def test_dict(self):
        user = User.objects.create(userid=21, password="user_pass")
        profile = Profile.objects.create(user=user, first_name="John", second_name="Walsh", height=1.8, weight=90, BMI=nutri.BMI_calc(
            1.8, 90), age=20, gender=True, weight_goal=80, weight_goal_time=datetime(2023, 1, 31), vegetarian=False, vegan=False, tags="")
        maintenance_calories = nutri.get_maintenance_calories(
            True, 180, 90, 20)
        needed_fat = nutri.needed_fat(maintenance_calories)
        needed_saturates = nutri.needed_saturates(maintenance_calories)
        needed_sugar = nutri.needed_sugar(maintenance_calories)
        needed_protein = nutri.needed_protein(90)
        needed_carbs = nutri.needed_carbs(maintenance_calories)
        needed_fibre = nutri.needed_fibre(maintenance_calories)
        nutrition = Nutrition.objects.create(maintenance_calories=maintenance_calories, needed_fat=needed_fat, needed_saturates=needed_saturates,
                                             needed_sugar=needed_sugar, needed_protein=needed_protein, needed_carbs=needed_carbs, needed_fibre=needed_fibre, needed_salt=6)
        diary = Diary.objects.create(profile=profile, nutrition=nutrition)
        carrot = Food.objects.create(name="Carrot", amount=2, calories=50, fat=0.6, saturates=0.4,
                                     sugar=20, salt=0.01, protein=2, carbs=30, fibre=25, tags="vegetarian vegan")
        tomato = Food.objects.create(name="Tomato", amount=2, calories=50, fat=0.6, saturates=0.4,
                                     sugar=20, salt=0.01, protein=2, carbs=30, fibre=25, tags="vegetarian vegan")
        peas = Food.objects.create(name="Peas", amount=2, calories=50, fat=0.6, saturates=0.4,
                                   sugar=20, salt=0.01, protein=2, carbs=30, fibre=25, tags="vegetarian vegan")
        curry = Recipe.objects.create(name="Thai Green Curry", amount=2, calories=200, fat=15,
                                      saturates=6, sugar=30, salt=0.4, protein=50, carbs=36, fibre=25, tags="meat")
        curry.ingredients.add(carrot, tomato, peas)
        curry = Recipe.objects.get(name="Thai Green Curry")
        nutrition_info = nutri.generate_dict(nutrition)
        self.assertAlmostEqual(nutrition_info['needed_calories'], 2069.41)
        detailed_nutrition_info = nutri.dict_decorator(
            nutri.generate_dict, diary, nutrition)(nutri.generate_dict)
